from django.shortcuts import render, get_object_or_404
from courses.models import Course
from course_manager.models import Module, SubModule

# Create your views here.

# def player_view(request, course_id, module_id, submodule_id):
#     course = get_object_or_404(Course, id=course_id)
#     module = get_object_or_404(Module, id=module_id, course=course)
#     submodule = get_object_or_404(SubModule, id=submodule_id, module=module)

#     context = {
#         'course': course,
#         'module': module,
#         'submodule': submodule,
#     }
    
#     return render(request, 'player/player_view.html', context)

def player_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    module_id = request.GET.get('module')
    submodule_id = request.GET.get('submodule')

    selected_module = None
    selected_submodule = None

    if module_id:
        try:
            selected_module = get_object_or_404(Module, id=module_id, course=course)
            if submodule_id:
                selected_submodule = get_object_or_404(SubModule, id=submodule_id, module=selected_module)
        except (ValueError, Module.DoesNotExist, SubModule.DoesNotExist):
            pass

    modules = course.modules.all()

    context = {
        'course': course,
        'modules': modules,
        'selected_module': selected_module,
        'selected_submodule': selected_submodule,
    }
    return render(request, 'player/player.html', context)
