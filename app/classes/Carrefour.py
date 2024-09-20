from classes.Product_Scrapper import Product_Scrapper


class Carrefour_Scrapper(Product_Scrapper):

    def __init__(self):
        super().__init__()
        self.market_name = 'Carrefour'
        self.base_url = 'https://www.carrefour.com.ar'

    def extract_product_info(self, soup, results, market_name):
        divs = soup.find_all('div')
        for div in divs:
            try:
                class_name = div['class'][0]
                if 'carrefourar-product-summary-status' in class_name:
                    print('Encontré un producto')
                    spans = div.find_all('span')

                    # Buscar el span que contiene la marca del producto
                    span = [span for span in spans if any(
                        'vtex-product-summary-2-x-productBrand'
                        in cls for cls in span.get('class', [])
                    )]

                    # Si existe, el nombre es el texto dentro del span
                    # de lo contrario "Nombre no disponible"
                    name = span[0].text.strip()\
                        if span\
                        else "Nombre no disponible"

                    # Filtrar el div que contiene el precio
                    priceSpan = [span for span in spans if any(
                        'currencyContainer'
                        in cls for cls in span.get('class', [])
                    )]

                    # Obtener el texto de los spans internos
                    # que contienen el precio
                    price = ''
                    if priceSpan:
                        innerSpans = priceSpan[0].find_all('span')
                        for innerSpan in innerSpans:
                            price += innerSpan.text.strip()
                    else:
                        print('No encontré precio')
                        price = "Precio no disponible"

                    # Evitar duplicados en los resultados
                    if not any(product['name'] == name for product in results):
                        results.append({
                            'name': name,
                            'price': price,
                            'market': market_name
                        })
            except Exception:
                pass

        return results
