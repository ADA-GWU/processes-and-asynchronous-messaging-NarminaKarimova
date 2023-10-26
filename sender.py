import threading
import psycopg2
import time

# Defining the list of database server IPs
db_server_ips = ["db_server1_ip", "db_server2_ip", "db_server3_ip"]

# Function to insert a record into ASYNC_MESSAGES table
def send_message(sender_name, message, db_ip):
    conn = psycopg2.connect(host=db_ip, user="dist_user", database="your_database")
    cursor = conn.cursor()
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    sql = "INSERT INTO ASYNC_MESSAGES (SENDER_NAME, MESSAGE, SENT_TIME) VALUES (%s, %s, %s)"
    cursor.execute(sql, (sender_name, message, current_time))
    conn.commit()
    conn.close()