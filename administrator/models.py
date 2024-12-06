from django.db import models


class Students(models.Model):
    first_name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    age = models.IntegerField()
    group = models.CharField(max_length=255, default='Unknown')
    coin = models.IntegerField()
    hobbi = models.CharField(max_length = 256)
    tolov = models.CharField(max_length = 256)
    filial = models.CharField(max_length = 256)
    study_time = models.TimeField()
    laptop = models.CharField(max_length = 256)
    
    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"

    def __str__(self):
        return self.first_name

    

class Teachers(models.Model):
    first_name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    age = models.IntegerField()
    groups = models.CharField(max_length=255, default='Unknown')
    salary = models.IntegerField()
    work = models.CharField(max_length = 256)
    work_time = models.TimeField()
    language = models.CharField(max_length = 256)
    filial = models.CharField(max_length = 256)
    extra_lesson = models.CharField(max_length = 256)

    
    class Meta:
        verbose_name = "O'qitovchi"
        verbose_name_plural = "O'qitovchilar"
    def __str__(self):
        return self.first_name