from django.db import models

# Create your models here.
class StudentBorrower(models.Model):
    id = models.AutoField(primary_key=True)
    studid = models.TextField(max_length=15, blank=False, unique=True)
    firstname = models.TextField(max_length=50, blank=False)
    lastname = models.TextField(max_length=50, blank=False)

class BorrowedHist(models.Model):
    id = models.AutoField(primary_key=True)
    studid = models.ForeignKey("StudentBorrower", on_delete=models.CASCADE, to_field="studid")
    borrowed_date = models.DateField(blank=False)