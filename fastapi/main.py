from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define a list to store student information (mock database)
students = []

# Define Student model
class Student(BaseModel):
    name: str
    age: int
    grade: str

# Route for getting all students (GET request)
@app.get('/students')
def get_students():
    return students

# Route for adding a new student (POST request)
@app.post('/students')
def add_student(student: Student):
    students.append(student)
    return student

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", po)
