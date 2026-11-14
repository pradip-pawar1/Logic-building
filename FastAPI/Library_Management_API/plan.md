# Book Library Management API


## Books data structure
| Field |	Type |	Example |
| :--- | :--- | :--- |
| id |	`str` |	B001 |
| title |	`str` |	Atomic Habits |
| author |	`str` |	James Clear |
| publication_year |	`int` |	2018 |
| genre |	`str` |	Self-help |
| is_available |	`bool` |	True |

### Sample JSON data
```json
{
    "B001": {
        "title": "Atomic Habits",
        "author": "James Clear",
        "publication_year": 2018,
        "genre": "Self-help",
        "is_available": true
    }
}
```

## Featured operations

| Method |	Endpoint |	Purpose |
| :--- | :--- | :--- |
| POST |	/books |	Add a new book |
| GET |	/books |	Display all books |
| GET |	/books/{book_id} |	Get a specific book |
| PUT |	/books/{book_id} |	Update a book |
| DELETE |	/books/{book_id} |	Delete a book |

> Get should allow sorting in order way

---

### A. CRUD operations

Implement all five endpoints. Handle situations such as:
- Book ID doesn't exist.
- Duplicate book IDs.
- Empty book collection.
- Invalid input data.

### B. Path parameters
Use book_id to retrieve, update and delete a particular book.

Example: /books/5

### C. Query parameters

Implement filtering through query parameters.

Examples:
- /books?genre=self-help
- /books?author=James
- /books?is_available=true
You can support multiple filters together.

### D. Pagination

This is an important requirement.

Implement:

>/books?page=1&limit=5

Your API should:
- Return only the requested number of books.
- Calculate the correct starting index.
- Handle invalid page numbers and limits.
- Return pagination metadata.

```json
{
    "page": 1,
    "limit": 5,
    "total_books": 23,
    "total_pages": 5,
    "books": []
}
```

### E. Pydantic and Field

Create a Pydantic model for book creation.

Practice:
- Required fields.
- Optional fields.
- Default values.
- Field() constraints.
- String length validation.
- Numeric validation.
- Boolean fields.



## Rules for this practice

1. Don't use SQLAlchemy or any database. JSON only.
2. Use Python's built-in json module for reading and writing.
3. Use Pydantic for request validation.
4. Use appropriate HTTP status codes.
5. Use HTTPException for error handling.
6. Generate IDs automatically.
7. Make sure every modification is persisted in books.json.
8. Test every endpoint using Swagger UI (/docs).