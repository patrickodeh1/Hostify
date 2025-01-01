from django import forms
from django.contrib.auth.models import User
from .models import User, Hotel, Room, Booking

class UserRegistrationForm(forms.ModelForm):
  """
  Form for user registration.
  """
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')

  def clean_password2(self):
    """
    Ensures both password fields match.
    """
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError('Passwords don\'t match.')
    return password2

  def save(self, commit=True):
    """
    Hashes the password before saving the user.
    """
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user

class HotelRegistrationForm(forms.ModelForm):
  """
  Form for hotel profile creation.
  """

  class Meta:
    model = Hotel
    fields = ('name', 'address', 'description', 'phone_number', 'email', 'logo', 'amenities')

  def __init__(self, *args, **kwargs):
    super(HotelRegistrationForm, self).__init__(*args, **kwargs)
    self.fields['amenities'].widget = forms.CheckboxSelectMultiple()


class RoomForm(forms.ModelForm):
    """
    Form for creating and editing rooms.
    """

    class Meta:
        model = Room
        fields = ('room_type', 'price', 'availability', 'description', 'images')


class BookingForm(forms.ModelForm):
    """
    Form for creating a booking.
    """

    class Meta:
        model = Booking
        fields = ('room', 'check_in_date', 'check_out_date', 'number_of_guests')

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')
        room = cleaned_data.get('room')

        if check_in_date >= check_out_date:
            raise forms.ValidationError("Check-out date must be after check-in date.")

        # Check for room availability (basic implementation)
        existing_bookings = Booking.objects.filter(
            room=room,
            check_in_date__lte=check_out_date,
            check_out_date__gte=check_in_date
        )
        if existing_bookings.exists():
            raise forms.ValidationError("Room is not available for the selected dates.")

        return cleaned_data