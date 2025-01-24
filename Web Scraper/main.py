import multiprocessing
from abpScraper import ABPScraper
from webScraper import WebScraper


def main(profileInfos, missingLinks, visitedLinkCount) -> None:
    scraper: WebScraper = ABPScraper(profileInfos, missingLinks, visitedLinkCount)
    scraper.run()


if __name__ == "__main__":
    manager = multiprocessing.Manager()
    profileInfos = manager.dict()
    missingLinks = manager.list()
    visitedLinkCount = manager.Value("i", 0)
    try:
        main(profileInfos, missingLinks, visitedLinkCount)
    except KeyboardInterrupt:
        print("\nProgram Terminated by User")