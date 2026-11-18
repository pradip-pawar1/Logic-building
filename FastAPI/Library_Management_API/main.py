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
        if not value.replace(" ", "").isalpha():
            raise ValueError("Author cannot conatin numeric or special character")
        return value.title()

    @field_validator("title")
    @classmethod
    def format_title(cls, value) -> str:
        return value.title()


class Verify(BaseModel):
    '''This class will checks for updated data'''
    title : str | None = Field(None)
    author : str | None = Field(None)
    publication_year : int | None = Field(None, gt=999, le=2026, examples=[2005])
    gener : str | None = Field(None, examples=["self-help"])

    @field_validator("author")
    @classmethod
    def check_author(cls, value) -> str:
        if not value.replace(" ", "").isalpha():
            raise ValueError("Author cannot conatin numeric or special character")
        return value.title()

    @field_validator("title")
    @classmethod
    def format_title(cls, value) -> str:
        return value.title()


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
@app.post('/add', status_code=201)
def add_book(book:Details):
    # load data
    data = Support.load_data()

    new_id = Support.create_id()

    data[new_id] = book.model_dump()
    Support.save_data(data)

    return {
        "message":"New book added successfully",
        "assign ID": new_id,
        "data": book.model_dump()
    }


@app.put('/update/{book_id}', status_code=200)
def update(check:Verify,
           book_id : str = Path(..., description="Id of the book", examples=["B001"])
           ):

    data = Support.load_data()

    # check if book id is valid or not
    if not book_id in data:
        raise HTTPException(
            status_code=404,
            detail=f"{book_id} was not found in DB, please try with correct ID"
        )

    updated_data = check.model_dump(exclude_unset=True)
    data[book_id].update(updated_data)
    Support.save_data(data)

    return {
        "Message": "Book detail updated succesfully",
        "Updated fields": updated_data,
        "Book": data[book_id]
    }

@app.delete('/delete/{book_id}', status_code=204)
def delete(book_id: str = Path(..., description="provide valid book id", examples=["B001"])):

    data = Support.load_data()

    if not book_id in data:
        raise HTTPException(
            status_code=404,
            detail=f"ID not found in DB"
        )

    del data[book_id]
    Support.save_data(data)

    return {
        "Message":f"Book no.{book_id} deleted succesfully"
    }
