from django import forms
from django.core.exceptions import ValidationError

error_message = {
    'required':'مقدار دهی به این فیلد ضروری هست',
    'invalid':'مقداری که به این فیلد داده اید نا معتبر است'
}


class CreateArticleForm(forms.Form):
    Title = forms.CharField(max_length=100, label="عنوان داستان ", widget=forms.TextInput(attrs={'class':'form-control'}), help_text="Enter title the story.")
    Text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label="متن داستان ", error_messages=error_message)
    Image = forms.ImageField(label="تصویر داستان ", widget=forms.FileInput(attrs={'class':'form-control'}))
    is_show = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), required=False, label="ایا داستان نمایش داده شود یا در حالت پش نوس قرا بگیرد ؟ ")
    # auther = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="نام نویسنده ")
# نام نویسنده دیگه لازم نیست که وارد بشه چون به صورت خودکار نام کاربری که مقاله رو ایجاد کرده قرار میگیره

    # def clean_Title(self):
    #     title = self.cleaned_data['Title']
    #     if 'iran' not in title.lower():
    #         print("user")
    #         raise ValidationError('this title has to has word iran.')
    #     return title

class EditArticleForm(forms.Form):
    Title = forms.CharField(max_length=100, label="عنوان داستان ",widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Enter title the story.")
    Text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="متن داستان ",error_messages=error_message)
    Image = forms.ImageField(label="تصویر داستان ", widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    is_show = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False,label="ایا داستان نمایش داده شود یا در حالت پش نوس قرا بگیرد ؟ ")
