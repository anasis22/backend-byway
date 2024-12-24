from django.db import models
from django.contrib.auth.models import User

# Top Categories
class Top_Categories(models.Model):
    icon = models.ImageField(upload_to="categories/category_icons")
    name = models.CharField(max_length=500)
    course_counts = models.CharField(max_length=500)

    def __str__(self):
        return self.name

# Top Courses
class Top_Courses(models.Model):
    COURSE_LEVELS = [("B","Beginner"), ("I","Intermediate"), ("A","Advanced")]
    thumbnail = models.ImageField(upload_to="courses/course_thumbnails")
    title = models.CharField(max_length=500)
    course_description = models.TextField()
    author = models.CharField(max_length=500)
    rating_star = models.ImageField(upload_to="courses/course_rating_stars")
    rating_single_star = models.ImageField(upload_to="courses/course_rating_stars")
    rating_five_out_of = models.CharField(max_length=500)
    rating_text = models.CharField(max_length=500)
    course_hours = models.CharField(max_length=500)
    lecture_counts = models.CharField(max_length=500)
    course_level = models.CharField(max_length=50, choices=COURSE_LEVELS)
    author_icon = models.ImageField(upload_to="courses/course_authors")
    course_languages = models.CharField(max_length=500)
    course_detail_thumbnail = models.ImageField(upload_to="courses/course_detail_thumbnails")
    price = models.CharField(max_length=500)
    strike_out_price = models.CharField(max_length=500)

    def __str__(self):
        return self.title

# Top Instructors
class Top_Instructors(models.Model):
    instructor_image = models.ImageField(upload_to="instructors/instructor_images")
    name = models.CharField(max_length=500)
    course_name = models.CharField(max_length=500)
    rating_star = models.ImageField(upload_to="instructors/rating_stars")
    rating_text = models.CharField(max_length=500)
    students_enrolled_count = models.CharField(max_length=500)

    def __str__(self):
        return self.name

# Customer Feedback
class Customer_Feedback(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="customer_feedbacks/customer_images")
    name = models.CharField(max_length=500)
    profession = models.CharField(max_length=500)

    def __str__(self):
        return f"Feedback from {self.name}"

# Purchase
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchases")
    course = models.ForeignKey(Top_Courses, on_delete=models.CASCADE, related_name="purchases")
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
