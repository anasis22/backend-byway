from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    Top_Categories,
    Top_Courses,
    Top_Instructors,
    Customer_Feedback,
    Purchase,
)
from .serializers import (
    CategoriesSerializers,
    CoursesSerializers,
    InstructorsSerializers,
    FeedbacksSerializers,
)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm
import json


# Top Categories View
class TopCategoriesLsit_view(APIView):
    def get(self, request):
        categories = Top_Categories.objects.all()
        serializer = CategoriesSerializers(categories, many=True)
        return Response(serializer.data)


# Top Courses View
class TopCoursesList_view(APIView):
    def get(self, request):
        courses = Top_Courses.objects.all()
        serializer = CoursesSerializers(courses, many=True)
        return Response(serializer.data)


# Top Instructors View
class TopInstructorsList_view(APIView):
    def get(self, request):
        instructor = Top_Instructors.objects.all()
        serializer = InstructorsSerializers(instructor, many=True)
        return Response(serializer.data)


# Customer Feedback View
class CustomerFeedbackList_view(APIView):
    def get(self, request):
        feedback = Customer_Feedback.objects.all()
        serializer = FeedbacksSerializers(feedback, many=True)
        return Response(serializer.data)


# Sigup View
@csrf_exempt
def register_view(req):
    if req.method == "POST":
        try:
            # Parse the JSON body of the request
            data = json.loads(req.body)
            form = RegisterForm(data)

            if form.is_valid():
                username = form.cleaned_data.get("username")
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")

                # Create user if no errors
                User.objects.create_user(
                    username=username, email=email, password=password
                )

                return JsonResponse(
                    {"message": "User registered successfully"}, status=201
                )
            else:
                # Return form errors if invalid
                return JsonResponse({"error": form.errors}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    # If not a POST request, return an error response
    return JsonResponse({"error": "Invalid request method"}, status=405)


# Login View
@csrf_exempt
def login_view(req):
    if req.method == "POST":
        try:
            # Parse the JSON body of the request
            data = json.loads(req.body)
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return JsonResponse(
                    {"message": "Username and password are required"}, status=400
                )

            # Authenticate the user
            user = authenticate(req, username=username, password=password)

            if user is not None:
                login(req, user)
                return JsonResponse({"message": "Login successful"}, status=200)
            else:
                return JsonResponse({"message": "Invalid credentials"}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON format"}, status=400)

    return JsonResponse({"message": "Only POST requests are allowed"}, status=405)


# Logout view
@csrf_exempt
def logout_view(req):
    if req.method == "POST":
        logout(req)
        return JsonResponse({"message": "Logout successful"}, status=200)
    return JsonResponse({"message": "Only POST requests are allowed"}, status=405)


# To Buy Course view
@login_required
def buy_course(request, course_id):
    try:
        # Find the course by ID
        course = Top_Courses.objects.get(id=course_id)

        # Check if the user has already purchased the course
        if Purchase.objects.filter(user=request.user, course=course).exists():
            return JsonResponse({"message": "You already own this course"}, status=400)

        # Create a purchase record
        Purchase.objects.create(user=request.user, course=course)
        return JsonResponse({"message": "Course purchased successfully!"}, status=200)
    except Top_Courses.DoesNotExist:
        return JsonResponse({"message": "Course not found!"}, status=404)


# Purchased Course view
@login_required
def purchased_courses(request):
    purchases = Purchase.objects.filter(user=request.user).select_related("course")
    data = [
        {
            "course_id": p.course.id,
            "title": p.course.title,
            "course_description": p.course.course_description,
            "course_detail_thumbnail": (
                p.course.course_detail_thumbnail.url
                if p.course.course_detail_thumbnail
                else ""
            ),
            "price": p.course.price
        }
        for p in purchases
    ]
    return JsonResponse({"purchased_courses": data}, status=200)
