from django.contrib import admin
from .models import Top_Categories , Top_Courses , Top_Instructors , Customer_Feedback , Purchase
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

    
# Users
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    
# Top Categories
@admin.register(Top_Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name"]
    
# Top Courses
@admin.register(Top_Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ["title" , "author"]
    
# Top Instructors
@admin.register(Top_Instructors)
class InstructorsAdmin(admin.ModelAdmin):
    list_display = ["name" , "course_name"]
    

# Customer Feedbacks
@admin.register(Customer_Feedback)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ["name" , "profession"]
    

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_course_name', 'purchased_at')  
    list_filter = ('user', 'course')  
    search_fields = ('user__username', 'course__title') 
    
    def get_course_name(self, obj):
        return obj.course.title 
    get_course_name.admin_order_field = 'course__title' 
    get_course_name.short_description = 'Course Name' 

# Register your models
admin.site.register(Purchase, PurchaseAdmin)
