from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Vatsal", "age": 22, "course": "Data Science"},
    {"id": 2, "name": "Rahul", "age": 21, "course": "BCA"},
    {"id": 3, "name": "Anjali", "age": 23, "course": "MCA"},
    {"id": 4, "name": "Priya", "age": 21, "course": "Data Science"},
]


@app.get("/")
def hello():
    return "Hello World"


# Filters
@app.get("/students")
def all_students(course: str = None, age: int = None):
    result = students
    if course:
        result = [s for s in result if s["course"] == course]

    if age:
        result = [s for s in result if s["age"] == age]

    if result:
        return {"Students": result}

    return {"Message": "No matching Students"}


@app.get("/students/{id}")
def student(id: int):
    for s in students:
        if s["id"] == id:
            return {"Student": s}

    return {"Message": "Student not found"}
