from django.db import connection
from courses.models import Course


def show_queries():

    connection.queries_log.clear()

    courses = Course.objects.all()

    for c in courses:
        print(c.instructor.username)

    print("Query count:", len(connection.queries))

def optimized_queries():

    connection.queries_log.clear()

    courses = Course.objects.select_related('instructor')

    for c in courses:
        print(c.instructor.username)

    print("Query count:", len(connection.queries))