from django.core.exceptions import ValidationError
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if self.group and self.group.student_set.count() >= 10:
            raise ValidationError('This group already has 10 students.')
        super().save(*args, **kwargs)

