from ninja import Router
from courses.models import Enrollment
from .schemas import EnrollmentSchema

router = Router()


@router.post("")
def enroll_course(request, payload: EnrollmentSchema):

    enrollment = Enrollment.objects.create(
        student=request.user,
        course_id=payload.course_id
    )

    return {"id": enrollment.id}


@router.get("/my-courses")
def my_courses(request):

    enrollments = Enrollment.objects.filter(
        student=request.user
    )

    return [
        {
            "course": e.course.title
        }
        for e in enrollments
    ]