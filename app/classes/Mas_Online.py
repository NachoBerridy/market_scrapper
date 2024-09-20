from classes.Product_Scrapper import Product_Scrapper
import time
import pandas as pd
from bs4 import BeautifulSoup


class Mas_Online_Scrapper(Product_Scrapper):

    def __init__(self):
        super().__init__()
        self.market_name = 'Mas Online'

    def get_products(self, URL: str) -> pd.DataFrame:
        print(f'Getting products from {self.market_name} at {URL}')
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
                self.driver.execute_script(
                    f"window.scrollBy(0, {scroll_increment});"
                )
                time.sleep(scroll_pause_time)

                # Capturar el HTML después del desplazamiento

                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                divs = soup.find_all('div')
                for div in divs:
                    try:
                        class_name = div['class'][0]
                        if 'product-summary-status' in class_name:
                            spans = div.find_all('span')
                            interDivs = div.find_all('div')
                            span = [span for span in spans if any(
                                    'productBrand' in cls for cls in
                                    span.get('class', [])
                                    )]
                            name = span[0].text.strip()\
                                if span\
                                else "Nombre no disponible"

                            # Filtrar el div que contiene el precio
                            priceDiv = [div for div in interDivs if any(
                                'dynamicProductPrice' in cls
                                for cls in div.get('class', [])
                            )]
                            price = priceDiv[0].text.strip()\
                                if priceDiv\
                                else "Precio no disponible"
                            if not any(
                                result['name'] == name for result in results
                            ):
                                results.append({'name': name, 'price': price})
                    except Exception:
                        pass

                # Verificar si hemos alcanzado el final de la página
                new_height = self.driver.execute_script(
                    "return document.body.scrollHeight"
                )
                current_scroll_position += scroll_increment
                if current_scroll_position >= new_height:
                    break

            # Convertir los resultados a DataFrame
            products = pd.DataFrame(results)
            return products
        except Exception as e:
            print('An error occurred', e)
