import mysql.connector
import pandas as pd
from datetime import datetime

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rrk@1729",
    database="bank_management"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()
def insert_customer():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    phone = int(input("Enter Phone: "))

    query = "INSERT INTO Customers (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, email, phone)

    cursor.execute(query, values)
    conn.commit()
    insert_account()

    print("Customer added successfully!")


def display_customers():
    query = "SELECT * FROM Customers"
    cursor.execute(query)
    customers = cursor.fetchall()

    print("Customer ID | First Name | Last Name  | Email                | Phone")
    print("---------------------------------------------------------------------")
    for customer in customers:
        print(f"{customer[0]}           | {customer[1]}     | {customer[2]}      | {customer[3]}  | {customer[4]}")
# Function to insert a new account into the database
def insert_account():
    customer_id = int(input("Enter Customer ID: "))
    acc_type = input("Enter Account Type (e.g., Savings, current): ")
    acc_no=int(input("enter account_no"))
    balance=int(input("enter balance:"))
    query = "INSERT INTO Account (acc_no,customer_id, acc_type,balance) VALUES (%s, %s,%s,%s)"
    values = (acc_no,customer_id, acc_type,balance)

    cursor.execute(query, values)
    conn.commit()

    print("Account added successfully!")
 # Function to fetch and display all accounts from the database    
def display_account():
    query = "SELECT * FROM Account"
    cursor.execute(query)
    account = cursor.fetchall()

    print("Account no| Customer ID | Account Type |balance")
    print("----------------------------------------")
    for account in account:
        print(f"{account[0]}          | {account[1]}           | {account[2]}   |{account[3]}")       

        
class transaction:
    
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn
        
    def deposit(self):
            
        acc_no = int(input("Enter Account number: "))
        amount = float(input("Enter Deposit Amount: "))

        # Update account balance
        query = "UPDATE Account SET balance = balance + %s WHERE acc_no = %s"
        values = (amount, acc_no)
        self.cursor.execute(query, values)

        # Record the transaction
        transaction_type = 'Deposit'
        transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO Transaction (acc_no, transaction_type, amount, transaction_date) VALUES (%s, %s, %s, %s)"
        values = (acc_no, transaction_type, amount, transaction_date)
        self.cursor.execute(query, values)

        self.conn.commit()
        print("Deposit successful!")
    
    def withdraw(self):
        acc_no = int(input("Enter Account number: "))
        amount = float(input("Enter Withdrawa Amount: "))

        # Check if there's sufficient balance
        df_acc = pd.read_sql_query("SELECT * FROM Account WHERE acc_no = %s",con=conn,params=(acc_no,))
        current_balance = df_acc.loc[0,'balance']
        print(current_balance)
        #query_balance = "SELECT balance FROM Account WHERE acc_no = %s"
        #values_balance = (amount,acc_no)
        #self.cursor.execute(query_balance, values_balance)
        #current_balance = self.cursor.fetchone()[0]

        if amount > current_balance:
            print("Insufficient balance for withdrawal.")
        else:
    

            # Update account balance
            query_update_balance = "UPDATE Account SET balance = balance - %s WHERE acc_no = %s"
            values_update_balance = (amount, acc_no)
            self.cursor.execute(query_update_balance, values_update_balance)

           # Record the transaction
            transaction_type = 'withdrawa'
            transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query_record_transaction = "INSERT INTO transaction (acc_no, transaction_type, amount, transaction_date) VALUES (%s, %s, %s, %s)"
            values_record_transaction = (acc_no, transaction_type, amount, transaction_date)
            self.cursor.execute(query_record_transaction, values_record_transaction)

            self.conn.commit()
            print("withdrawa successful!")

    def view_transaction(self):
        acc_no = int(input("Enter Account number: "))
        
        final = pd.read_sql_query("SELECT * FROM transaction WHERE acc_no = %s",con=conn,params=(acc_no,))
        print(final)
