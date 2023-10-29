Asynchronous Messaging with Sender and Receiver

Welcome to the Asynchronous Messaging project! This README provides step-by-step instructions on how to download, configure, and run the sender and receiver scripts on macOS. This system allows you to send and receive messages across multiple PostgreSQL databases simultaneously.


Getting Started

Create a Project Folder: Begin by creating a dedicated folder on your desktop named "hw2." This folder will serve as the central location for organizing your project files.



Clone the Repository: Open your terminal and navigate to the "hw2" folder using the cd command. Replace "your-github-link" with the actual GitHub repository link provided by your instructor.

shell
Copy code
cd ~/Desktop/hw2
git clone "your-github-link"
Install Python: Ensure that Python is installed on your macOS. If you don't already have Python, you can follow the installation instructions provided in your previous homework. You can download Python from the official website.

Access the Code: Once you've successfully cloned the repository, navigate to the "processes-and-asynchronous-messaging-NarminaKarimova" folder within your "hw2" directory.

Open Code Editor: If you prefer to use Visual Studio Code as your code editor, you can open it with a simple command:

shell
Copy code
code .
Customizing the Code
Edit Sender and Receiver Scripts: Inside the "processes-and-asynchronous-messaging-NarminaKarimova" folder, locate the Python scripts sender.py and receiver.py. These scripts contain the following customizable fields:

db_server_ips: Replace the list of database server IP addresses with the actual IP addresses of your PostgreSQL database servers.
database: Replace this field with your specific database name.
user: Replace with your database username.
password: Input your database password.
Make sure your database is properly configured to listen on port 5432.

Running the Code

Sender Script: Open two new terminal windows, one for the sender and one for the receiver. Ensure you navigate to the "processes-and-asynchronous-messaging-NarminaKarimova" folder in both terminals.


In the first terminal, initiate the sender script by running:

shell
Copy code
python sender.py
Follow the prompts and enter your messages.

Receiver Script: In the second terminal, initiate the receiver script with:

shell
Copy code
python receiver.py
You will receive available messages from the configured databases.

Quitting the Scripts

Sender Script: To exit the sender script, type "exit" or use Ctrl+C in the sender terminal.

Receiver Script: To quit the receiver script, simply type "q" Ctrl+C in the receiver terminal.

You now have the complete source code and detailed instructions for running the sender and receiver software on macOS. Simply follow these steps, customize the code as necessary, and enjoy asynchronous messaging across multiple PostgreSQL databases. We hope you have a great experience using this asynchronous messaging system!
