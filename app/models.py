from db import get_connection


def create_table():
    """Crea la tabla de productos si no existe."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        market VARCHAR(255),
        date_scraped TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    # Ejecutar la consulta de creación de tabla
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)
            conn.commit()
        print("Tabla 'products' creada exitosamente (si no existía).")
    except Exception as e:
        print(f"Error creando la tabla: {e}")
    finally:
        conn.close()
