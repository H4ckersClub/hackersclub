from django.shortcuts import render, redirect
from .models import Course
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# Sample courses data 
COURSES = [
    {
        'id': 1,
        'title': 'Cybersecurity Fundamentals',
        'short_description': 'Learn the basics of cybersecurity.',
        'description': 'A comprehensive introduction to cybersecurity concepts, threats, and defenses.',
        'price': 999,
        'image': 'https://via.placeholder.com/400x200?text=Cybersecurity',
    },
    {
        'id': 2,
        'title': 'Computer Networks',
        'short_description': 'Understand how computer networks work.',
        'description': 'Detailed course on networking, protocols, and architectures.',
        'price': 799,
        'image': 'https://via.placeholder.com/400x200?text=Networks',
    },
    {
        'id': 3,
        'title': 'Python Programming',
        'short_description': 'Master Python programming from basics to advanced.',
        'description': 'Complete Python course covering basics, web development, data science, and more.',
        'price': 1299,
        'image': 'https://via.placeholder.com/400x200?text=Python',
    },
]


def home(request):
    # Try to fetch courses from the database
    try:    
        courses = Course.objects.all()
        if courses.exists():
            # If courses exist in the database, use them
            courses = [
                {
                    'id': course.id,
                    'title': course.title,
                    'short_description': course.short_description,
                    'description': course.description,
                    'price': course.price,
                    'image_url': course.image_url or 'https://via.placeholder.com/400x200?text=Course+Image',
                }
                for course in courses
            ]
        else:
            # If no courses in the database, use the static list
            courses = COURSES
    except Course.DoesNotExist:
        # If Course model does not exist, use the static list
        courses = COURSES
    return render(request, 'courses/home.html', {'courses': courses})

def course_detail(request, course_id):
    # Try to fetch the course from the database
    try:
        course = Course.objects.get(id=course_id)
        course = {
            'id': course.id,
            'title': course.title,
            'short_description': course.short_description,
            'description': course.description,
            'price': course.price,
            'image_url': course.image_url or 'https://via.placeholder.com/400x200?text=Course+Image',
        }
    except Course.DoesNotExist:
        # Fallback to dummy data
        course = next((c for c in COURSES if c['id'] == course_id), None)
    if not course:
        # If the course is not found in both the database and dummy data
        messages.error(request, "Course not found.")
        return redirect('home')
    
    # Check if user already owns this course
    # create this after creating orders Model in database
    # user_owns_course = False
    # if request.user.is_authenticated:
    #     user_owns_course = Order.objects.filter(
    #         user=request.user,
    #         course_reference=course_id,
    #         payment_status='paid' # Assuming 'paid' is the status for completed orders
    #     ).exists()

    # Render the course detail page with the course data
    context = {
            'course': course,
            # 'user_owns_course': user_owns_course
        }
    
    return render(request, 'courses/course_detail.html', context)
