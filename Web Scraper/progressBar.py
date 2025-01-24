class ProgressBar:


    PREFIX = "Progress:" 
    SUFFIX = "Complete"
    DECIMALS = 1
    LENGTH = 100
    FILL = '█'
    PRINT_END = "\r"
    

    @staticmethod
    def printProgressBar(iteration: int, total: int) -> None:
        percent = ("{0:." + str(ProgressBar.DECIMALS) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(ProgressBar.LENGTH * iteration // total)
        bar = ProgressBar.FILL * filledLength + '-' * (ProgressBar.LENGTH - filledLength)
        print(f'\r{ProgressBar.PREFIX} |{bar}| {percent}% {ProgressBar.SUFFIX}', end = ProgressBar.PRINT_END)
        if iteration == total: 
            print()