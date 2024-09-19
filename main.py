from classes.Mas_Online import Mas_Online_Scrapper
import pandas as pd

if __name__ == '__main__':

    URLS = [
        'https://www.masonline.com.ar/3454?map=productClusterIds',
        'https://www.masonline.com.ar/3454?map=productClusterIds&page=2',
    ]

    mas_online_scrapper = Mas_Online_Scrapper()

    results = []
    for URL in URLS:
        results.append(mas_online_scrapper.get_products(URL))

    df = pd.concat(results, ignore_index=True)

    print(df)
