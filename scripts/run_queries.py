# Script to run example queries
# run_queries.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine


def menu():
    print("\nSelect an option:")
    print("0. Exit")
    print("1. List all authors")
    print("2. Find author by name")
    print("3. Find author by id")
    print("4. Create new author")
    print("5. Update existing author")
    print("6. Delete existing author")
    print("7. List all magazines")
    print("8. Create new magazine")
    print("9. List all articles")
    print("10. Create new article")


def main():
    while True:
        menu()
        choice = input("> ")

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            authors = Author.get_all()
            for author in authors:
                print(author)
        
        elif choice == "2":
            name = input("Enter the author's name: ")
            author = Author.find_by_name(name)
            print(author) if author else print(
                f'Author {name} not found')
        
        elif choice == "3":
            id = int(input("Enter the author's id: "))
            author = Author.find_by_id(id)
            print(author) if author else print(
                f'Author {id} not found')

        elif choice == "4":
            name = input("Enter author name: ")
            author = Author(name)
            author.save()
            print("Author saved!")
            
        elif choice == "5":
            id = int(input("Enter the author's id: "))
            if author:= Author.find_by_id(id):
                try:
                    name = input("Enter the author's new name: ")
                    author.name = name
                    
                    author.update()
                    print(f"Success {author}")
                except Exception as exc:
                    print(f"Error updating author: {exc}")
            else:
                print(f"Author {id} not found.")
                
        elif choice == "6":
            id = int(input("Enter the employee's id: "))
            if author := Author.find_by_id(id):
                author.delete()
                print(f"Author {id} deleted.")
            else:
                print(f"Author {id} not found.")

        elif choice == "7":
            magazines = Magazine.get_all()
            for mag in magazines:
                print(mag)

        elif choice == "8":
            name = input("Enter magazine name: ")
            category = input("Enter magazine category: ")
            try:
                id_ = int(input("Enter magazine id: "))
                magazine = Magazine(name, category, id_)
                magazine.save()
                print("Magazine saved!")
            except ValueError:
                print("ID must be a number.")
                

        elif choice == "9":
            articles = Article.get_all()
            for article in articles:
                print(article)

        elif choice == "10":
            title = input("Enter article title: ")
            try:
                magazine_id = int(input("Enter magazine id: "))
                author_id = int(input("Enter author id: "))
                article = Article(title, magazine_id, author_id)
                article.save()
                print("Article saved!")
            except ValueError:
                print("Magazine and Author IDs must be integers.")
        else:
            print("Invalid option, try again.")
            
            


if __name__ == "__main__":
    main()

