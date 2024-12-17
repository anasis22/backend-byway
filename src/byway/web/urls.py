from django.urls import path
from .views import register_view, login_view, logout_view , TopCategoriesLsit_view , TopCoursesList_view , TopInstructorsList_view , CustomerFeedbackList_view , buy_course , purchased_courses

app_name = "web"

urlpatterns = [
    path("api/top-categories/", TopCategoriesLsit_view.as_view(), name="top-categories"),
    path("api/top-courses/", TopCoursesList_view.as_view(), name="top-courses"),
    path("api/top-instructors/", TopInstructorsList_view.as_view(), name="top-instructors"),
    path("api/customer-feedbacks/", CustomerFeedbackList_view.as_view(), name="customer-feedbacks"),
    path("api/register/", register_view, name="register"),
    path("api/login/", login_view, name="login"),
    path("api/logout/", logout_view, name="logout"),
    path('api/buy-course/<int:course_id>/', buy_course, name='buy_course'),
    path('api/purchased-courses/', purchased_courses, name='purchased_courses'),
]
