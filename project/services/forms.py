from django import forms

from services.models import Construction
from services.models import Event
from services.models import Tour


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
    class Meta:
        model = Tour
        fields = {
            'date',
            'number_of_days',
            'type_of_hotel',
            'food_items',
        }
