from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/agroblock"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_database_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print("Connection to the database successful. Result:", result)
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)


if __name__ == '__main__':
    test_database_connection()