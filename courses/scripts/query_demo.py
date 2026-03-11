from courses.models import Course
from django.db import connection


def show_queries():

    print("Total Queries:", len(connection.queries))


def n_plus_one_problem():

    courses = Course.objects.all()

    for course in courses:
        print(course.instructor.username)

    show_queries()


def optimized_query():

    courses = Course.objects.select_related('instructor')

    for course in courses:
        print(course.instructor.username)

    show_queries()