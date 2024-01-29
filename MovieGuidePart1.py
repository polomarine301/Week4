# Your Name: Mark Aceto
# Course Number: Object-Oriented Computer Prog
# Lab Title: MovieGuidePart1



import os

project_name = "MovieGuidePart1"

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
    print("Welcome to Movie Guide!")
    print("1. Display all titles")
    print("2. Add a title")
    print("3. Delete a title")
    print("4. Exit")

# Part 2: Prepopulate a list with movie titles
movie_titles = ["Movie1", "Movie2", "Movie3"]

# Part 3: Menu functions
def display_all_titles(movie_list):
    print("Movie Titles:")
    for title in movie_list:
        print(title)

def add_title(movie_list, new_title):
    movie_list.append(new_title)
    print("Movie added successfully!")

def delete_title(movie_list, title_to_delete):
    if title_to_delete in movie_list:
        movie_list.remove(title_to_delete)
        print("Movie deleted successfully!")
    else:
        print("Movie not found!")

# Main program
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_all_titles(movie_titles)
    elif choice == "2":
        new_movie = input("Enter the new movie title: ")
        add_title(movie_titles, new_movie)
        display_all_titles(movie_titles)
    elif choice == "3":
        title_to_remove = input("Enter the movie title to delete: ")
        delete_title(movie_titles, title_to_remove)
        display_all_titles(movie_titles)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
