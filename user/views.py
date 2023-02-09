from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.urls import reverse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm, PasswordResetForm, CustomSetPasswordForm

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage, send_mail
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetConfirmView

from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import FormView, PasswordContextMixin

from .tokens import account_activation_token
from user.models import User

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        print(user.is_active)
        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('user:login')
    else:
        messages.error(request, "Activate link is invalid!")

    return redirect('user:login')

def activateEmail(request, user, to_email):
    # user = User.objects.get(email=to_email)
    mail_subject = "Activate your user account."
    message = render_to_string("user/template_activate_account.html", {
        'user': user.full_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user.full_name}, please go to you email {to_email} inbox and click on '
            f'received activation link to confirme and complete the registration. Note: Check your spam folder.')
    else:
        message.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def login(request):
    user = request.user
    if user.is_authenticated:
        return redirect('ask_chat:ask_anything')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        # if form.is_valid():
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('ask_chat:ask_anything'))
        else:
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.is_superuser = False
            user.is_staff = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('user:login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=user_email)
            except Exception:
                user = False
            if user:
                subject = 'Request reset password'
                email_template_name = 'user/reset_password_email.html'
                cont = {
                    'email': user.email,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                msg_html = render_to_string(email_template_name, cont)
                try:
                    send_mail(subject, 'Link', 'noreply@askaaron.app', [user.email], fail_silently=True, html_message=msg_html)
                except Exception:
                    return HttpResponse('Invalid Header')
                return redirect('password_reset_done')
            else:
                messages.error(request, "User not found")
                return redirect('reset_password')
    return render(request, template_name='user/password_reset.html')
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'user/password_reset_confirm.html'



def custom_page_not_found_view(request, exception):
    return render(request, "user/404.html", {})

# def custom_error_view(request, exception=None):
#     return render(request, "errors/500.html", {})
#
# def custom_permission_denied_view(request, exception=None):
#     return render(request, "errors/403.html", {})
#
# def custom_bad_request_view(request, exception=None):
#     return render(request, "errors/400.html", {})