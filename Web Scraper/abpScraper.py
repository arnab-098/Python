import multiprocessing.process
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from typing import List
import multiprocessing
import sys

from webScraper import WebScraper
from reader import Reader
from writer import Writer
from progressBar import ProgressBar

class ABPScraper(WebScraper):


    def __init__(self, profileInfos, missingLinks, visitedLinkCount) -> None:
        self.profileInfos = profileInfos
        self.profileInfos["Serial No"] = []
        self.profileInfos["Id"] = []
        self.profileInfos["Name"] = []
        self.profileInfos["Age"] = []
        self.profileInfos["Height"] = []
        self.profileInfos["Present Location"] = []
        self.profileInfos["Hometown"] = []
        self.profileInfos["Caste"] = []
        self.profileInfos["Education"] = []
        self.profileInfos["Profession"] = []
        self.profileInfos["Salary"] = []
        self.missingLinks = missingLinks
        self.visitedLinkCount = visitedLinkCount
        self.LOGIN_URL = "https://www.abpweddings.com/"
        self.MATCH_URL = "https://www.abpweddings.com/my-matches"
        self.WAIT_DURATION = 10
        self.PROCESS_COUNT = 5
    

    def run(self) -> None:
        reader = Reader()
        self.username, self.password = reader.getCredentials()
        self.visitedLinks: set = reader.getVisitedLinks()
        self.getLinks()
        self.checkMatches()
        writer = Writer(dict(self.profileInfos), self.links, list(self.missingLinks))
        writer.write()
    

    def login(self, driver: webdriver.Chrome) -> None:
        driver.get(self.LOGIN_URL)

        try:
            loginButton = driver.find_element(By.ID, "landingPage_topbar_register")
            loginButton.click()
            passwordButton = driver.find_element(By.ID, "landPage_login_IhavePasswd_text")
            passwordButton.click()
            inputField = driver.find_element(By.CLASS_NAME, "input_email")
            inputField.send_keys(self.username)
            passwordField = driver.find_element(By.CLASS_NAME, "input_password")
            passwordField.send_keys(self.password)
            submitButton = driver.find_element(By.ID, "landPage_login_loginWithPassword_loginNow")
            submitButton.click()
            sleep(2)

        except NoSuchElementException:
            print("\nFailed to login\nTerminating Program")
            sys.exit()


    def findNumberOfMatches(self, driver: webdriver.Chrome) -> int:
        try:
            numOfMatches = driver.find_element(By.CLASS_NAME, "active-btn").find_element(By.CLASS_NAME, "number-color").text
            if numOfMatches == 0:
                print("\nNo matches found\nTerminating Program")
                sys.exit()
            return int(numOfMatches)

        except NoSuchElementException:
            print("\nNo matches found\nTerminating Program")
            sys.exit()
    

    def getLinks(self) -> None:
        driver: webdriver.Chrome = webdriver.Chrome()
        driver.implicitly_wait(self.WAIT_DURATION)

        self.login(driver=driver)

        driver.get(self.MATCH_URL)
        sleep(1)

        try:
            print("\nLoading...")

            numberOfMatches = self.findNumberOfMatches(driver=driver)

            elements = driver.find_elements(By.CLASS_NAME, "matches-box1 ")
            while len(elements) < numberOfMatches:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                sleep(0.5)
                elements = driver.find_elements(By.CLASS_NAME, "matches-box1 ")
                ProgressBar.printProgressBar(len(elements), numberOfMatches)

            print("\nFinding your matches...")

            self.links = []
            for idx, element in enumerate(elements):
                data = element.find_element(By.TAG_NAME, "a").get_attribute("href")
                if data not in self.visitedLinks:
                    self.links.append(data)
                ProgressBar.printProgressBar(idx+1, numberOfMatches)
            
            if len(self.links) == 0:
                print("\nNo new matches found\nTerminating Program")
                sys.exit()

        except NoSuchElementException:
            print("\nFailed to find matches\nTerminating Program")
            sys.exit()
        
        driver.quit()
    

    def checkMatches(self) -> None:
        print("\nGathering information on your matches...")

        self.totalLinkCount: int = len(self.links)

        self.detailsMutex= multiprocessing.Lock()
        self.missingLinkMutex = multiprocessing.Lock()
        self.countMutex = multiprocessing.Lock()

        processArray: List[multiprocessing.Process] = []

        chunkSize = len(self.links) // self.PROCESS_COUNT

        linkArray: List[str] = []

        for i in range (self.PROCESS_COUNT):
            if i < self.PROCESS_COUNT-1:
                linkArray = self.links[i*chunkSize: (i+1)*chunkSize]
            else:
                linkArray = self.links[i*chunkSize:]
            processArray.append(multiprocessing.Process(target= self.checkMathcesProcess, args=(linkArray,)))
        
        for i in range (self.PROCESS_COUNT):
            processArray[i].start()
        
        for i in range (self.PROCESS_COUNT):
            processArray[i].join()


    def checkMathcesProcess(self, links: List[str]) -> None:
        driver: webdriver.Chrome = webdriver.Chrome()
        driver.implicitly_wait(self.WAIT_DURATION)

        self.login(driver=driver)

        for idx, link in enumerate(links):
            self.checkEachMatch(driver=driver, url=link)
            with self.countMutex:
                self.visitedLinkCount.value += 1
                ProgressBar.printProgressBar(self.visitedLinkCount.value, self.totalLinkCount)

        driver.quit()

   
    def checkEachMatch(self, driver: webdriver.Chrome, url: str) -> None:
        driver.get(url)

        self.info = self.getInfo(driver=driver)

        if not self.getInfo(driver=driver):
            self.populateMissingLinks(url=url)
            return 

        if not self.checkInfo():
            self.populateMissingLinks(url=url)
            return 

        self.populateInfo()
    

    def getInfo(self, driver: webdriver.Chrome) -> bool:
        try:
            info1 = driver.find_element(By.CLASS_NAME, "new-profile-text").text
            info2 = driver.find_element(By.CLASS_NAME, "name-detail").text
            info3 = [element.text for element in driver.find_elements(By.CLASS_NAME, "coloninbefore")]
            self.info = [info1, info2, info3]
            return True

        except NoSuchElementException:
            return False
    

    def checkInfo(self) -> bool:
        if self.info[0] == "":
            return False

        if len(self.info[1].split(", ")) != 2:
            return False

        if len(self.info[2]) != 53:
            return False

        return True
    

    def populateInfo(self) -> None:
        with self.detailsMutex:
            self.profileInfos["Serial No"] += [str(len(self.profileInfos["Serial No"]) + 1)]
            self.profileInfos["Id"] += [self.info[0]]
            self.profileInfos["Name"] += [str(self.info[1].split(", ")[0])]
            self.profileInfos["Age"] += [str(self.info[1].split(", ")[1])]
            self.profileInfos["Height"] += [self.info[2][7]]
            self.profileInfos["Present Location"] += [self.info[2][1]]
            self.profileInfos["Hometown"] += [self.info[2][39]]
            self.profileInfos["Caste"] += [self.info[2][50]]
            self.profileInfos["Education"] += [self.info[2][15]]
            self.profileInfos["Profession"] += [self.info[2][10]]
            self.profileInfos["Salary"] += [self.info[2][14]]


    def populateMissingLinks(self, url: str) -> None:
        with self.missingLinkMutex:
            self.missingLinks.append(url + "\n")