from bs4 import BeautifulSoup
# from selenium import webdriver
import time
import pandas as pd
from classes.Product_Scrapper import Product_Scrapper


class Carrefour_Scrapper(Product_Scrapper):

    def __init__(self):
        super().__init__()
        self.market_name = 'Carrefour'

    def get_products(self, URL: str) -> pd.DataFrame:
        print(f'Getting products from {self.market_name} at {URL}')
        results = []
        contador  = 0
        try:
            self.driver.implicitly_wait(10)  # Aumenta el tiempo de espera
            self.driver.get(URL)

            # Simula el desplazamiento incremental para cargar productos
            # Pausa entre cada scroll
            scroll_pause_time = 3
            # Cantidad de pixeles a desplazar en cada scroll
            scroll_increment = 500
            # current_scroll_position = 0

            while True:
                # Desplazarse hacia abajo en incrementos pequeños
                self.driver.execute_script(
                    f"window.scrollBy(0, {scroll_increment});"
                )
                time.sleep(scroll_pause_time)

                # Capturar el HTML después del desplazamiento

                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                divs = soup.find_all('div')
                print(' Cant de divs: ', len(divs))
                for div in divs:
                    try:
                        if hasattr(div, 'class') and len(div['class']) > 0:
                            class_name = div['class'][0]
                        else:
                            print('No tiene clase')
                            class_name = ''
                        if (
                            'carrefourar-product-summary-status'
                            in class_name
                        ):
                            print('Encontré un producto')
                            spans = div.find_all('span')
                            span = [span for span in spans if any(
                                    'vtex-product-summary-2-x-productBrand'
                                    in cls for cls in span.get('class', [])
                                    )]
                            if len(span) > 0:
                                name = span[0].text.strip()
                            else:
                                print('No encontré nombre')
                                name = "Nombre no disponible"

                            # Filtrar el div que contiene el precio
                            priceSpan = [span for span in spans if any(
                                'valtech-carrefourar-product-price-0-x-currencyContainer'
                                in cls for cls in span.get('class', [])
                            )]
                            # The price is the text inside all inners
                            # spans of first element of priceSpan
                            price = ''
                            if len(priceSpan) > 0:
                                innerSpans = priceSpan[0].find_all('span')
                                for innerSpan in innerSpans:
                                    price += innerSpan.text
                            else:
                                print('No encontré precio')
                                price = "Precio no disponible"

                            if not any(
                                product['name'] == name
                                for product in results
                            ):
                                results.append({
                                    'name': name,
                                    'price': price,
                                    'market': self.market_name
                                })
                    except Exception:
                        pass

                    # new_height = self.driver.execute_script(
                    #     "return document.body.scrollHeight"
                    # )
                    # current_scroll_position += scroll_increment
                    # if current_scroll_position >= new_height:
                        # break
                        
        except IndexError as e:
            print(
                f'''Error getting products
                from {self.market_name} at {URL}'''
            )
            print(f"IndexError: {e}")
        except Exception as e:
            print(
                f'''Error getting products
                from {self.market_name} at {URL}'''
            )
            # variables_relevantes = locals()
            # print(print(f"Estado de las variables: {variables_relevantes}"))
            print(e)
        return pd.DataFrame(results)
