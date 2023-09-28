from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('index')


def index(request):
    db = {
        'Pers': Personel.objects.all(),
        'Partenaire': Partenaire.objects.all(),
        'service': Service.objects.all(),
        'Project': Project.objects.all(),
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, phone=phone, email=email,
                          subject=subject, message=message)
        contact.save()
        send_mail(
            subject,
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False
        )

    if request.user.is_authenticated:

        username = request.user.username
        db['username'] = username

    return render(request, 'index.html', db)


@login_required
def project_detail(request, project_id):
    project1 = get_object_or_404(Project, id=project_id)
    context = {'project1': project1}
    if request.user.is_authenticated:

        username = request.user.username
        context['username'] = username
    return render(request, 'project_detail.html', context)


def demande_project(request):
    context = {}
    if request.method == 'POST':

        client_name = request.POST.get('client-name')
        number = request.POST.get('client-number')
        libelle = request.POST.get('libelle')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        client_mail = request.POST.get('client-mail')

        project = Project(client_name=client_name, number_client=number,
                          libelle=libelle, image=image, description=description,
                          client_mail=client_mail)
        project.save()

        return redirect('project_detail', project_id=project.id)

    if request.user.is_authenticated:
        # if connecte
        username = request.user.username
        context['username'] = username
    return render(request, 'demande_project.html', context)


def login_registration(request):
    if request.method == 'POST':
        if 'signup-form' in request.POST:
            fullname = request.POST['fullname']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(fullname, email, password)
            user.first_name = fullname
            user.save()
            login(request, user)
            return redirect('index')
        elif 'login-form' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error_message = 'Invalid email or password'
                return render(request, 'login.html', {'error_message': error_message})
        else:
            error_msg = 'Invalid form submission'
            return render(request, 'login.html', {'error_msg': error_msg})
    else:
        return render(request, 'login.html')


def my_projects(request):
    projects = Project.objects.filter(client_name=request.user.username)
    context = {'projects': projects}
    if request.user.is_authenticated:
        # if the user is authenticated, pass their username to the template
        username = request.user.username
        context['username'] = username
    return render(request, 'my_projects.html', context)
