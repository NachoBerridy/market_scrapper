from classes.Mas_Online import Mas_Online_Scrapper
from classes.Carrefour import Carrefour_Scrapper
import pandas as pd

if __name__ == '__main__':

    URLS_MAS = [
        'https://www.masonline.com.ar/3454?map=productClusterIds',
    ]

    URLS_CARREFOUR = [
        'https://www.carrefour.com.ar/almacen'
    ]

    mas_online_scrapper = Mas_Online_Scrapper()

    results = []
    # for URL in URLS_MAS:
    #     results.append(mas_online_scrapper.get_products(URL))

    # df_mas = pd.concat(results, ignore_index=True)
    # print(df_mas)

    carrefour_scrapper = Carrefour_Scrapper()

    for URL in URLS_CARREFOUR:
        results.append(carrefour_scrapper.get_products(URL))

    df_carrefour = pd.concat(results, ignore_index=True)
    print(df_carrefour)
