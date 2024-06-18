from django.contrib import admin

# Register your models here.
from modules_django.olms.models import StudentBorrower, BorrowedHist

admin.site.register(StudentBorrower)
admin.site.register(BorrowedHist)