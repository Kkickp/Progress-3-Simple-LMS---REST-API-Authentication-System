from ninja import Schema


class UserRegisterSchema(Schema):
    username: str
    password: str
    role: str


class LoginSchema(Schema):
    username: str
    password: str


class CourseCreateSchema(Schema):
    title: str
    description: str
    category_id: int


class EnrollmentSchema(Schema):
    course_id: int