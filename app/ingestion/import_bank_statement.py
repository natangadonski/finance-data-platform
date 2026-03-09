import csv
from pathlib import Path
from app.database.models import create_transactions_table

# Function responsible for loading a bank statement in CSV format.
# Receives the file path and returns a list of transactions
def load_bank_statement(file_path: str):

    # List that will store all transactions read from the CSV.
    transactions = []

    # Open the CSV file
    # "with" ensures the file is automatically closed after use
    with open(file_path, newline = "", encoding = "utf-8") as csvfile:

        # DictReader reads the CSV and converts each row into a dictionary
        # using the column headers as keys
        reader = csv.DictReader(csvfile)

        # Iterate through each row in the CSV file
        for row in reader:

            # Add the row (transaction) to the transactions list
            transactions.append(row)

    # Return the list of loaded transactions
    return transactions

# This block ensures the code below only runs when this script is executed directly
if __name__ == "__main__":

    # Ensure the transactions table exists before processing data
    create_transactions_table()

    # Path to the bank statement CSV file
    path = "data/raw/sample_statement.csv"

    # Call the function that loads the CSV data
    transactions = load_bank_statement(path)

    # Iterate through the loaded transactions
    for t in transactions:

        # Print each transaction to the terminal
        print(t)