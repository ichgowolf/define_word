import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys;
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup


# Get current file path to chromedriver.exe
cwd = os.path.dirname(__file__)
PATH = cwd + "\chromedriver.exe"

# get past cer error
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Driver set
driver = webdriver.Chrome(PATH, options=options,)

driver.get("https://www.dictionary.com/")


#  ASk for words
print ("Type in list of words add one space between words")
undefined = input('input words!: ').split()

#  Access search bar, Loop through each given word, scrape a definition, and place them in a file.
for x in undefined:
	un = x

	try:
		elem = driver.find_element_by_id("global-search")

	except NoSuchElementException:
		time.sleep(5)
		# driver.find_element_by_class_name("bx-close-xsvg").click()
		elem = driver.find_element_by_id("globalSearch")
	# clear()
	elem.send_keys(Keys.CONTROL, "a")
	elem.send_keys(Keys.DELETE)
	elem.send_keys(un)
	elem.send_keys(Keys.RETURN)
	time.sleep(5)
	page_source = driver.page_source

	soup = BeautifulSoup(page_source, 'html.parser')
	defined = []
	word = soup.find('div', class_='css-10ul8x e1q3nk1v2').get_text(" ", strip=True)
	word = word.strip()
	f = open(cwd + "\defined_words.txt", "a", encoding="utf-8")
	f.write(un + " - " + word + '\n' + '\n')
	print (word)

driver.close()