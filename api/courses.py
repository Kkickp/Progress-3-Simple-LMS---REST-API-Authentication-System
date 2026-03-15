from ninja import Router
from courses.models import Course
from .schemas import CourseCreateSchema

router = Router()


@router.get("")
def list_courses(request):

    courses = Course.objects.all()

    return [
        {
            "id": c.id,
            "title": c.title,
            "instructor": c.instructor.username
        }
        for c in courses
    ]


@router.get("/{course_id}")
def course_detail(request, course_id: int):

    course = Course.objects.get(id=course_id)

    return {
        "title": course.title,
        "description": course.description
    }


@router.post("")
def create_course(request, payload: CourseCreateSchema):

    course = Course.objects.create(
        title=payload.title,
        description=payload.description,
        category_id=payload.category_id,
        instructor=request.user
    )

    return {"id": course.id}