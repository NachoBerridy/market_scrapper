from classes.Mas_Online import Mas_Online_Scrapper
from classes.Carrefour import Carrefour_Scrapper
import pandas as pd
from db import get_connection
from models import create_table

if __name__ == "__main__":
    URLS_MAS = [
        "https://www.masonline.com.ar/3454?map=productClusterIds",
    ]

    URLS_CARREFOUR = ["https://www.carrefour.com.ar/almacen"]

    mas_online_scrapper = Mas_Online_Scrapper()

    results_mas = []
    for URL in URLS_MAS:
        results_mas.append(mas_online_scrapper.get_products(URL))

    df_mas = pd.concat(results_mas, ignore_index=True)

    carrefour_scrapper = Carrefour_Scrapper()
    results_carr = []
    for URL in URLS_CARREFOUR:
        results_carr.append(carrefour_scrapper.get_products(URL))

    df_carrefour = pd.concat(results_carr, ignore_index=True)

    for market, df in zip(["Mas Online", "Carrefour"], [df_mas, df_carrefour]):
        df["market"] = market

    create_table()

    conn = get_connection()
    with conn.cursor() as cursor:
        for _, row in df_mas.iterrows():
            cursor.execute(
                """
                INSERT INTO products (name, price, market)
                VALUES (%s, %s, %s);
                """,
                (row["name"], row["price"], row["market"]),
            )
        conn.commit()
    conn.close()

    conn = get_connection()
    with conn.cursor() as cursor:
        for _, row in df_carrefour.iterrows():
            cursor.execute(
                """
                INSERT INTO products (name, price, market)
                VALUES (%s, %s, %s);
                """,
                (row["name"], row["price"], row["market"]),
            )
        conn.commit()
    conn.close()

    # Verificar que los datos se hayan insertado correctamente

    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM products;")
        results = cursor.fetchall()

        for row in results:
            print(row)
    conn.close()
