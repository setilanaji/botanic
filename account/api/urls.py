from django.urls import path
from account.api.views import (
    registration_view,
    ObtainAuthTokenView,
    account_properties_view,
    update_account_view,
    does_account_exist_view,
    ChangePasswordView,
    ActivateAccount,
)


urlpatterns = [
    path('check_if_account_exists/', does_account_exist_view, name="check_if_account_exists"),
    path('change_password/', ChangePasswordView.as_view(), name="change_password"),
    path('properties/', account_properties_view, name="properties"),
    path('properties/update/', update_account_view, name="update"),
    path('register/', registration_view, name="register"),
    path('login/', ObtainAuthTokenView.as_view(), name="login"),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name="activate"),
]
