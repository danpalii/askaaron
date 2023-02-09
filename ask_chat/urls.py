from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import GPTChatView
app_name = 'ask_chat'

urlpatterns = [
    # path('ask-anything/', ask_anything, name='ask_anything'),
    path('ask_anything/', login_required(GPTChatView.as_view()), name='ask_anything'),
]