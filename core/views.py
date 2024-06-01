# core/views.py

import csv
from django.shortcuts import render, redirect
from .form import UploadFileForm, QueryForm
from .models import Company
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload_file')  # Redirect to the upload file page after login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if username and password and email:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('upload_file') 
        else:
            messages.error(request, 'Please fill out all fields')
    return render(request, 'signup.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            # Process the uploaded file and save data into Company model
            with open(fs.path(uploaded_file.name), 'r') as file:
                reader = csv.DictReader(file)
                print(reader)
                for row in reader:
                    Company.objects.create(
                        company_id=row.get(''),
                        name=row.get('name', ''),
                        domain=row.get('domain', ''),
                        year_founded=int(row.get('year founded', 0)),
                        industry=row.get('industry', ''),
                        size_range=row.get('size range', ''),
                        locality=row.get('locality', ''),
                        country=row.get('country', ''),
                        linkedin_url=row.get('linkedin url', ''),
                        current_employee_estimate=int(row.get('current employee estimate', 0)),
                        total_employee_estimate=int(row.get('total employee estimate', 0))
                    )
            return redirect('upload_file')  # Redirect to the same page after processing
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def query_builder(request):
    results = None

    if request.method == 'POST':
        form = QueryForm(request.POST)
       
        if form.is_valid():
            keyword = form.cleaned_data.get('keyword')
            industry = form.cleaned_data.get('industry')
            year_founded = form.cleaned_data.get('year_founded')
            country = form.cleaned_data.get('country')
            employees_from = form.cleaned_data.get('employees_from')
            employees_to = form.cleaned_data.get('employees_to')


            query = Company.objects.all()
            if keyword:
                query = query.filter(name__icontains=keyword)
            if industry:
                query = query.filter(industry=industry)
            if year_founded:
                query = query.filter(year_founded=year_founded)
            if country:
                query = query.filter(country=country)
            if employees_from:
                query = User.objects.filter(username=employees_from)
            if employees_to:
                query = User.objects.filter(username=employees_from)

            results = query.count()
            print(results)
    else:
        form = QueryForm()
    
    return render(request, 'query.html', {'form': form, 'results': results})

@api_view(['GET'])
def query_count(request):
    q = Q()
    if 'name' in request.GET:
        q &= Q(name__icontains=request.GET['name'])
    count = Company.objects.filter(q).count()
    return Response({'count': count})


def user_list(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        if username and email:
            User.objects.create(username=username, email=email)
            messages.success(request, 'New user added')
            return redirect('user_list')

    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    messages.success(request, 'User deleted')
    return redirect('user_list')