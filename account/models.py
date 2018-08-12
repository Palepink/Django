from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    phone = models.DecimalField(max_digits=11, decimal_places=0)  # 十进制数字
    birthDay = models.DateField(blank=True)
    school = models.CharField(blank=True, max_length=200)
    sex = models.BooleanField('性别', max_length=1, choices=((0, '男'), (1, '女'),), default=0)

    def __str__(self):
        return 'user {}'.format(self.user.username)
