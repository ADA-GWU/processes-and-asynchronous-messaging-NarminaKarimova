import psycopg2
import threading
import time

# Function to read and process available messages
def read_available_messages(sender_name, conn):
    cursor = conn.cursor()

    while True:
        try:
            cursor.execute('SELECT RECORD_ID, SENDER_NAME, MESSAGE, SENT_TIME FROM ASYNC_MESSAGES WHERE RECEIVED_TIME IS NULL AND SENDER_NAME != %s LIMIT 1 FOR UPDATE',
                           (sender_name,))
            message = cursor.fetchone()

            if message:
                record_id, sender, message_text, sent_time = message
                received_time = time.strftime('%Y-%m-%d %H:%M:%S')
                print(f'Sender {sender} sent "{message_text}" at time {sent_time}')
                cursor.execute('UPDATE ASYNC_MESSAGES SET RECEIVED_TIME = %s WHERE RECORD_ID = %s',
                               (received_time, record_id))
                conn.commit()
        except psycopg2.Error as e:
            print(f"Error: {e}")

# Define the list of database server IPs here
db_server_ips = ['127.0.0.1', '192.168.0.108']
connections = []

# Create connections to each database server
for ip in db_server_ips:
    conn = psycopg2.connect(
        host=ip,
        database="db",
        user="narminakarimova",
        password="1234",
        port="5432"
    )
    connections.append(conn)

# Define your sender_name
sender_name = 'Narmina'

# Create threads for reading and processing messages
reader_threads = []
for conn in connections:
    reader_thread = threading.Thread(target=read_available_messages, args=(sender_name, conn))
    reader_threads.append(reader_thread)
    reader_thread.start()

# Wait for user input to stop
print("Press 'q' and Enter to stop the reader threads.")
while True:
    user_input = input()
    if user_input.lower() == 'q':
        break

# Stop the reader threads
for reader_thread in reader_threads:
    reader_thread.join()

# Close all database connections when done
for conn in connections:
    conn.close()



