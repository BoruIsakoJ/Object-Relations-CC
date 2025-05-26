# Author class with SQL methods
from ..db import get_connection
conn = get_connection()
cursor = conn.cursor()
class Author:
    all ={}
    def __init__(self, name,id=None):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return f"<Author {self.id}: {self.name}>"

        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if type(name) == str and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )      
        
    def save(self):
        sql = """
            INSERT INTO authors (name)
            VALUES (?)
        """
        cursor.execute(sql, (self.name,))
        conn.commit()

        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    
    @classmethod
    def create(cls,name):
        author = cls(name)
        author.save()
        return author
    
    def update(self):
        sql = """
            UPDATE authors
            SET name = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name,self.id))
        conn.commit()
        
    def delete(self):
        sql = """
            DELETE FROM authors
            WHERE id = ?
        """
        
        cursor.execute(sql, (self.id,))
        conn.commit()
        
        del type(self).all[self.id]
        
        self.id = None
        
    @classmethod
    def instance_from_db(cls, row):

        if not row:
            return None
        # Check the dictionary for an existing instance using the row's primary key
        author = cls.all.get(row[0])
        if author:
            # ensure attributes match row values in case local instance was modified
            author.name = row[1]
        else:
        # not in dictionary, create new instance and add to dictionary
            author = cls(row[1])
            author.id = row[0]
            cls.all[author.id] = author
        return author
        
    @classmethod
    def get_all(cls):
        """Return a list containing a Author object per row in the table"""
        sql = """
            SELECT *
            FROM authors
            """

        rows = cursor.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
        
        
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM authors
            WHERE id = ?
        """

        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM authors
            WHERE name = ?
        """

        row = cursor.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def articles(self):
        """Return list of articles written by the author"""
        from article import Article
        sql = """
            SELECT * FROM articles
            WHERE author_id = ?
        """
        cursor.execute(sql, (self.id,),)

        rows = cursor.fetchall()
        return [
            Article.instance_from_db(row) for row in rows
        ]
        
    def magazines(self):
        """Return list of unique magazines the author has written articles for"""
        from magazine import Magazine
        sql = """
            SELECT DISTINCT magazines.*
            FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        """
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        return [Magazine.instance_from_db(row) for row in rows]
    
    def add_article(self, magazine, title):
        """Create and save a new article by the author in the given magazine"""

        from article import Article
        article = Article(title=title, author_id=self.id, magazine_id=magazine.id)
        article.save()
        return article

    def topic_areas(self):
        """Return a list of unique categories the author has written in"""

        sql = """
            SELECT DISTINCT magazines.category
            FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        """
        cursor.execute(sql, (self.id,))
        return [row[0] for row in cursor.fetchall()]
