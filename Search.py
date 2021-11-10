import time
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search:
    def __init__(self, url, driver, key_word, count_deep_seek_page, current_website):
        self.driver = driver
        self.url = url
        self.key_word = key_word
        self.count_deep_seek_page = count_deep_seek_page
        self.current_website = current_website

    def set_options_and_fake_agent(self):
        ua = UserAgent()
        user_agent = ua.random
        options = Options()

        options.add_argument("--disable-extensions")
        options.add_argument("--headless")
        options.add_argument("--window-size=1920x1080")
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = self.driver.Chrome(options=options)
        print(f'[+] set fake user_agent {user_agent}')

    def go_to_search_page(self):
        try:
            self.driver.get(f'{self.url}')
            self.driver.find_element(By.CSS_SELECTOR, "input#text").send_keys(self.key_word, Keys.RETURN)
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.organic__url.link")))
        except ValueError:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul#search-result")))
            print(ValueError)

    def find_all_websites(self):
        websites = self.driver.find_elements(By.CSS_SELECTOR, "h2.organic__title-wrapper a.organic__url.link")
        links = [elem.get_attribute('href') for elem in websites]
        return links

    def check_current_websites(self, websites):
        page = 0
        count_deep_seek_page = self.count_deep_seek_page

        while page < count_deep_seek_page:
            print(f'==== Start loop websites ====')

            self._loop_website(websites=websites, page=page)

            page += 1
            current_page = f'{str(self.url)}/search/?lr=109993&text={self.key_word.replace(" ", "+")}&p={str(page)}'
            print('current_page', current_page)

            self.driver.get(current_page)
            print(f'Start next page #{page}')

    def _loop_website(self, websites, page):
        for link in websites:
            # if link attr not contains STOP words
            if link.find("yandex") == -1:
                print(f'Website link: {link}')
                self.driver.get(link)
                time.sleep(20000)
                self.driver.back()
            else:
                pass
        print(f'Finish page#{page}')

    def behavioral_factor(self):
        print(1)