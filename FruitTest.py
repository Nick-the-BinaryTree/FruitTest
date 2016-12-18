import sys
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    fruits = ["apple", "banana", "orange", "avocado", "lime", "strawberry", "orange", "coconut"]
    index = 0
    length = len(fruits)-1
    scrollScript = "window.scrollTo(0, document.body.scrollHeight);"
    Y = 0

    numFruits = int(sys.argv[1])

    driver = webdriver.Chrome(executable_path="C:\\Users\Administrator\Downloads\chromedriver.exe")
    driver.get("http://images.google.com")

    while numFruits > 0:
        index = random.randint(0, length)

        searchBar = driver.find_elements_by_name("q")[0]
        searchBar.clear()
        slowType(fruits[index], searchBar)
        searchBar.send_keys(Keys.RETURN)

        time.sleep(1)
        while Y < 2000:
            driver.execute_script("window.scrollTo(0, " + str(Y) + ");")
            Y += 1

        Y = 0
        time.sleep(2)
        numFruits -= 1

def slowType(str, searchBar):
    for char in str:
        searchBar.send_keys(char)
        time.sleep(.2)

if __name__ == "__main__":
    main()