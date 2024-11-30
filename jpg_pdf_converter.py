import os
from PIL import Image
from typing import List
import sys


class Convert:
    def __init__(self, directory: str) -> None:
        self.checkDirectory(directory)
        self.imageDirectory: str = directory
        self.findImages()

    def __str__(self) -> str:
        return "This is used to convert jpg or png files to pdf files"

    def findImages(self) -> None:
        self.imagePaths: List[str] = [
            file
            for file in os.listdir(self.imageDirectory)
            if file.endswith(".jpg") or file.endswith(".png")
        ]
        if len(self.imagePaths) == 0:
            print("No jpg or png files found in the directory!")
            print("Exiting program")
            sys.exit(1)
        return

    def checkDirectory(self, directory: str) -> None:
        if not os.path.exists(directory):
            print("Directory not found!\nExiting program")
            sys.exit(1)
        return

    def displayFiles(self) -> None:
        for idx, imagePath in enumerate(self.imagePaths):
            print(f"{idx+1}: {imagePath}")
        return

    def validateChoice(self, choices: List[str]) -> bool:
        for choice in choices:
            if (
                not choice.isdigit()
                or int(choice) <= 0
                or int(choice) > len(self.imagePaths)
            ):
                return False
        return True

    def selectFiles(self) -> None:
        choices: List[str] = []
        self.displayFiles()
        while True:
            print("Enter the index numbers in order your want to make the pdf")
            choices = input().split(" ")
            if self.validateChoice(choices):
                break
            else:
                print("Invalid choice! Please try again")
        files: List[str] = list(self.imagePaths)
        self.imagePaths = []
        for choice in choices:
            self.imagePaths.append(files[int(choice) - 1])
        return

    def convert(self) -> None:
        self.selectFiles()
        images = [Image.open(path) for path in self.imagePaths]
        pdfPath = self.imageDirectory + "/output.pdf"
        images[0].save(
            pdfPath, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
        )
        print("Successfully converted into a pdf")


def main() -> None:
    imageDirectory = input("Enter the file path of the image directory: ")
    converter = Convert(imageDirectory)
    print(converter)
    converter.convert()
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting Program")
        sys.exit(2)
