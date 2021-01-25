from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from services.forms import ProductLaunchBookingForm


def about_us_view(request):
    return render(request, 'services/about-us.html', {})


def contact_us_view(request):
    return render(request, 'services/contact-us.html', {})


def human_resource_page_view(request):
    return render(request, 'services/human_resources.html', {})


def event_management_page_view(request):
    return render(request, 'services/event_management.html', {})


def construction_page_view(request):
    return render(request, 'services/construction.html', {})


def tour_page_view(request):
    return render(request, 'services/tour.html', {})


def marketing_view(request):
    return render(request, 'services/marketing.html', {})


@login_required
def book_product_launch_view(request):
    title = 'Product Launch Booking'
    if request.method == 'POST':
        form = ProductLaunchBookingForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.event_type = 'product_launch'
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = ProductLaunchBookingForm()
    return render(request, 'services/forms/product_launch_form.html', {'form': form, 'title': title})
