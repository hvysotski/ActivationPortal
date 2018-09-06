from rest_framework import serializers
from .models import ActivationCode, Credentials


class CredentialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credentials
        fields = ('cea_login', 'cea_password', 'cima_login', 'cima_password')


class ActivationCodeSerializer(serializers.ModelSerializer):
    credentials = CredentialsSerializer(read_only=True)

    class Meta:
        model = ActivationCode
        fields = ('activation_code', 'credentials')

