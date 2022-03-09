import email
from django.db import models

# Create your models here.

class Uesr(models.Model):
    id = models.CharField(max_length=12, verbose_name='아이디')
    email = models.EmailField(verbose_name='Email')
    nickname = models.CharField(max_length=8, verbose_name='닉네임')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='회원가입 시간')
    divisions = models.CharField(max_length=8, verbose_name='기업 규모',
        choices=(
            ('A', ),
            ('B', ),
            ('C', )
        ))
    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'user'
        verbose_name = '계정'
        verbose_name_plural = '계정'