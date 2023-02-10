from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.contrib.auth.forms import SetPasswordForm
from user.views import CustomPasswordResetConfirmView
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.views.defaults import page_not_found

from user.admin import admin_view
admin.site.admin_view = admin_view

import ask_chat
from ask_chat import views

urlpatterns = [
    url(r'^admin/login/', page_not_found),
    url(r'^admin/', admin.site.urls),
    # path('admin/', admin.site.urls),
    path('', ask_chat.views.index, name='index'),
    path('ask/', include('ask_chat.urls', namespace='ask_chat')),
    path('user/', include('user.urls', namespace='user')),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='ask_chat/index.html'
         ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='ask_chat/index.html'
         ),
         name='password_reset_complete'),

]


handler404 = 'user.views.custom_page_not_found_view'
# handler500 = 'my_app_name.views.custom_error_view'
# handler403 = 'my_app_name.views.custom_permission_denied_view'
# handler400 = 'my_app_name.views.custom_bad_request_view'