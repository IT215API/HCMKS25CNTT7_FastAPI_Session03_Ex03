from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": False
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2025,
        "is_available": True
    }
]

@app.get("/books/statistics")
def get_statistics_books():
    count_available = 0
    count_borrowed = 0
    for item in books:
        if item.get("is_available") == True:
            count_available += 1
        else:
            count_borrowed += 1
    return {
        "total_books": len(books),
        "available_books": count_available,
        "borrowed_books": count_borrowed
    }


@app.get("/books/categories")
def get_categories_books():
    categories_list = []
    for item in books:
        if item.get("category") not in categories_list:
            categories_list.append(item.get("category"))
    return {
        "categories": categories_list
    }


@app.get("/books/latest")
def get_latest_book():
    if not books:
        return {
            "message": "No books available"
        }
    
    latest_book = books[0]
    for item in books:
        if item.get("year") > latest_book.get("year"):
            latest_book = item
    return latest_book
