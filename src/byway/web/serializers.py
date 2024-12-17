from rest_framework import serializers
from .models import Top_Categories , Top_Courses , Top_Instructors , Customer_Feedback
from .forms import RegisterForm
from django.contrib.auth.models import User
        
# serializers for Top Categories
class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Top_Categories
        fields = '__all__'
        
# serializers for Top Courses
class CoursesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Top_Courses
        fields = "__all__"
        
# serializers for Top Instructors
class InstructorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Top_Instructors
        fields = "__all__"
        
# serializers for Customer Feedbacks
class FeedbacksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer_Feedback
        fields = "__all__"
        