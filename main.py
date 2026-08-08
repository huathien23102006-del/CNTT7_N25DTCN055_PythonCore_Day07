from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Library Book Management")

# 1. PYDANTIC MODEL

class Book(BaseModel):
    id: int
    ten_sach: str
    tac_gia: str
    nam_xuat_ban: int
    so_luong: int

# 2. DATABASE TẠM TRÊN RAM

danh_sach_sach = [
    {
        "id": 1,
        "ten_sach": "Nhà Giả Kim",
        "tac_gia": "Paulo Coelho",
        "nam_xuat_ban": 1988,
        "so_luong": 5
    },
    {
        "id": 2,
        "ten_sach": "Dế Mèn Phiêu Lưu Ký",
        "tac_gia": "Tô Hoài",
        "nam_xuat_ban": 1941,
        "so_luong": 10
    },
    {
        "id": 3,
        "ten_sach": "Tuổi Trẻ Đáng Giá Bao Nhiêu",
        "tac_gia": "Rosie Nguyễn",
        "nam_xuat_ban": 2016,
        "so_luong": 7
    }
]

# 3. POST - THÊM SÁCH

@app.post("/api/v1/books", response_model=Book)
def create_book(book: Book):

    danh_sach_sach.append(book.model_dump())

    return book

# 4. GET - LẤY TẤT CẢ SÁCH

@app.get("/api/v1/books", response_model=list[Book])
def get_all_books():

    return danh_sach_sach

# 5. GET - LẤY SÁCH THEO ID

@app.get("/api/v1/books/{book_id}", response_model=Book)
def get_book(book_id: int):

    for book in danh_sach_sach:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail=f"Không tìm thấy sách với id: {book_id}"
    )

# 6. PUT - CẬP NHẬT SÁCH

@app.put("/api/v1/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: Book):

    for index, book in enumerate(danh_sach_sach):

        if book["id"] == book_id:

            danh_sach_sach[index] = book_update.model_dump()

            return danh_sach_sach[index]

    raise HTTPException(
        status_code=404,
        detail=f"Không tìm thấy sách với id: {book_id}"
    )

# 7. DELETE - XÓA SÁCH

@app.delete("/api/v1/books/{book_id}", response_model=Book)
def delete_book(book_id: int):

    for index, book in enumerate(danh_sach_sach):

        if book["id"] == book_id:

            deleted_book = danh_sach_sach.pop(index)

            return deleted_book

    raise HTTPException(
        status_code=404,
        detail=f"Không tìm thấy sách với id: {book_id}"
    )