from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

class RegisterForm(forms.Form):
    err_me = ' 입력해주세요.'

    email = forms.EmailField(
        error_messages={'required': '이메일을' +err_me},
        max_length=64, label='이메일')
    
    password = forms.CharField(
        error_messages={'required': '비밀번호를' +err_me},
        widget=forms.PasswordInput, label='비밀번호')
    
    re_password = forms.CharField(
        error_messages={'required': '비밀번호를' +err_me},
        widget=forms.PasswordInput, label='비밀번호 확인')
    
    nickname = forms.CharField(
        error_messages={'required': '닉네임을' +err_me},
        max_length=8, label='닉네임')

    divisions = forms.ChoiceField(
        error_messages={'required': '부서를 골라주세요.'},
        label='부서' ,
        choices=(
            ('A','A'),
            ('B','B'),
            ('C','C')
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        nickname = cleaned_data.get('nickname')
        try:
            user_email = User.objects.get(email=email)
            self.add_error('email', '중복된 이메일입니다.')
        except User.DoesNotExist:
            try:
                user_nickname = User.objects.get(nickname=nickname)
                self.add_error('nickname', '중복된 닉네임입니다.')
            except User.DoesNotExist:
                if password and re_password:
                    if password != re_password:
                        self.add_error('password', '비밀번호가 서로 다릅니다.')
                        self.add_error('re_password', '비밀번호가 서로 다릅니다.')
