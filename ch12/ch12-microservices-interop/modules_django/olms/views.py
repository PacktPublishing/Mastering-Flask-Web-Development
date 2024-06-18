from rest_framework.response import Response
from rest_framework.decorators import api_view
from modules_django.olms.serializer import BorrowedHistSerializer, StudentBorrowerSerializer
from modules_django.olms.models import StudentBorrower, BorrowedHist

@api_view(['GET'])
def getData(request):
    app = StudentBorrower.objects.all()
    serializer = StudentBorrowerSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = StudentBorrowerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"message:error"})