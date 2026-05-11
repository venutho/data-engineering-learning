from python_refresh.db.postgres_connection import get_db_connection
from python_refresh.db.base_loader import execute_batch_insert
from python_refresh.etl.fetch_comments import fetch_comments
from python_refresh.config.logger_config import logger
from python_refresh.etl.transform_comments import transform_comment
import time

def main():
    connection = None
    cursor = None  
    try:
        logger.info("Starting ETL process")
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO comments (post_id, id, name, email, body)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
        """

        comments = fetch_comments()

        transformed_comments = [transform_comment(comment) for comment in comments]

        starts = time.time() 

        execute_batch_insert(cursor, query, transformed_comments)
        connection.commit()
        ends = time.time() 
        logger.info(f"{len(transformed_comments)} comments loaded successfully in {ends - starts:.4f} seconds")
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