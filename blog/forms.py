from django import forms
from django.core.validators import ValidationError
from django.template.defaultfilters import title

from blog.models import Message


class ContactUsForm(forms.Form):
    BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
    FAVORITE_COLORS_CHOICES = {
        "blue": "Blue",
        "green": "Green",
        "black": "Black",
    }

    name = forms.CharField(max_length=500, label='Your Name', required=False)
    text = forms.CharField(widget=forms.Textarea, label='Your Message')
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={'class': 'form-control'}),
        label='Your Birth Year', required=False)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES, label='Your Favorite Colors')

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        # if any(char.isdigit() for char in name):
        #     self.add_error('name',"نام نباید شامل عدد باشد!")
        if name == text:
            raise ValidationError('name and text cannot be the same', code='name_text_same')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise ValidationError("نام نباید شامل عدد باشد!", code='isdigit')
        return name


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # fields = ('title', 'text', 'email')
        # fields = '__all__'
        exclude = ('created','type')
        widgets={
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Your Title',
                'style':'max-width:300px',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
            })
        }