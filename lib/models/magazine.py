# Magazine class with SQL methods
from ..db import get_connection
conn = get_connection()
cursor = conn.cursor()

class Magazine:
    all={}
    def __init__(self,name,category, id=None):
        self.id = id
        self.name = name
        self.category = category
        
    def __repr__(self):
        return f"<Magazine {self.id}: {self.name} - {self.category}>"
    
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if type(name)==str and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )         
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if type(category)==str and len(category):
            self._category = category
        else:
            raise ValueError(
                "Category must be a non-empty string"
                )
            
    def save(self):
        sql = """
            INSERT INTO magazines (name, category)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.name, self.category))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE magazines
            SET name = ?, category = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.category, self.id))
        conn.commit()

    def delete(self):
        sql = """
            DELETE FROM magazines
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
        magazine = cls.all.get(row[0])
        if magazine:
            magazine.name = row[1]
            magazine.category = row[2]
        else:
            magazine = cls(row[1], row[2], id=row[0])
            cls.all[magazine.id] = magazine
        return magazine

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM magazines"
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM magazines WHERE id = ?"
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row)

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM magazines WHERE name = ?"
        row = cursor.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row)
    
    def articles(self):
        from article import Article
        sql = """
            SELECT * FROM articles
            WHERE magazine_id = ?
        """
        rows = cursor.execute(sql, (self.id,)).fetchall()
        return [Article.instance_from_db(row) for row in rows]

    def contributors(self):
        from author import Author
        sql = """
            SELECT DISTINCT authors.*
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        """
        rows = cursor.execute(sql, (self.id,)).fetchall()
        return [Author.instance_from_db(row) for row in rows]

    def article_titles(self):
        sql = """
            SELECT title FROM articles
            WHERE magazine_id = ?
        """
        rows = cursor.execute(sql, (self.id,)).fetchall()
        return [row[0] for row in rows]

    def contributing_authors(self):
        from author import Author
        sql = """
            SELECT authors.*, COUNT(articles.id) as article_count
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING article_count > 2
        """
        rows = cursor.execute(sql, (self.id,)).fetchall()
        return [Author.instance_from_db(row) for row in rows]
