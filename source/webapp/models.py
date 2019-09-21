from django.db import models

STATUS_DEFAULT = 'active'
RECORD_STATUS = [(STATUS_DEFAULT, 'Активно'), ('blocked','Заблокировано')]


class Record(models.Model):
    author = models.CharField(max_length=40, null=False, blank=False, verbose_name='Имя автора')
    author_email = models.EmailField(null=False, blank=False, verbose_name='Почтовый адрес автора')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=20, verbose_name='Статус',default=STATUS_DEFAULT, choices=RECORD_STATUS)

    def __str__(self):
        return self.text
