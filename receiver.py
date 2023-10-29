import psycopg2
import threading
import time

# Flag to control the reader threads
terminate_reader = False

def read_available_messages(sender_name, conn):
    global terminate_reader
    cursor = conn.cursor()

    while not terminate_reader:
        try:
            cursor.execute('SELECT SENDER_NAME, MESSAGE, SENT_TIME FROM ASYNC_MESSAGES WHERE RECEIVED_TIME IS NULL AND SENDER_NAME = %s LIMIT 1',
                           (sender_name,))
            message = cursor.fetchone()

            if message:
                sender, message_text, sent_time = message
                received_time = time.strftime('%Y-%m-%d %H:%M:%S')
                print(f'Sender {sender} sent "{message_text}" at time {sent_time}')
                cursor.execute('UPDATE ASYNC_MESSAGES SET RECEIVED_TIME = %s WHERE SENDER_NAME = %s AND RECEIVED_TIME IS NULL',
                               (received_time, sender))
                conn.commit()

            time.sleep(1)
        except psycopg2.Error as e:
            print(f"Error: {e}")

# Replace 'server1_ip', 'server2_ip', etc. with actual IP addresses
db_server_ips = ['127.0.0.1', '192.168.0.108']
connections = []

# Create connections to each database server
for ip in db_server_ips:
    conn = psycopg2.connect(
        dbname='db',
        user='narminakarimova',
        password='1234',
        host=ip,
        port='5432'
    )
    connections.append(conn)

# Define the sender_name variable or retrieve it from the sender
sender_name = 'Shamsiyya'

print("Reader is listening...")
reader_threads = []

for conn in connections:
    reader_thread = threading.Thread(target=read_available_messages, args=(sender_name, conn))
    reader_threads.append(reader_thread)
    reader_thread.start()

print("Press 'q' and Enter to stop the reader threads.")
while not terminate_reader:
    user_input = input()
    if user_input.lower() == 'q':
        terminate_reader = True

for reader_thread in reader_threads:
    reader_thread.join()

for conn in connections:
    conn.close()
"""import psycopg2
import threading
import time

# Flag to control the reader thread
terminate_reader = False

def read_available_messages(sender_name):
    global terminate_reader  # Allow the thread to access the flag

    while not terminate_reader:
        cursor.execute('SELECT SENDER_NAME, MESSAGE, SENT_TIME FROM ASYNC_MESSAGES WHERE RECEIVED_TIME IS NULL AND SENDER_NAME = %s LIMIT 1',
                       (sender_name,))
        message = cursor.fetchone()

        if message:
            sender, message_text, sent_time = message
            received_time = time.strftime('%Y-%m-%d %H:%M:%S')
            print(f'Sender {sender} sent "{message_text}" at time {sent_time}')
            cursor.execute('UPDATE ASYNC_MESSAGES SET RECEIVED_TIME = %s WHERE SENDER_NAME = %s AND RECEIVED_TIME IS NULL',
                           (received_time, sender))
            conn.commit()

        time.sleep(1)  # Adjust the interval as needed

# Create a PostgreSQL database connection
conn = psycopg2.connect(
    dbname='db',
    user='narminakarimova',
    password='1234',
    host='127.0.0.1',
    port='5432'
)
cursor = conn.cursor()

# Define the sender_name variable or retrieve it from the sender
sender_name = 'Narmina'

print("Receiver is listening...")  # Display a listening message

reader_thread = threading.Thread(target=read_available_messages, args=(sender_name,))
reader_thread.start()

# Allow the thread to run, but add an option to stop it
print("Press 'q' and Enter to stop the receiver.")
while not terminate_reader:
    user_input = input()
    if user_input.lower() == 'q':
        terminate_reader = True

reader_thread.join()  # Wait for the thread to finish"""


