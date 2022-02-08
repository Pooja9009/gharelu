from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from authentications.auth import customer_only
from authentications.forms import ProfileForm
from django.contrib import messages
from homepage.models import Order
from professionals.models import Service
from homepage.filters import ServiceFilter

# Create your views here.

@login_required
@customer_only
def customerDashboard(request):
    services = Service.objects.all().order_by('-id')
    service_filter = ServiceFilter(request.GET, queryset=services)

    services_final = service_filter.qs 

    context = {'services':services_final , 'service_filter':service_filter}
    return render(request, 'customers/customerDashboard.html',context)


@login_required
@customer_only
def customerProfile(request):
    profile= request.user.profile # Getting currently logged in user data
    if request.method == 'POST':
        userdata = ProfileForm(request.POST, request.FILES, instance=profile) 
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Profile data updated successfully!')
            return redirect('/customers/customerprofile')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong!")
            context={'profileForm':userdata}
            return render(request, '/customers/customerProfile.html',context)

    context = {'profileForm':ProfileForm(instance=profile)}
    return render(request, 'customers/customerProfile.html', context)



@login_required
@customer_only
def customerUpdateProfile(request):
    profile= request.user.profile # Getting currently logged in user data
    print(profile)
    if request.method == 'POST':
        print('hello')
        # Delete image from uploads static after changing new image
        # os.remove(profile.profile_pic.path)

        userdata = ProfileForm(request.POST,request.FILES,instance=profile) 
        print(userdata)
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Profile data updated successfully!')
            return redirect('/customers/customerupdateprofile')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong!")
            context={'profileUpdateForm':userdata}
            return render(request, 'customers/customerUpdateProfile.html',context)

    context = {'profileUpdateForm':ProfileForm(instance=profile)}
    return render(request, 'customers/customerUpdateProfile.html', context)

@login_required
@customer_only
def myBookings(request):
    user = request.user
    servicePending = Order.objects.filter(user=user, status="Pending").order_by('-id')
    serviceApproved = Order.objects.filter(user=user, status="Approved").order_by('-id')
    serviceDeclined = Order.objects.filter(user=user, status="Declined").order_by('-id')
    context = {
        'servicePending': servicePending,
        'serviceApproved': serviceApproved,
        'serviceDeclined': serviceDeclined,
        'activate_mybookings': 'active'
    }
    return render(request, 'customers/myBookings.html',context)

