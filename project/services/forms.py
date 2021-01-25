from django import forms
from django.contrib.auth import authenticate

from services.models import Candidate
from services.models import Company
from services.models import Construction
from services.models import Event
from services.models import Tour
from services.models import Vacancy


class ProductLaunchBookingForm(forms.ModelForm):
    date_of_event = forms.DateTimeField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Event
        fields = {
            'date_of_event',
            'type_of_venue',
            'number_of_person',
            'food_items',
            'light_and_sound',
        }


class BusinessMeetingBookingForm(forms.ModelForm):
    date_of_event = forms.DateTimeField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Event
        fields = {
            'date_of_event',
            'type_of_venue',
            'number_of_person',
            'food_items',
            'light_and_sound',
        }


class LiveShowBookingForm(forms.ModelForm):
    date_of_event = forms.DateTimeField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Event
        fields = {
            'date_of_event',
            'type_of_venue',
            'number_of_person',
            'number_of_security',
            'food_items',
            'light_and_sound',
        }


class WeddingBookingForm(forms.ModelForm):
    date_of_event = forms.DateTimeField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Event
        fields = {
            'date_of_event',
            'type_of_venue',
            'number_of_person',
            'number_of_security',
            'number_of_days',
            'amount',
            'transportation',
            'photography',
            'beautician',
            'food_items',
            'light_and_sound',
        }


class BirthdayBookingForm(forms.ModelForm):
    date_of_event = forms.DateTimeField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Event
        fields = {
            'date_of_event',
            'type_of_venue',
            'number_of_person',
            'amount',
            'food_items',
            'light_and_sound',
        }


class ConstructionForm(forms.ModelForm):
    work_progress = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Construction
        fields = {
            'number_of_day',
            'square_feet',
            'work_progress',
            'construction_plan',
        }


class SoloTourForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Tour
        fields = {
            'date',
            'number_of_days',
            'type_of_hotel',
            'food_items',
        }


class FamilyTourForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Tour
        fields = {
            'date',
            'number_of_days',
            'type_of_hotel',
            'food_items',
            'number_of_person',
            'transportation',
            'need_tour_guid',
        }


class CollegeTourForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Tour
        fields = {
            'date',
            'number_of_days',
            'number_of_boys',
            'number_of_girls',
            'number_of_staff',
            'number_of_room',
            'type_of_hotel',
            'food_items',
            'transportation',
            'need_tour_guid',
        }


class HoneymoonForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Tour
        fields = {
            'date',
            'number_of_days',
            'food_items',
            'type_of_hotel',
            'need_tour_guid',
        }


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = {
            'category',
            'full_name',
            'age',
            'qualification',
            'skills',
            'job_position',
            'address',
            'pin_code',
            'email',
        }


class VacancyForm(forms.ModelForm):
    date_of_interview = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    time = forms.DateTimeField(input_formats=['%H:%M'])

    class Meta:
        model = Vacancy
        fields = {
            'post_name',
            'number_of_post',
            'skills',
            'salary_package',
            'job_description',
            'experience',
            'date_of_interview',
            'venue',
            'time',
        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class AdminLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid credentials")
            if not user.check_password(password):
                raise forms.ValidationError("Invalid credentials")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active")

        return super(AdminLoginForm, self).clean()
