from ninja.errors import HttpError


def is_instructor(user):

    if user.role != "instructor":
        raise HttpError(403, "Instructor only")


def is_admin(user):

    if user.role != "admin":
        raise HttpError(403, "Admin only")


def is_student(user):

    if user.role != "student":
        raise HttpError(403, "Student only")