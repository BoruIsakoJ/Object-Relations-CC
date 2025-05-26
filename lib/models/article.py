# Article class with SQL methods
from ..db import get_connection
conn = get_connection()
cursor = conn.cursor()
class Article:
    all ={}
    def __init__(self,title,author_id,magazine_id,id=None):
        self.id = id
        self.title = title
        self.author_id =author_id
        self.magazine_id = magazine_id
        
    def __repr__(self):
        return f"<Article {self.id}: {self.title}>"
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if type(title) == str and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")
        
    def save(self):
        sql ="""
            INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)    
        """
        cursor.execute(sql,(self.title,self.author_id,self.magazine_id))
        conn.commit()
        
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql ="""
            UPDATE articles SET title =?, author_id =?, magazine_id =? WHERE id =?     
        """
        cursor.execute(sql,(self.title, self.author_id, self.magazine_id, self.id))
        conn.commit()
 
    def delete(self):
        sql = """
            DELETE FROM articles WHERE id = ?
        """
        
        cursor.execute(sql, (self.id,))
        conn.commit()
        
        del type(self).all[self.id]
        
        self.id = None        

    @classmethod
    def instance_from_db(cls, row):
        if not row:
            return None
        article = cls.all.get(row[0])
        if article:
            article.title = row[1]
            article.author_id = row[2]
            article.magazine_id = row[3]
        else:
            article = cls(row[1], row[2], row[3], id= row[0])
            cls.all[article.id] = article
        return article

    @classmethod
    def get_all(cls):
        sql ="""
        SELECT * FROM articles
        """
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM articles WHERE id = ?
        """
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT * FROM articles WHERE title = ?
        """
        row = cursor.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None