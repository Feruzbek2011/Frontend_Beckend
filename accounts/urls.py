from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

urlpatterns=[
    path('signup/', SignUpView, name='signup'),
    path('password/', PasswordsChangeView.as_view(), name='password'),
    path('user/edit/done/', UserChangeDoneView.as_view(), name='user_done'),
    path('user/edit/', UsersChangeView, name='edit'),
    path('password_done/', PasswordChangeDoneView.as_view(), name='password_done')
    # path('accounts/password_change_form/', HomePasswordChangeView.as_view(), name='password_change_form'),
]
