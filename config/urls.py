from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from api.auth import router as auth_router
from api.courses import router as course_router
from api.enrollments import router as enrollment_router

api = NinjaAPI()

api.add_router("/auth/", auth_router)
api.add_router("/courses/", course_router)
api.add_router("/enrollments/", enrollment_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]