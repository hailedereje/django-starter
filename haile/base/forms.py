from django.forms import ModelForm
from .models import Student ,Room

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'