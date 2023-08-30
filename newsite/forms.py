from django import forms
from newsite.models import Employees
from django.contrib.auth.models import User
from newsite.models import Addusernews
from django.contrib.auth import password_validation
# from django.forms import SelectDateWidget
# from bootstrap_datepicker_plus.widgets import DatePickerInput


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()

        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and confirm password does not match"
            )
        password_validation.validate_password(self.cleaned_data.get('password', None))

        return cleaned_data

class DateInput(forms.widgets.DateInput):
    input_type = 'date'


class Addnewsform(forms.ModelForm):

    NEWS_CITY = (
        ('ahmedabad', 'Ahmedabad'),
        ('surat', 'Surat'),
    )

    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    city = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=NEWS_CITY)
    #Usertype = forms.MultipleChoiceField(widget=forms.RadioSelect)
    # newstitle = forms.CharField(widget=forms.Textarea)

    publish_type = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label="Publish type",
                                  initial='', widget=forms.RadioSelect(), required=True)

    # publish_date = forms.DateField(widget=DateInput())
    publish_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))

    class Meta:
        model = Addusernews
        fields = ('newstitle', 'category', 'news', 'city', 'publish_date', 'publish_type')


class UpdateUserForm(forms.ModelForm):

    NEWS_CITY = (
        ('ahmedabad', 'Ahmedabad'),
        ('surat', 'Surat'),
    )

    CATEGORY_CHOICE = (
        ('National', 'National'),
        ('Politics', 'Politics'),
        ('Automobile', 'Automobile'),
        ('Business', 'Business'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Hatke', 'Hatke'),
        ('Health', 'Health'),
        ('International', 'International'),
        ('Miscellaneous', 'Miscellaneous'),
        ('Science', 'Science'),
        ('sports', 'sports'),
        ('Startup', 'Startup'),
        ('Technology', 'Technology'),
        ('World', 'World'),
    )
    newstitle = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICE)
    news = forms.CharField(max_length=500,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=NEWS_CITY)
    publish_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))

    class Meta:
        model = Addusernews
        fields = ('newstitle', 'category', 'news', 'city', 'publish_date', 'publish_type')



