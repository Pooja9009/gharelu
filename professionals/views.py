from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentications.auth import professional_only
from authentications.forms import ProfileForm
import os
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from professionals.forms import ServiceForm
from professionals.models import Service

# Create your views here.

@login_required
@professional_only
def professionalDashboard(request):
    service = Service.objects.all()



    totalService =service.count()

    context = {
        'totalService': totalService,
        'activate_professionalshome': 'active bg-primary',
    }
    return render(request, 'professionals/professionalDashboard.html', context)



@login_required
@professional_only
def professionalProfile(request):
    profile= request.user.profile # Getting currently logged in user data
    if request.method == 'POST':
        userdata = ProfileForm(request.POST, request.FILES, instance=profile) 
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Profile data updated successfully!')
            return redirect('/professionals/professionalprofile')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong!")
            context={'profileForm':userdata}
            return render(request, 'professionals/professionalProfile.html',context)

    context = {'profileForm':ProfileForm(instance=profile)}
    return render(request, 'professionals/professionalProfile.html', context)


@login_required
@professional_only
def professionalUpdateProfile(request):
    profile= request.user.profile # Getting currently logged in user data

    if request.method == 'POST':
        # Delete image from uploads static after changing new image
        # os.remove(profile.profile_pic.path)

        userdata = ProfileForm(request.POST,request.FILES,instance=profile) 
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Profile data updated successfully!')
            return redirect('/professionals/professionalupdateprofile')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong!")
            context={'profileUpdateForm':userdata}
            return render(request, 'professionals/professionalUpdateProfile.html',context)

    context = {'profileUpdateForm':ProfileForm(instance=profile)}
    return render(request, 'professionals/professionalUpdateProfile.html', context)


@login_required
@professional_only
def service(request):
    services = Service.objects.all().order_by('-id')
    context={
        'services':services,
        'activate_services': 'active bg-primary'
    }
    return render(request, 'professionals/service.html', context)



@login_required
@professional_only
def bookings(request):
    context = {
        'activate_bookings': 'active bg-primary'
    }
    return render(request, 'professionals/bookings.html', context)




@login_required
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "Password changed successfully")
            return redirect('/professionals/change_password')
        else:
            messages.add_message(request, messages.ERROR, "Please check the fields")
            return render(request, 'professionals/changePassword.html' ,{'user_password_change_form':form})
    context = {
        'user_password_change_form': PasswordChangeForm(request.user),

    }
    return render(request, 'professionals/changePassword.html', context)


@login_required
@professional_only
def service_form(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Service added Successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Service!')
            return render(request, 'professionals/service_form.html', {'form_service': form})

    context = {
        'form_service': ServiceForm,
        'activate_service': 'active',
    }
    return render(request, 'professionals/service_form.html', context)

@login_required
@professional_only
def show_service(request):
    services = Service.objects.all().order_by('-id')
    context={
        'services':services,
    }
    return render(request, 'professionals/show_service.html', context)



@login_required
@professional_only
def service_update_form(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Service Updated Successfully')
            return redirect("/professionals/services")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update Service!')
            return render(request, 'professionals/service_update_form.html', {'form_service': form})

    context = {
        'form_service': ServiceForm(instance=service),
        'activate_service': 'active',
    }
    return render(request, 'professionals/service_update_form.html', context)

@login_required
@professional_only
def delete_service(request, service_id):
    service = Service.objects.get(id=service_id)
    os.remove(service.service_photo.path)
    service.delete()
    messages.add_message(request, messages.SUCCESS, 'Service deleted successfully!')
    return redirect('/professionals/services')