import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int


class Book(BookCreate):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Implement GET /books and GET /books/{book_id}.
# TODO: Add POST /books, PUT /books/{book_id}, and DELETE /books/{book_id}.


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)