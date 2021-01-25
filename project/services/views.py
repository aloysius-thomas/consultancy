from django.shortcuts import render


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
