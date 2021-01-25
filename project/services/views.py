from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from services.forms import BirthdayBookingForm
from services.forms import BusinessMeetingBookingForm
from services.forms import CollegeTourForm
from services.forms import ConstructionForm
from services.forms import FamilyTourForm
from services.forms import LiveShowBookingForm
from services.forms import ProductLaunchBookingForm
from services.forms import SoloTourForm
from services.forms import WeddingBookingForm


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


@login_required
def book_business_meeting_view(request):
    title = 'Business Meeting Booking'
    if request.method == 'POST':
        form = BusinessMeetingBookingForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.event_type = 'business_meeting'
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = BusinessMeetingBookingForm()
    return render(request, 'services/forms/business_meeting_form.html', {'form': form, 'title': title})


@login_required
def book_live_show_view(request):
    title = 'Live Show Booking'
    if request.method == 'POST':
        form = LiveShowBookingForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.event_type = 'live_show'
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = LiveShowBookingForm()
    return render(request, 'services/forms/live_show_form.html', {'form': form, 'title': title})


@login_required
def book_wedding_view(request):
    title = 'Wedding Booking'
    if request.method == 'POST':
        form = WeddingBookingForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.event_type = 'wedding'
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = WeddingBookingForm()
    return render(request, 'services/forms/wedding_form.html', {'form': form, 'title': title})


@login_required
def book_birthday_view(request):
    title = 'Birthday Booking'
    if request.method == 'POST':
        form = BirthdayBookingForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.event_type = 'birthday'
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = BirthdayBookingForm()
    return render(request, 'services/forms/birthday_form.html', {'form': form, 'title': title})


@login_required
def construction_service_view(request, service):
    title = f'{service.title()} Booking'
    if request.method == 'POST':
        form = ConstructionForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.service_type = service
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = ConstructionForm()
    return render(request, 'services/forms/construction_form.html', {'form': form, 'title': title})


@login_required
def solo_tour_view(request):
    title = 'Solo Tour Booking'
    if request.method == 'POST':
        form = SoloTourForm(request.POST)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.booked_by = request.user
            tour.tour_type = 'solo'
            tour.number_of_person = 1
            tour.need_tour_guid = 'n'
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = SoloTourForm()
    return render(request, 'services/forms/solo_tour_form.html', {'form': form, 'title': title})


@login_required
def family_tour_view(request):
    title = 'Family Tour Booking'
    if request.method == 'POST':
        form = FamilyTourForm(request.POST)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.booked_by = request.user
            tour.event_type = 'family'
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = FamilyTourForm()
    return render(request, 'services/forms/family_tour_form.html', {'form': form, 'title': title})


@login_required
def college_tour_view(request):
    title = 'Collage Tour Booking'
    if request.method == 'POST':
        form = CollegeTourForm(request.POST)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.booked_by = request.user
            tour.event_type = 'college'
            tour.number_of_person = tour.number_of_staff + tour.number_of_girls + tour.number_of_boys
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = CollegeTourForm()
    return render(request, 'services/forms/college_tour_form.html', {'form': form, 'title': title})
