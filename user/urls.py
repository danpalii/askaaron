from django.conf.urls import url
from django.urls import path

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from .views import login, register, logout, activate, password_reset_request
app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),

    path('activate/<uidb64>/<token>', activate, name='activate'),

    path('password_reset/', password_reset_request, name='password_reset'),

    # path('password-reset/',
    #      auth_views.PasswordResetView.as_view(
    #          template_name='user/password_reset.html',
    #          email_template_name='user/reset_password_email.html',
    #          success_url = reverse_lazy('index')
    #      ),
    #      name='reset_password'),
    #
    # path(r'reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(
    #          template_name='user/password_reset_confirm.html',
    #      ),
    #      name='password_reset_confirm'),
    #
    # path('password-reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(
    #          template_name='ask_chat/index.html'
    #      ),
    #      name='password_reset_done'),
    #
    # # path('password-reset-confirm/<uidb64>/<token>/',
    # #      auth_views.PasswordResetConfirmView.as_view(
    # #          template_name='user/password_reset_confirm.html'
    # #      ),
    # #      name='password_reset_confirm'),
    #
    # path('password-reset-complete/',
    #      auth_views.PasswordResetCompleteView.as_view(
    #          template_name='ask_chat/index.html'
    #      ),
    #      name='password_reset_complete'),

    # path('password_change', password_change, name='password_change'),
    # path('password_reset', password_reset_request, name='password_reset'),
    # path('reset/<uidb64>/<token>', passwordResetConfirm, name='password_reset_confirm')

    # path('password_reset/', auth_views.PasswordResetView.as_view(
    #     email_template_name='user/reset_password_email.html',
    #     template_name='user/password_reset.html',
    #     success_url=reverse_lazy('user:password_reset_done'),
    #
    # ), name='password_reset'),
    #
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #     template_name='user/password_reset_confirm.html'
    # ), name='password_reset_confirm'),
    #
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]