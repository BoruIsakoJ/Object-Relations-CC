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
    print("8. Find author by name")
    print("9. Find author by id")
    print("10. Create new magazine")
    print("11. Update existing magazine")
    print("12. Delete existing magazine")
    print("13. List all articles")
    print("14. Create new article")
    print("15. Delete existing article")


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
            name = input("Enter the magazine's name: ")
            magazine = Magazine.find_by_name(name)
            print(magazine) if magazine else print(
                f'magazine {name} not found')
        
        elif choice == "9":
            id = int(input("Enter the magazine's id: "))
            magazine = Magazine.find_by_id(id)
            print(magazine) if magazine else print(
                f'Magazine {id} not found')

        elif choice == "10":
            name = input("Enter magazine name: ")
            category = input("Enter magazine category: ")
            try:
                magazine = Magazine(name, category)
                magazine.save()
                print("Magazine saved!")
            except ValueError:
                print("ID must be a number.")
                
        elif choice == "11":
            id = int(input("Enter the magazine's id: "))
            if magazine := Magazine.find_by_id(id):
                try:
                    name = input("Enter the magazine's new name: ")
                    magazine.name = name
                    category = input("Enter the magazine's new category: ")
                    magazine.category = category
                    magazine.update()
                    print(f"Success: {magazine}")
                except Exception as exc:
                    print(f"Error updating magazine: {exc}")
            else:
                print(f"Magazine {id} not found")
                
        elif choice == "12":
            id = int(input("Enter the magazine's id: "))
            if magazine := Magazine.find_by_id(id):
                magazine.delete()
                print(f"Magazine {id} deleted")
            else:
                print(f"Magazine {id} not found")                

        elif choice == "13":
            articles = Article.get_all()
            for article in articles:
                print(article)

        elif choice == "14":
            title = input("Enter article title: ")
            try:
                magazine_id = int(input("Enter magazine id: "))
                author_id = int(input("Enter author id: "))
                article = Article(title, magazine_id, author_id)
                article.save()
                print("Article saved!")
            except ValueError:
                print("Magazine and Author IDs must be integers.")
        
        elif choice == "15":
            id = int(input("Enter the article's id: "))
            if article := Article.find_by_id(id):
                article.delete()
                print(f"Article {id} deleted")
            else:
                print(f"Article {id} not found")   
        
        
        else:
            print("Invalid option, try again.")
            
            


if __name__ == "__main__":
    main()

