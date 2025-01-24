import sys
from typing import Tuple


class Reader:


    def __init__(self) -> None:
        self.CREDENTIALS_FILE_PATH = "PATH_TO_CREDENTIALS_FILE"
        self.VISITED_LINKS_FILE_PATH = "PATH_TO_VISITED_LINKS_FILE"
    

    def getCredentials(self) -> Tuple[str, str]:
        try:
            fd = open(self.CREDENTIALS_FILE_PATH, "r")
            content = fd.readlines()
            if len(content) != 2:
                print("\nFailed to get credentials\nTerminating Program")
                sys.exit()
            line1 = str(content[0]).split(":")
            line2 = str(content[1]).split(":")
            if len(line1) != 2 or len(line2) != 2:
                print("\nFailed to get credentials\nTerminating Program")
                sys.exit()
            USERNAME: str = line1[1].strip()
            PASSWORD: str = line2[1].strip()
            fd.close()

        except OSError:
            print("\nFailed to get credentials\nTerminating Program")
            sys.exit()

        return (USERNAME, PASSWORD)
    

    def getVisitedLinks(self) -> set:
        fd = open(self.VISITED_LINKS_FILE_PATH, "r")
        content = fd.readlines()
        for idx, line in enumerate(content):
            content[idx] = line.strip()
        visitedLinks = set(content)
        fd.close()
        return visitedLinks