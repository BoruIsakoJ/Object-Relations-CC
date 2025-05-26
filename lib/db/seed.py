# Seed data for testing
from .connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()
    
    authors = [
        ("Ngũgĩ wa Thiong’o",),           # Celebrated author
        ("Yvonne Adhiambo Owuor",),       # Award-winning writer
        ("Hanifa Farsafi",),              # Goated Activist 
        ("Wanjiru Kihoro",),              # Political activist and feminist
        ("Binyavanga Wainaina",)          # Renowned author and journalist
    ]
    
    magazines = [
        ("The East African", "News"),
        ("True Love", "Lifestyle"),
        ("Parents Africa", "Family"),
        ("Business Daily", "Finance"),
        ("Drum Magazine", "Culture")
    ]    
    

    articles = [
        ("The Legacy of African Languages", 1, 1),
        ("Reimagining Nairobi in Fiction", 2, 5),
        ("Women in Kenyan Politics", 3, 1),
        ("Parenting in a Digital Age", 4, 3),
        ("Why Africa Will Write Back", 5, 5)
    ]


    cursor.executemany("INSERT INTO authors(name) VALUES (?)",authors)
    cursor.executemany("INSERT INTO magazines(name,category) VALUES (?,?)",magazines)
    cursor.executemany("INSERT INTO articles(title,author_id,magazine_id) VALUES (?,?,?)", articles)
    
    conn.commit()
    conn.close()
    
    
if __name__ == '__main__':
    seed_data()