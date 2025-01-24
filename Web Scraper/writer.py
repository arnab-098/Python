import pandas as pd
import sys
import os
from typing import List


class Writer:


    def __init__(self, profileInfos: dict, links: List[str], missingLinks: List[str]) -> None:
        self.profileInfos = profileInfos
        self.links = links
        self.missingLinks = missingLinks
        self.VISITED_LINKS_FILE_PATH = "PATH_TO_VISITED_LINKS_FILE"
        self.CSV_FILE_PATH = "PATH_TO_CSV_FILE"
        self.MISSING_LINKS_FILE_PATH = "PATH_MISSING_LINKS_FILE"


    def write(self) -> None:
        self.writeProfileData()
        self.writeMissingLinksData()
        self.writeVisitedLinksData()


    def writeProfileData(self) -> None:
        if len(self.profileInfos["Serial No"]) == 0:
            return
        df = pd.DataFrame(self.profileInfos)
        filePath = self.getFileName(fileName=self.CSV_FILE_PATH)
        df.to_csv(filePath, index=False)
        print(f"\nCSV file {filePath} has been created successfully")
    

    def writeVisitedLinksData(self) -> None:
        if len(self.links) == 0:
            return
        fd = open(self.VISITED_LINKS_FILE_PATH, "a")
        for link in self.links:
            fd.write(link + "\n")
        fd.close()
    

    def writeMissingLinksData(self) -> None:
        if len(self.missingLinks) == 0:
            return
        filePath = self.getFileName(fileName=self.MISSING_LINKS_FILE_PATH)
        fd = open(filePath, "w")
        fd.writelines(self.missingLinks)
        fd.close()
        print(f"\nMissing links file {filePath} has been created successfully")
    

    def getFileName(self, fileName: str) -> str:
        value = 1
        originalFileName: List[str] = fileName.split(".")
        if len(originalFileName) != 2:
            print("\nInvalid file name\nTerminating Program")
            sys.exit()
        while os.path.isfile(fileName):
            value += 1
            fileName = originalFileName[0] + str(value) + "." + originalFileName[1]
        return fileName