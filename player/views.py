from django.shortcuts import render, get_object_or_404
from courses.models import Course
from course_manager.models import Module, SubModule

# Create your views here.

def player_view(request, course_id, module_id, submodule_id):
    course = get_object_or_404(Course, id=course_id)
    module = get_object_or_404(Module, id=module_id, course=course)
    submodule = get_object_or_404(SubModule, id=submodule_id, module=module)

    context = {
        'course': course,
        'module': module,
        'submodule': submodule,
    }
    
    return render(request, 'player/player_view.html', context)