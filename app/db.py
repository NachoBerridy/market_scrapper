from sqlalchemy import create_engine
import os


def get_connection() -> create_engine:
    """
    Get connection to database
    """
    # Get credentials from environment variables
    DATABASE_URL = os.getenv("DATABASE_URL")

    print(f"Connecting to {DATABASE_URL}")

    engine = create_engine(DATABASE_URL)

    conn = engine.connect()

    return conn
