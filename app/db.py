import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Conexión a la base de datos usando la URL de la base de datos desde la variable de entorno
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:password@db:5432/market_scrapper"
)


def get_connection():
    """Establece y devuelve una conexión a la base de datos."""
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn
