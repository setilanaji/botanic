from rest_framework import status
from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import authenticate, login
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib import messages
from django.shortcuts import reverse

from django.core.mail import EmailMessage

from account.api.serializers import RegistrationSerializer, AccountPropertiesSerializer, ChangePasswordSerializer
from account.models import Account
from rest_framework.authtoken.models import Token


# Register
# Url: https://<your-domain>/api/account/register
from account.tokens import account_activation_token


@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view(request):
    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0').lower()
        if validate_email(email) != None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            data['key'] = 'email.inuse'
            return Response(data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        username = request.data.get('username', '0')
        if validate_username(username) != None:
            data['error_message'] = 'That username is already in use.'
            data['response'] = 'Error'
            data['key'] = 'username.inuse'
            return Response(data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            # data['pk'] = account.pk
            token = Token.objects.get(user=account).key
            # data['token'] = token
            data['is_active'] = account.is_active
            current_site = get_current_site(request)
            subject = 'Activate Your Taneman Account'
            # url = 'http://192.168.43.243:8000' + reverse('confirm_email', kwargs={'user_id': user_id, 'token': token})

            message = render_to_string('account_activation_email.html', {
                'user': account,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(account.pk)),
                'token': account_activation_token.make_token(account),
            })
            mail = EmailMessage(subject, message, to=[account.email],
                                from_email=settings.EMAIL_HOST_USER)
            mail.content_subtype = 'html'
            mail.send()
            # account.email_account(subject, message)
        else:
            data = serializer.errors

        return Response(data, )


@permission_classes([])
@authentication_classes([])
class ActivateAccount(APIView):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = Account.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.email_confirmed = True
            user.save()
            # login(request, user)
            return render(request, 'registration_success.html')
            # return redirect('home')
        else:
            return render(request, 'registration_failed.html')
            # return redirect('home')


def validate_email(email):
    account = None
    try:
        account = Account.objects.get(email=email)
    except Account.DoesNotExist:
        return None
    if account != None:
        return email


def validate_username(username):
    account = None
    try:
        account = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return None
    if account != None:
        return username


# Account properties
# Url: https://<your-domain>/api/account/
# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def account_properties_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data)


# Account update properties
# Url: https://<your-domain>/api/account/properties/update
# Headers: Authorization: Token <token>
@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def update_account_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AccountPropertiesSerializer(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Account update success'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# LOGIN
# URL: http://127.0.0.1:8000/api/account/login

class ObtainAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        data = {}
        # print(self.request.POST.get('username'))
        email = request.POST.get('username')
        password = request.POST.get('password')
        print(email)
        print(password)
        account = authenticate(email=email, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            data['response'] = 'Successfully authenticated.'
            # data['pk'] = account.pk
            data['username'] = account.username
            data['email'] = email.lower()
            data['token'] = token.key
            data['is_active'] = account.is_active

            return Response(data, status=status.HTTP_200_OK)
        else:
            data['response'] = 'Error'
            data['error_message'] = 'Invalid credentials'
            data['key'] = 'error.unauthorized.login'
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)





@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def does_account_exist_view(request):
    if request.method == 'GET':
        email = request.GET['email'].lower()
        data = {}
        try:
            account = Account.objects.get(email=email)
            data['response'] = email
        except Account.DoesNotExist:
            data['response'] = "Account does not exist"
        return Response(data)


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = Account
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            # confirm the new passwords match
            new_password = serializer.data.get("new_password")
            confirm_new_password = serializer.data.get("confirm_new_password")
            if new_password != confirm_new_password:
                return Response({"new_password": ["New passwords must match"]}, status=status.HTTP_400_BAD_REQUEST)

            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"response": "successfully changed password"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)