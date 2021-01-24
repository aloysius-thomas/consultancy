from django.shortcuts import render


def about_us_view(request):
    return render(request, 'site/about-us.html', {})


def contact_us_view(request):
    return render(request, 'site/contact-us.html', {})


def human_resource_page_view(request):
    return render(request, 'site/human_resources.html', {})
