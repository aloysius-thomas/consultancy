from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from services.forms import AdminLoginForm
from services.forms import BirthdayBookingForm
from services.forms import BusinessMeetingBookingForm
from services.forms import CandidateForm
from services.forms import CollegeTourForm
from services.forms import CompanyForm
from services.forms import ConstructionForm
from services.forms import FamilyTourForm
from services.forms import HoneymoonForm
from services.forms import LiveShowBookingForm
from services.forms import ProductLaunchBookingForm
from services.forms import SoloTourForm
from services.forms import VacancyForm
from services.forms import WeddingBookingForm
from services.models import Candidate
from services.models import Company
from services.models import Construction
from services.models import Event
from services.models import Tour
from services.models import Vacancy


def admin_required(login_url='admin-login-view'):
    return user_passes_test(lambda u: u.is_superuser, login_url=login_url)


def admin_banned(login_url='login'):
    return user_passes_test(lambda u: u.is_superuser == False, login_url=login_url)


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


def company_view(request):
    companies = Company.objects.all()
    return render(request, 'services/company.html', {'companies': companies})


def company_details_view(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'services/company_details.html', {'company': company})


@login_required
@admin_banned()
def book_product_launch_view(request):
    title = 'Product Launch Booking'
    if request.method == 'POST':
        form = ProductLaunchBookingForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.event_type = 'product_launch'
            event.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = ProductLaunchBookingForm()
    return render(request, 'services/forms/product_launch_form.html', {'form': form, 'title': title})


@admin_banned
@login_required
def book_business_meeting_view(request):
    title = 'Business Meeting Booking'
    if request.method == 'POST':
        form = BusinessMeetingBookingForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.event_type = 'business_meeting'
            event.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = BusinessMeetingBookingForm()
    return render(request, 'services/forms/business_meeting_form.html', {'form': form, 'title': title})


@admin_banned
@login_required
def book_live_show_view(request):
    title = 'Live Show Booking'
    if request.method == 'POST':
        form = LiveShowBookingForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.event_type = 'live_show'
            event.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = LiveShowBookingForm()
    return render(request, 'services/forms/live_show_form.html', {'form': form, 'title': title})


@admin_banned
@login_required
def book_wedding_view(request):
    title = 'Wedding Booking'
    if request.method == 'POST':
        form = WeddingBookingForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.event_type = 'wedding'
            event.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = WeddingBookingForm()
    return render(request, 'services/forms/wedding_form.html', {'form': form, 'title': title})


@admin_banned
@login_required
def book_birthday_view(request):
    title = 'Birthday Booking'
    if request.method == 'POST':
        form = BirthdayBookingForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.event_type = 'birthday'
            event.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = BirthdayBookingForm()
    return render(request, 'services/forms/birthday_form.html', {'form': form, 'title': title})


@admin_banned
@login_required
def construction_service_view(request, service):
    title = f'{service.title()} Booking'
    if request.method == 'POST':
        form = ConstructionForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.booked_by = request.user
            event.service_type = service
            event.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = ConstructionForm()
    return render(request, 'services/forms/construction_form.html', {'form': form, 'title': title})


@admin_banned
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
            tour.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = SoloTourForm()
    return render(request, 'services/forms/solo_tour_form.html', {'form': form, 'title': title})


@admin_banned
@login_required
def family_tour_view(request):
    title = 'Family Tour Booking'
    if request.method == 'POST':
        form = FamilyTourForm(request.POST)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.booked_by = request.user
            tour.event_type = 'family'
            tour.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = FamilyTourForm()
    return render(request, 'services/forms/family_tour_form.html', {'form': form, 'title': title})


@admin_banned
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
            tour.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = CollegeTourForm()
    return render(request, 'services/forms/college_tour_form.html', {'form': form, 'title': title})


@admin_banned
@login_required
def honeymoon_view(request):
    title = 'Honeymoon Booking'
    if request.method == 'POST':
        form = HoneymoonForm(request.POST)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.booked_by = request.user
            tour.event_type = 'honeymoon'
            tour.number_of_person = 2
            tour.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = CollegeTourForm()
    return render(request, 'services/forms/honeymoon_tour_form.html', {'form': form, 'title': title})


@admin_banned()
@login_required
def candidate_register_view(request):
    title = 'Register Candidate'
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.added_by = request.user
            candidate.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = CandidateForm()
    return render(request, 'services/forms/candidate_register_form.html', {'form': form, 'title': title})


@admin_banned
@login_required
def vacancy_submit_view(request):
    title = 'Submit Vacancy  '
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.posted_by = request.user
            candidate.save()
            messages.success(request, 'Successfully Saved!')
            return redirect('home')
    else:
        form = VacancyForm()
    return render(request, 'services/forms/vacancy_submit_form.html', {'form': form, 'title': title})


@admin_required
def company_create_view(request):
    title = 'Submit Company  '
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CompanyForm()
    return render(request, 'services/forms/company_form.html', {'form': form, 'title': title})


@admin_required()
def admin_home_view(request):
    title = 'Home'
    return render(request, 'admin/home.html', {'title': title})


@admin_required()
def candidate_list_view(request):
    data = Candidate.objects.all()
    title = 'Candidate List'
    return render(request, 'admin/human_resource/candidate_list.html', {'data': data, 'title': title})


@admin_required()
def vacancy_list_view(request):
    data = Vacancy.objects.all()
    title = 'Vacancy List'
    return render(request, 'admin/human_resource/vacancy_list.html', {'data': data, 'title': title})


@admin_required()
def company_list_view(request):
    data = Company.objects.all()
    title = 'Company List'
    return render(request, 'admin/human_resource/company_list.html', {'data': data, 'title': title})


@admin_required()
def product_launch_list(request):
    data = Event.objects.filter(event_type='product_launch')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'Product Launch List'
    return render(request, 'admin/event/product_launch_list.html', {'data': data, 'title': title})


@admin_required()
def business_meeting_list(request):
    data = Event.objects.filter(event_type='business_meeting')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'Business Meeting List'
    return render(request, 'admin/event/business_meeting_list.html', {'data': data, 'title': title})


@admin_required()
def live_show_list(request):
    data = Event.objects.filter(event_type='live_show')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'Live Show List'
    return render(request, 'admin/event/live_show_list.html', {'data': data, 'title': title})


@admin_required()
def wedding_list(request):
    data = Event.objects.filter(event_type='wedding')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'Wedding List'
    return render(request, 'admin/event/wedding_list.html', {'data': data, 'title': title})


@admin_required()
def birthday_list(request):
    data = Event.objects.filter(event_type='birthday')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'Birthday  List'
    return render(request, 'admin/event/birthday_list.html', {'data': data, 'title': title})


@admin_required()
def construction_list(request):
    data = Construction.objects.filter(service_type='construction')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'Construction  List'
    return render(request, 'admin/constructions/construction_list.html', {'data': data, 'title': title})


@admin_required()
def interior_2d_list(request):
    data = Construction.objects.filter(service_type='interior_2d')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'Interior 2D-Drawing  List'
    return render(request, 'admin/constructions/construction_list.html', {'data': data, 'title': title})


@admin_required()
def interior_3d_list(request):
    data = Construction.objects.filter(service_type='interior_3d')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'Interior 3D-Drawing  List'
    return render(request, 'admin/constructions/construction_list.html', {'data': data, 'title': title})


@admin_required()
def solo_tour_list(request):
    data = Tour.objects.filter(tour_type='solo')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'Solo Tour List'
    return render(request, 'admin/tour/solo_tour_list.html', {'data': data, 'title': title})


@admin_required()
def family_tour_list(request):
    data = Tour.objects.filter(tour_type='family')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'Family Tour List'
    return render(request, 'admin/tour/family_tour_list.html', {'data': data, 'title': title})


@admin_required()
def college_tour_list(request):
    data = Tour.objects.filter(tour_type='college')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'College Tour List'
    return render(request, 'admin/tour/college_tour_list.html', {'data': data, 'title': title})


@admin_required()
def honeymoon_list(request):
    data = Tour.objects.filter(tour_type='honeymoon')
    status = request.GET.get('status', None)
    if status:
        data = data.filter(status=status)
    title = 'Honeymoon List '
    return render(request, 'admin/tour/honeymoon_list.html', {'data': data, 'title': title})


def admin_login_view(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('admin-home')
    else:
        form = CompanyForm()
    return render(request, 'admin/login.html', {'form': form})


@admin_required()
def admin_logout_view(request):
    logout(request)
    return redirect('admin-login-view')
