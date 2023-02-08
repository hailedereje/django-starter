from django.shortcuts import redirect, render
from . import models , forms
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here. 
def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home ')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            print('not valid user')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print('invaild user')
    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    studentActivity = models.Room.objects.filter(
        Q(topic__name__icontains = q)|
        Q(name__icontains = q)
        
    )
    student_list = models.Topic.objects.all()
   
    room_count = studentActivity.count()
    
    context = {'studentActivity':student_list,'student_list':studentActivity,'room':room_count}
    return render(request,'home.html',context)


@login_required(login_url='login')
def detail(request,pk):
    student = models.Room.objects.get(id = pk)
    context = {'student':student}
    return render(request,'detail.html',context)


@login_required(login_url='login')
def create_student(request):
    form = forms.RoomForm()
    if request.method == 'POST':
        form = forms.RoomForm(request.POST)
        form.save()
        return redirect('home') 

    context = {'form':form}
    return render(request,'create_student.html',context)


@login_required(login_url='login')
def update_student(request,pk):
    student = models.Room.objects.get(id = pk)
    form = forms.RoomForm(instance=student)
    if request.method == 'POST':
        form = forms.RoomForm(request.POST,instance=student)
        form.save()
        return redirect('home') 
    context = {'form':form}
    return render(request,'create_student.html',context)
 


@login_required(login_url='login')   
def delete_student(request,pk):
    student = models.Room.objects.get(id = pk)
    student.delete()
    return redirect('home')

