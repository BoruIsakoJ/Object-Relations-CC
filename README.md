# Articles Code Challenge 

## Project Overview

This project models the relationships between Authors, Articles, and Magazines with data persisted in a SQLite database. It demonstrates raw SQL query integration with Python classes to handle CRUD operations and relationships in an object-oriented manner.

### Key Features
- Authors can write multiple articles.
- Magazines publish multiple articles.
- Articles belong to both an author and a magazine.
- Many-to-many relationship between authors and magazines through articles.

---

## Project Structure

```
code-challenge/
├── lib/
│   ├── models/
│   │   ├── author.py
│   │   ├── article.py
│   │   └── magazine.py
│   ├── db/
│   │   ├── connection.py
│   │   ├── seed.py
│   │   └── schema.sql
│   └── __init__.py
├── scripts/
│   ├── setup_db.py
│   └── run_queries.py
├── tests/
│   ├── test_author.py
│   ├── test_article.py
│   └── test_magazine.py
├── .gitignore
├── Pipfile
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repo

```bash
git clone git@github.com:BoruIsakoJ/Object-Relations-CC.git 
```
### 2. Navigate to the Cloned Repo

```bash
cd code-challenge
```

### 3. Set Up Virtual Environment Using Pipenv

Install and activate the virtual environment:

```bash
pipenv install && pipenv shell
```

### 3. Initialize the Database

Run the setup script to create tables and seed(add) data in to the database:

```bash
python scripts/setup_db.py
```

### 4. Run Example Queries

After setup, you can execute example queries with:

```bash
python scripts/run_queries.py
```

---

## Contributing

Feel free to open issues or submit pull requests. Please follow the existing code style and include tests for new features.

---