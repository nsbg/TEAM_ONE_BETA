from django.db import models

# 장고 ORM을 이용하여 DB 테이블 생성
class User(models.Model):
    user_id = models.TextField(max_length=10, verbose_name='아이디')
    user_pw = models.TextField(max_length=64, verbose_name='비밀번호')
    user_email = models.EmailField(verbose_name='이메일')
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')

    def __str__(self):
        return self.user_id 