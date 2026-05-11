def execute_batch_insert(cursor, query, records):
    cursor.executemany(query, records)