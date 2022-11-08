
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from requests import HTTPError
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import GenericAPIView
from . import serializers
from .send_email import send_confirmation_email, send_code_password_reset
from django.contrib.auth import get_user_model, login

User = get_user_model()


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                send_confirmation_email(user.email, user.activation_code)
            return Response(serializer.data, status=201)
        return Response('Bad request!', status=400)


class ActivationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Successfully activated'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'Link expired'}, status=400)


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


class LogoutView(GenericAPIView):
    serializer_class = serializers.LogoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully logged out!', status=204)

# def send_mail(request):
#     html = '<html><body> Hello check your gmail</body></html>'
#     send_confirmation_email('krsymr18@gmail.com', '1234')
#     return HttpResponse(html)

class ForgotPasswordView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.ForgotPasswordSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            email = serializer.data.get('email')
            user = User.objects.get(email=email)
            user.create_activation_code()
            user.save()
            send_code_password_reset(user)
            return Response('Check your email, we send a code!', 200)
        except User.DoesNotExist:
            return Response(
                'User with this email does not exists!',
                status=400
            )


class RestorePasswordView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.RestorePasswordSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Password changed successfully!')

class FollowSpamApi(APIView):
    def post(self, request):
        serializer = serializers.SpamViewSerializer(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(email=request.user.email)
        return Response('Followed to spam!', 201)



