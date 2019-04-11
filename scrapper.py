from selenium import webdriver


class Scrapper:
    ip_port = "181.52.237.106:36060"

    def __init__(self):
        chrome_driver = "C:/chromedriver_win32/chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument('--proxy-server={}'.format(self.ip_port))

        self._driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
        self._sentences = []
        self._audio = None
        self._details = None

    def scrape(self, word):
        self._driver.get("https://www.vocabulary.com/dictionary/{}".format(word))
        self._sentences = []
        self._audio = None
        self._details = None

        audio = self._driver.find_element_by_css_selector('a.audio')
        self._audio = audio.get_attribute('data-audio')

        details = self._driver.find_element_by_css_selector('p.short')
        self._details = details.get_attribute('innerHTML')

        content = self._driver.find_element_by_css_selector('div.exampleBrowser')
        lines = content.find_elements_by_class_name('sentence')

        for li in lines:
            self._sentences.append(li.get_attribute('innerHTML'))

        return self

    def examples(self):
        return self._sentences

    def audio(self):
        return self._audio

    def details(self):
        return self._details

    def close(self):
        self._driver.close()


if __name__ == '__main__':
    scrapper = Scrapper()
    scrape = scrapper.scrape('banish')
    print(scrape.examples())
    print(scrape.audio())
    scrapper.close()
