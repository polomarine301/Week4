# Your Name: Mark Aceto
# Course Number: Object-Oriented Computer Prog
# Lab Title: Country


import os

project_name = "Country"

# Check if Git is installed
if os.system("git --version"):
    print("Git is not installed. Please install Git and try again.")
    exit()

# Create a new directory for the project
os.mkdir(project_name)

# Change into the project directory
os.chdir(project_name)

# Initialize a new Git repository
os.system("git init")

# Step 6 ends here

# Step 7: Write and test the code for the lab.

# Part 1: Display heading and menu choices
def display_menu():
    print("Welcome to Country Info!")
    print("1. View a country")
    print("2. Add a country")
    print("3. Delete a country")
    print("4. Exit")

# Part 2: Prepopulate a dictionary with country keys and names
country_dict = {"USA": "United States", "CAN": "Canada", "GBR": "United Kingdom"}

# Part 3: Menu functions
def view_country(country_dict):
    print("Available countries:")
    for key in country_dict.keys():
        print(key, "-", country_dict[key])

    user_input = input("Enter a country code to view details: ")
    if user_input in country_dict:
        print(f"Country: {country_dict[user_input]}")
    else:
        print("Invalid country code!")

def add_country(country_dict):
    key = input("Enter a new country code: ")
    if key in country_dict:
        print("Country code already exists!")
    else:
        name = input("Enter the country name: ")
        country_dict[key] = name
        print("Country added successfully!")

def delete_country(country_dict):
    key = input("Enter the country code to delete: ")
    if key in country_dict:
        del country_dict[key]
        print("Country deleted successfully!")
    else:
        print("Invalid country code!")

# Main program
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_country(country_dict)
    elif choice == "2":
        add_country(country_dict)
    elif choice == "3":
        delete_country(country_dict)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
