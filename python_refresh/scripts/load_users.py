from python_refresh.db.postgres_connection import get_db_connection
from python_refresh.db.base_loader import execute_batch_insert
from python_refresh.etl.fetch_users import fetch_users
from python_refresh.config.logger_config import logger
from python_refresh.etl.transform_users import transform_user

def main():
    connection = None
    cursor = None  
    try:
        logger.info("Starting ETL process")
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO users (id, name, email, city, company)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
        """

        users = fetch_users()
        transformed_users = [transform_user(user) for user in users]

        execute_batch_insert(cursor, query, transformed_users)        
        connection.commit()
        logger.info(f"{len(transformed_users)} users loaded successfully")
    except Exception as error:
        logger.exception("Error during ETL process")
        if connection:
            connection.rollback()
    finally:
        cursor and cursor.close()
        connection and connection.close()
        logger.info("Database connection closed")        


if __name__ == "__main__":
    main()