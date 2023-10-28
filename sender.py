import psycopg2
import time

# Database connection details for your single database server
db_server_ip = "127.0.0.1"  # Replace with your database server's IP
sender_name = "Narmina"  # Replace with your name

# Function to insert a message into the database
def insert_message(sender_name, message):
    conn = psycopg2.connect(host=db_server_ip, user="postgres", database="hw2")
    cursor = conn.cursor()
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    sql = "INSERT INTO ASYNC_MESSAGES (SENDER_NAME, MESSAGE, SENT_TIME) VALUES (%s, %s, %s)"
    cursor.execute(sql, (sender_name, message, current_time))
    conn.commit()
    conn.close()

# User input and message sending
while True:
    message = input("Enter a message (or type 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    insert_message(sender_name, message)
