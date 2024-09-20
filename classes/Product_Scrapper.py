from selenium import webdriver


class Product_Scrapper:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_experimental_option(
            'excludeSwitches',
            ['enable-logging']
        )
        self.driver = webdriver.Chrome(options=self.options)
        self.market_name = None
