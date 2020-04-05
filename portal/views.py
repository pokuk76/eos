from django.shortcuts import render
from django.http import Http404, HttpResponse, FileResponse, HttpResponseRedirect

from django.urls import reverse_lazy
from django.views import generic

#from django.contrib.auth import authenticate, login

from .models import CustomUser, Department
from .forms import CustomUserCreationForm

from .forms import PersonalDetailsForm

def nhis_form(request):
    """
    The view for the HR Pocket Guide (use this generally for pdf documents)
    """
    with open('portal/nhis_form.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=nhis_form.pdf'
        return response


def pocket_guide(request):
    """
    The view for the HR Pocket Guide (use this generally for pdf documents)
    """
    with open('portal/pocket_guide.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pocket_guide.pdf'
        return response

def details(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonalDetailsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            """
            TODO: process the data in form.cleaned_data as required
            """
            # redirect to a new URL:
            return HttpResponseRedirect('../forms/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonalDetailsForm()

    return render(request, 'portal/details.html', {'form': form})

def personal_details(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonalDetailsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            """
            TODO:process the data in form.cleaned_data as required
            """
            # redirect to a new URL:
            return HttpResponseRedirect('../forms/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonalDetailsForm()

    return render(request, 'portal/personal_details.html', {'form': form})

class EmployeesView(generic.ListView):
    template_name = 'portal/employees.html'
    context_object_name = 'is_video_list'

    def get_queryset(self):
        """
        """
        dept = Department.objects.get(dept_name="Information Systems")
        return dept.video_set.all()

class FormsView(generic.ListView):
    template_name = 'portal/forms.html'
    context_object_name = 'is_video_list'

    def get_queryset(self):
        """
        """
        dept = Department.objects.get(dept_name="Information Systems")
        return dept.video_set.all()

class TodoView(generic.ListView):
    template_name = 'portal/todo.html'
    context_object_name = 'is_video_list'

    def get_queryset(self):
        """
        """
        dept = Department.objects.get(dept_name="Information Systems")
        return dept.video_set.all()


class TutorialsView(generic.ListView):
    template_name = 'portal/tutorials.html'
    context_object_name = 'user_video_list'

    def get_queryset(self):
        """
        """
        user = self.request.user
        dept = user.dept
        return dept.video_set.all()

class SignUpView(generic.CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'portal/signup.html'

class ISView(generic.ListView):
    template_name = 'portal/is.html'
    context_object_name = 'is_video_list'

    def get_queryset(self):
        """
        """
        dept = Department.objects.get(dept_name="Information Systems")
        return dept.video_set.all()

class HRView(generic.ListView):
    template_name = 'portal/hr.html'
    context_object_name = 'hr_video_list'

    def get_queryset(self):
        """
        """
        dept = Department.objects.get(dept_name="Human Resources")
        return dept.video_set.all()
"""
TODO: Test login redirect on incorrect Information

def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            url = reverse('pilot:home')
            return HttpResponseRedirect(url)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

    ORRR?

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        url = reverse('portal:tutorials')
        return HttpResponseRedirect(url)
    else:
        # Return an 'invalid login' error message.

    #return render(request, 'portal/login.html')
"""
def login(request):

    return render(request, 'portal/login.html')

def home(request):

    return render(request, 'portal/home.html')
