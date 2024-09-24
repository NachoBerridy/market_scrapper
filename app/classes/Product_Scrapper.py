from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


class Product_Scrapper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=self.options)
        self.market_name = None

    def get_products(self, URL: str) -> pd.DataFrame:
        """
        Get products from Carrefour
        * URL: URL to scrape
        * Returns: DataFrame with products
        """
        print(f"Getting products from {self.market_name} at {URL}")
        results = []

        try:
            self.driver.implicitly_wait(10)  # Aumenta el tiempo de espera
            self.driver.get(URL)

            # Simula el desplazamiento incremental para cargar productos
            # Pausa entre cada scroll
            scroll_pause_time = 3
            # Cantidad de pixeles a desplazar en cada scroll
            scroll_increment = 500
            current_scroll_position = 0

            while True:
                # Desplazarse hacia abajo en incrementos pequeños
                self.driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
                time.sleep(scroll_pause_time)

                # Capturar el HTML después del desplazamiento

                soup = BeautifulSoup(self.driver.page_source, "html.parser")

                results = self.extract_product_info(soup, results, self.market_name)
                new_height = self.driver.execute_script(
                    "return document.body.scrollHeight"
                )
                current_scroll_position += scroll_increment
                if current_scroll_position >= new_height:
                    break

        except IndexError as e:
            print(
                f"""Error getting products
                from {self.market_name} at {URL}"""
            )
            print(f"IndexError: {e}")
        except Exception as e:
            print(
                f"""Error getting products
                from {self.market_name} at {URL}"""
            )
            # variables_relevantes = locals()
            # print(print(f"Estado de las variables: {variables_relevantes}"))
            print(e)
        return pd.DataFrame(results)

    def extract_product_info(soup, results, market_name):
        raise NotImplementedError(
            "Subclass must implement abstract method extract_product_info"
        )
