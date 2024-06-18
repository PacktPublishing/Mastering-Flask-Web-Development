from rest_framework import serializers
from modules_django.olms.models import StudentBorrower, BorrowedHist

class StudentBorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentBorrower
        fields=('id','studid', 'firstname', 'lastname')
        
class BorrowedHistSerializer(serializers.ModelSerializer):
    class Meta:
        model=BorrowedHist
        fields=('id', 'studid', 'borrowed_date')