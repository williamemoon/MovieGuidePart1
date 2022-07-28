# William Moon 
# CIS 261 
# MovieGuidePart1 Week 4 Lab 1


# Function that will display a heading and menu choices
def show_menu():
    print("Bill's Movie List Program")
    print("")
    print("Menu: Type the following commands to modify the list")
    print("------------------------------------------------------")
    print("list - Display the List of Movies")
    print("add - Add a Movie to the List")
    print("delete - Delete a Movie from the List")
    print("exit - Exit the program")
    print(" ")
    
    
# List funciton
def list(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print(f"{i}. {movie}")
    print(" ")
    
# Add function
def add(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added to the list.")
    print(" ")

# Delete function
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid selection, try again:")
        print(" ")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie} was removed from the list")
        print(" ")

# Main program function with loop
def main():
    movie_list = ["Citizen Cane",
                  "The Godfather",
                  "Star Trek II: The Wrath of Khan"]

    show_menu()

    while True: 
        comand = input("Enter Comand From Program Command List: ")
        if comand.lower() == "list":
           list(movie_list)
        elif comand.lower() == "add":
            add(movie_list)
        elif comand.lower() == "delete":
            delete(movie_list)
        elif comand.lower() == "exit":
            break
        else:
            print("That's not a valid command.  Please try again.")
            print("")

    print("Ending Program")
     
if __name__ == "__main__":
    main()








