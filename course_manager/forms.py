from django import forms
from courses.models import Course
from .models import Module, SubModule

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'  # Include all fields from the Course model
        exclude = ['created_at', 'updated_at']

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['course', 'title', 'video_url', 'notes', 'source_code_url', 'additional_resources']

class SubModuleForm(forms.ModelForm):
    class Meta:
        model = SubModule
        fields = ['module', 'title', 'video_url', 'notes', 'source_code_url',]