from letterboxedhelpers import get_movie_info, get_movie_rating

def main():
    print("Welcome to Grant's Letterboxd Database!")
    while True:
        print("\nChoose an option:")
        print("1️ Search for a movie")
        print("2 Show all ratings above a certain score")
        print("3️ Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            get_movie_info()
        elif choice == "2":
            from letterboxedhelpers import get_movie_rating
            get_movie_rating()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()