from django.core.exceptions import ValidationError
from django.db import models
from account.models import Account


# class YEAR(models.Model):
#     year = models.CharField(max_length=30, primary_key=True, blank=False)
#     course1 = models.CharField(max_length=20, unique=True)
#     course2 = models.CharField(max_length=20, unique=True)
#     course3 = models.CharField(max_length=20, unique=True)
#     course4 = models.CharField(max_length=20, unique=True)
#     course5 = models.CharField(max_length=20, unique=True)
#     course6 = models.CharField(max_length=20, unique=True)
#     course7 = models.CharField(max_length=20, unique=True)
#

class Student(models.Model):
    email = models.ForeignKey(Account, to_field='email', db_column='email', on_delete=models.CASCADE)
    Student_Name = models.CharField(max_length=30)
    Student_ID = models.CharField(max_length=12, unique=True, primary_key=True)
    # S_Year = models.ForeignKey(YEAR, to_field='year', blank=False, null=False, on_delete=models.CASCADE)

    # class Meta:
    #     unique_together = ('Student_ID', 'S_Year')

    def __str__(self):
        return self.Student_ID

    # deleting the image folder
    def delete(self, *args, **kwargs):
        x = Image.objects.get().student_image
        x.delete(save=False)
        super(Student, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        try:
            this = Image.objects.get(id=self.Student_ID)
            if this.student_id != self.Student_ID:
                this.student_image.delete()
        except:
            pass
        super(Student, self).save(*args, **kwargs)


class Image(models.Model):
    student_id = models.ForeignKey(Student, to_field='Student_ID', on_delete=models.CASCADE)
    student_image = models.TextField(max_length=10000000, null=False, blank=False)

    def delete(self, *args, **kwargs):
        self.student_image.delete(save=False)
        super(Image, self).delete(*args, **kwargs)


class Professor(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    email = models.ForeignKey(Account, to_field='email', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

#
# class Prepmaterials(models.Model):
#     material = models.CharField(unique=True, max_length=30)
#
#     def __str__(self):
#         return self.material

# class YEAR(models.Model):
#     Year = models.ForeignKey(Student,to_field='Year', primary_key=True, max_length=30,on_delete=models.CASCADE,null=False)
#     course1 = models.CharField(max_length=20, unique=True)
#     course2 = models.CharField(max_length=20, unique=True)
#     course3 = models.CharField(max_length=20, unique=True)
#     course4 = models.CharField(max_length=20, unique=True)
#     course5 = models.CharField(max_length=20, unique=True)
#     course6 = models.CharField(max_length=20, unique=True)
#     course7 = models.CharField(max_length=20, unique=True)
