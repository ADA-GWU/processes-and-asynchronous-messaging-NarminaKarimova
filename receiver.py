import psycopg2
import time

# Database connection details for your single database server
db_server_ip = "127.0.0.1"  # Replace with your database server's IP

# Function to read and update messages
def read_and_update_message():
    conn = psycopg2.connect(host=db_server_ip, user="postgres", database="hw2")
    cursor = conn.cursor()

    while True:
        cursor.execute("""
            SELECT * FROM ASYNC_MESSAGES
            WHERE RECEIVED_TIME IS NULL
            LIMIT 1
            FOR UPDATE
        """)
        message = cursor.fetchone()

        if message:
            sender_name, msg, sent_time = message[1], message[2], message[3]
            print(f"Sender {sender_name} sent '{msg}' at time {sent_time}.")
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("UPDATE ASYNC_MESSAGES SET RECEIVED_TIME = %s WHERE RECORD_ID = %s", (current_time, message[0]))
            conn.commit()

    conn.close()

# Start the reader
read_and_update_message()
