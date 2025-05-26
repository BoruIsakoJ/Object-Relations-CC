# Script to run example queries
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

author1 = Author("Boru Isako")
author1.save()

authors = Author.get_all()
for author in authors:
    print(author)

magazine1 = Magazine("Technologiaaa", "Technology", 6)
magazine1.save()

magazines = Magazine.get_all()
for magazine in magazines:
    print(magazine)

article1 = Article("AI Revolution", 6, 4)
article1.save()

articles = Article.get_all()
for article in articles:
    print(article)
