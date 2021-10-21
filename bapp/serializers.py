from rest_framework import serializers
from .models import MyFile
from django.contrib.auth.models import User


class MyFileSerializer(serializers.ModelSerializer):
    # uploaded_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = MyFile
        fields = ('file', 'description', 'uploaded_date', 'uploaded_by')

    # def save(self, request):
    #     user = User.objects.filter(email__contains=self.validated_data['uploaded_by']).first()
    #     print("in myfile serializer:")
    #     print(user)
    #     print(self.validated_data)
    #     mfile = MyFile(
    #         file=self.validated_data['file'],
    #         description=self.validated_data['description'],
    #         uploaded_by=user
    #     )
    #
    #     mfile.save()
    #     return mfile
