from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.contrib.auth.models import User

from .serializers import MyFileSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class MyFileView(APIView):
    # MultiPartParser AND FormParser
    # https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
    # "You will typically want to use both FormParser and MultiPartParser
    # together in order to fully support HTML form data."
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print('upload file : \n')
        print(request.data)
        print(f"uploaded_by: {request.data['uploaded_by']}")
        file_serializer = MyFileSerializer(data=request.data)
        print("valid: " + str(file_serializer.is_valid()))
        if file_serializer.is_valid():
            user = User.objects.filter(email__contains=request.data['uploaded_by']).first()
            print(user)
            # file_serializer['uploaded_by'] = user.pk
            file_serializer.save()
            return Response(
                file_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                file_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
