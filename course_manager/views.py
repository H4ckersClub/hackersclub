from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from courses.models import Course
from .models import Module, SubModule
from .forms import CourseForm, ModuleForm, SubModuleForm


# Create your views here.

@staff_member_required
def course_list_view(request):
    courses = Course.objects.all()
    return render(request, 'course_manager/course_list.html', {'courses': courses})

@staff_member_required
def course_create_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_manager:course_list')
    else:
        form = CourseForm()
    return render(request, 'course_manager/course_form.html', {'form': form})

@staff_member_required
def course_edit_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_manager:course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_manager/course_form.html', {'form': form, 'course': course})

@staff_member_required
def course_modules(request, pk):
    course = get_object_or_404(Course, pk=pk)
    modules = Module.objects.filter(course=course)
    return render(request, 'course_manager/course_modules.html', {'course': course, 'modules': modules})

@staff_member_required
def module_create(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = form.save(commit=False)
            module.course = course
            module.save()
            return redirect('course_manager:course_detail', pk=course.id)
    else:
        form = ModuleForm(initial={'course': course})
    return render(request, 'course_manager/module_form.html', {'form': form, 'course': course})

@staff_member_required
def module_edit(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            return redirect('course_manager:course_detail', pk=module.course.id)
    else:
        form = ModuleForm(instance=module)
    return render(request, 'course_manager/module_form.html', {'form': form, 'module': module})

@staff_member_required
def submodule_create(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if request.method == 'POST':
        form = SubModuleForm(request.POST)
        if form.is_valid():
            submodule = form.save(commit=False)
            submodule.module = module
            submodule.save()
            return redirect('course_manager:course_detail', pk=module.course.id)
    else:
        form = SubModuleForm(initial={'module': module})
    return render(request, 'course_manager/submodule_form.html', {'form': form, 'module': module})

@staff_member_required
def submodule_edit(request, submodule_id):
    submodule = get_object_or_404(SubModule, id=submodule_id)
    if request.method == 'POST':
        form = SubModuleForm(request.POST, instance=submodule)
        if form.is_valid():
            form.save()
            return redirect('course_manager:course_detail', pk=submodule.module.course.id)
    else:
        form = SubModuleForm(instance=submodule)
    return render(request, 'course_manager/submodule_form.html', {'form': form, 'submodule': submodule})

@staff_member_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    modules = Module.objects.filter(course=course)
    context = {
        'course': course,
        'modules': modules
    }
    return render(request, 'course_manager/course_detail.html', context)

@staff_member_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_manager:course_list')
    return render(request, 'course_manager/course_confirm_delete.html', {'course': course})

@staff_member_required
def module_delete(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if request.method == 'POST':
        module.delete()
        return redirect('course_manager:course_detail', pk=module.course.id)
    return render(request, 'course_manager/module_confirm_delete.html', {'module': module})

@staff_member_required
def submodule_delete(request, submodule_id):
    submodule = get_object_or_404(SubModule, id=submodule_id)
    if request.method == 'POST':
        submodule.delete()
        return redirect('course_manager:course_detail', pk=submodule.module.course.id)
    return render(request, 'course_manager/submodule_confirm_delete.html', {'submodule': submodule})

@staff_member_required
def module_list_view(request):
    from .models import Module
    from courses.models import Course

    course_id = request.GET.get('course')
    courses = Course.objects.all()
    modules = Module.objects.all()
    if course_id:
        modules = modules.filter(course_id=course_id)
    return render(request, 'course_manager/module_list.html', {
        'modules': modules,
        'courses': courses,
        'selected_course_id': course_id,
    })

@staff_member_required
def submodule_list_view(request):
    from .models import SubModule, Module
    module_id = request.GET.get('module')
    modules = Module.objects.all()
    submodules = SubModule.objects.all()
    if module_id:
        submodules = submodules.filter(module_id=module_id)
    return render(request, 'course_manager/submodule_list.html', {
        'submodules': submodules,
        'modules': modules,
        'selected_module_id': module_id,
    })