from abc import ABC, abstractmethod
from selenium import webdriver
from typing import List

class WebScraper(ABC):

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def login(self, driver: webdriver.Chrome) -> None:
        pass
    
    @abstractmethod
    def findNumberOfMatches(self, driver: webdriver.Chrome) -> int:
        pass
    
    @abstractmethod
    def getLinks(self) -> None:
        pass
    
    @abstractmethod
    def checkMatches(self) -> None:
        pass
    
    @abstractmethod
    def checkMathcesProcess(self, links: List[str]) -> None:
        pass
    
    @abstractmethod
    def checkEachMatch(self, driver: webdriver.Chrome, url: str) -> None:
        pass
    
    @abstractmethod
    def getInfo(self, driver: webdriver.Chrome) -> bool:
        pass
    
    @abstractmethod
    def checkInfo(self) -> bool:
        pass
    
    @abstractmethod
    def populateInfo(self) -> None:
        pass
    
    @abstractmethod
    def populateMissingLinks(self, url: str) -> None:
        pass