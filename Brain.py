from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import re

chrome_options = Options()
chrome_options.add_argument("--headless")

# Set the path to your ChromeDriver executable
chrome_driver_path = r'C:\Users\chatu\OneDrive\Desktop\StudyBuddy\Driver\chromedriver.exe'

chrome_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get("https://www.google.com")


def search(text):
    try:
        search_box = driver.find_element("name", "q")

        # Clear the search box content
        search_box.clear()

        # Type the search query
        search_query = text
        search_box.send_keys(search_query)

        # Submit the form
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results to be present (adjust the timeout as needed)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g')))

        # Find the first search result element again
        first_result = driver.find_element(By.CSS_SELECTOR, 'div.g')

        # Extract the link of the first result
        first_result_link = first_result.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')

        # Visit the first result link
        driver.get(first_result_link)

        # Extract the webpage content
        webpage_content = driver.page_source

        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(webpage_content, 'html.parser')

        # Extract text from the webpage, excluding script and style tags
        webpage_text = ' '.join([p.get_text() for p in soup.find_all('p')])

        # Extract keywords or relevant information based on your specific requirements
        # For example, you can use a keyword extraction library or manually define keywords

        # Extract and print the first 8-9 sentences from the webpage text
        sentences = re.split(r'(?<=[.!?])\s', webpage_text)
        result_text = '. '.join(sentences[:9])

        # Navigate back to the Google search page
        driver.back()
        return result_text

        # Clear the search box for the next query

    except Exception as e:
        print("An error occurred:", e)


