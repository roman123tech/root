import csv

# Function to get all unique items from transactions
def get_unique_items(transactions):
    unique_items = set()
    for transaction in transactions:
        unique_items.update(transaction)
    return list(unique_items)

# Backtracking function to generate all possible groupings
def generate_groupings(items, index, current_group, all_groupings):
    # If we have processed all items, store the current grouping
    if index == len(items):
        all_groupings.append(list(current_group))  # Make a copy of current_group
        return
    
    # Option 1: Do not include the current item (skip it)
    generate_groupings(items, index + 1, current_group, all_groupings)
    
    # Option 2: Include the current item in the current group
    current_group.append(items[index])
    generate_groupings(items, index + 1, current_group, all_groupings)
    current_group.pop()  # Backtrack by removing the last item
    
    # Option 3: Start a new group with the current item (create a new group)
    all_groupings.append([items[index]])
    generate_groupings(items, index + 1, current_group, all_groupings)

# Write the generated groupings to an output CSV file
def write_groupings_to_csv(output_file, groupings):
    with open(output_file, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Grouping'])  # Header
        for grouping in groupings:
            csv_writer.writerow([', '.join(grouping)])

# Main function
def main(input_file, output_file):
    # Read transactions from CSV
    transactions = read_transactions_from_csv(input_file)
    
    # Get all unique items from the transactions
    unique_items = get_unique_items(transactions)
    
    # Generate all possible groupings using backtracking
    all_groupings = []
    generate_groupings(unique_items, 0, [], all_groupings)
    
    # Write the groupings to the output CSV file
    write_groupings_to_csv(output_file, all_groupings)
    print(f"All possible groupings written to {output_file}")

# Helper function to read transactions from CSV
def read_transactions_from_csv(input_file):
    transactions = []
    with open(input_file, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            transaction = [item for item in row[1:] if item]  # Ignore TID and empty values
            transactions.append(transaction)
    return transactions

# Run the main function
input_file = 'ip.csv'   # Input CSV file containing transactions
output_file = 'generated_groupings.csv'  # Output CSV file for groupings
main(input_file, output_file)
