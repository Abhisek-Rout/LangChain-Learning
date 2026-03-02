from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description="A decimal value representing the cgpa of the student")

# By using Pydantic we can perform data type validation as well
# In case of str for the name field if we provide the integer then it will give an error
# It also gives type coercion, e.g if u provide age as "32" then it will convert to 32 interger
# Here u can also set constraint to specific fields and give default value as well

new_student = {"name": "Abhisek Rout", "age": "32", "email": "abc@gmail.com"}

student = Student(**new_student)

print(type(student))
print(student.name)
print(student.age)
print(student.email)
print(student.cgpa)

student_dict = dict(student)
print(student_dict)

student_json = student.model_dump_json()
print(student_json)