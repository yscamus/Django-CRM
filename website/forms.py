from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import FilmLog
from django.core.validators import MaxValueValidator

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta: 
			model = User
			fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
			super(SignUpForm, self).__init__(*args, **kwargs)
			self.fields['username'].widget.attrs['class'] = 'form-control'
			self.fields['username'].widget.attrs['placeholder'] = 'User Name'
			self.fields['username'].label = ''
			self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

			self.fields['password1'].widget.attrs['class'] = 'form-control'
			self.fields['password1'].widget.attrs['placeholder'] = 'Password'
			self.fields['password1'].label = ''
			self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

			self.fields['password2'].widget.attrs['class'] = 'form-control'
			self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
			self.fields['password2'].label = ''
			self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


# Create Add FilmLog Form
class AddFilmLogForm(forms.ModelForm):
    class Meta:
        model = FilmLog  # Specify the model
        fields = [
            'film_title',
            'genre',
            'director',
            'year_of_release',
            'personal_rating',
            'review',
            'would_recommend',
            'I_have_seen_this_film_before',
        ]  # List the fields you want to include in the form

        widgets = {
            'film_title': forms.TextInput(attrs={"placeholder": "Film Title", "class": "form-control"}),
            'genre': forms.TextInput(attrs={"placeholder": "Genre", "class": "form-control"}),
            'director': forms.TextInput(attrs={"placeholder": "Director", "class": "form-control"}),
            'year_of_release': forms.NumberInput(attrs={"placeholder": "Year of Release", "class": "form-control"}),
            'personal_rating': forms.NumberInput(attrs={
                "placeholder": "Personal Rating (out of 5, e.g., 4.5)",
                "class": "form-control",
                "step": "0.1"
            }),
            'review': forms.Textarea(attrs={
                "placeholder": "Write your review here...",
                "class": "form-control",
                "rows": 5
            }),
            'would_recommend': forms.RadioSelect(choices=[
                (True, "Yes"),
                (False, "No")
            ]),
            'I_have_seen_this_film_before': forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }



def clean_personal_rating(self):
        """Additional validation for the personal_rating field."""
        personal_rating = self.cleaned_data.get('personal_rating')
        if personal_rating is not None and personal_rating > 5.0:
            raise forms.ValidationError("The rating must not exceed 5.0.")
        return personal_rating


