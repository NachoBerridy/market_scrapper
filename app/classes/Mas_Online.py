from classes.Product_Scrapper import Product_Scrapper


class Mas_Online_Scrapper(Product_Scrapper):

    def __init__(self):
        super().__init__()
        self.market_name = 'Mas Online'
        self.base_url = 'https://www.masonline.com.ar'

    def extract_product_info(soup, results, market_name):
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
                        results.append({
                            'name': name,
                            'price': price,
                            'market': market_name
                        })
            except Exception:
                pass

        return results
