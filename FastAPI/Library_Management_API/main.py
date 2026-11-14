from supports import Support

from fastapi import FastAPI, HTTPException
from fastapi import Path, Query

from pydantic import Field, field_validator, computed_field
from pydantic import BaseModel

app = FastAPI()

# ------------------ | Checks & Validation | --------------- 

class Details(BaseModel):
    '''This is a basic check form data verification'''
    title           : str = Field(..., description="Name of book", examples=["Atomic Habits"])
    author          : str = Field(..., description="Name of an author", examples=["James clear"])
    publication_year: int = Field(..., gt=999, le=2026, description="year of book published", examples=[2005])
    gener           : str = Field(..., examples=["self-help"])

    @field_validator("author")
    @classmethod
    def check_author(cls, value) -> str:
        if value.replace(" ", "").isalpha():
            raise ValueError("Author cannot conatin numeric or special character")
        return value.title()

    @computed_field
    @property
    def new_id() -> str:
        return Support.create_id()


# ------------------ | API | --------------- 

# home route
@app.get('/')
def home():
    return{"message":"Welcome to Book Library Management System"}

# pagination
@app.get('/pages')
def pages(
    page : int = Query(1, ge=1, le=100, description="number of page you want to view"),
    limit : int = Query(4, ge=4, le=10, description="Amount of data you want to see on a single page"),
    sort_by : str = "title",
    order : str = "asc"
):
    # important data 
    FIELD = ["id", "title", "author", "publication_year", "gener"]
    SORT_ORDER = ["asc", "dsc"]
    START = (page - 1) * limit
    END = START + limit

    # pagination logic
    if sort_by not in FIELD:
        raise HTTPException(
            status_code=404,
            detail=f"you can only sort by {FIELD}"
        )

    if order not in SORT_ORDER:
        raise HTTPException(
            status_code=404,
            detail=f"you can only sort by {SORT_ORDER}"
        )

    data = Support.load_data()

    is_descending = (order=="dsc")
    sorted_items = sorted(data.items(), key=lambda x: x[1][sort_by], reverse=is_descending)
    pages = sorted_items[START:END]

    return {
        "page":page,
        "limit":limit,
        "Sort_by":sort_by,
        "data on page":len(pages),
        "data":pages
    }
    

# create/add new book in database
@app.post('/add')
def add_book(book:Details):
    # load data
    data = Support.load_data()

    data[book.new_id] = book.model_dump(exclude={"new_id"})
    Support.save_data(data)

    return {
        "message":"New book added successfully",
        "data":book.model_dump()
    }


