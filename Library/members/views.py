from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
import time

# Create your views here.

def get_members(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        
        queryset = Member.objects.filter(
            Q(email=email)
        )

        if queryset.count() == 0:
            member = Member(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date_of_birth=date_of_birth,
                debt=0
            )
            member.save()

        context = { 'members': Member.objects.all() }
        return render(request, 'members/member_list.html', context)

    name = request.GET.get('name', '')

    queryset = Member.objects.filter(
        Q(first_name__icontains=name) |
        Q(last_name__icontains=name)
    )

    context = { 'members': queryset }
    return render(request, 'members/member_list.html', context)

def delete_member(request, id):
    queryset = Member.objects.get(id=id)
    queryset.delete()
    time.sleep(1)
    return redirect('/members/')

def update_member(request, id):
    if request.method == 'POST':
        queryset = Member.objects.get(id=id)
        data = request.POST
        queryset.first_name = data.get('first_name')
        queryset.last_name = data.get('last_name')
        queryset.email = data.get('email')
        queryset.date_of_birth = data.get('date_of_birth')
        queryset.save()
        return redirect('/members/')

    queryset = Member.objects.get(id=id)
    context = { 'member': queryset }
    return render(request, 'members/update_member.html', context)