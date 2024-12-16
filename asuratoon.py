from bs4 import BeautifulSoup
import requests

links = (
'https://asuratoon.com/manga/1908287720-the-greatest-estate-developer/', 
'https://asuratoon.com/manga/1908287720-myst-might-mayhem/', 
'https://asuratoon.com/manga/1908287720-reaper-of-the-drifting-moon/',
'https://asuratoon.com/manga/1908287720-mr-devourer-please-act-like-a-final-boss/',
'https://asuratoon.com/manga/1908287720-the-max-level-players-100th-regression/',
'https://asuratoon.com/manga/1908287720-martial-god-regressed-to-level-2/',
'https://asuratoon.com/manga/1908287720-the-player-hides-his-past/',
'https://asuratoon.com/manga/1908287720-revenge-of-the-iron-blooded-sword-hound/',
'https://asuratoon.com/manga/1908287720-the-main-characters-that-only-i-know/'
)

file = '/home/lazyboy/Desktop/Programs/Bots/asuraData'

def main():

	f = open(file, 'r+')
	data = f.readlines()
	f.close()

	change = False
	
	for index, link in enumerate(links):
		html_page = requests.get(link).text
		soup = BeautifulSoup(html_page, 'lxml')
		name = soup.find('h1', class_ = 'entry-title').text.strip()
		content = soup.find('ul', class_ = 'clstyle').text.strip().split()
		chapter = content[1]
		if chapter != data[index][:-1]:
			change = True
			data[index] = chapter + '\n'
			print(f'{name} : {chapter}')

	if change == True:
		f = open(file, 'w')
		f.writelines(data)
		f.close()
	else:
		print("No new chapters")


if __name__ == "__main__":
	main()

