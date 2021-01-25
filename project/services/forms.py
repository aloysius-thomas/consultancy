from django import forms

from services.models import Event


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
