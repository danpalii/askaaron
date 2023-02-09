import openai
import asyncio
import aiohttp
import requests

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from ask_chat.forms import *
from django.views.generic import TemplateView
from ask_chat.utils import getCHAT
from asgiref.sync import async_to_sync, sync_to_async
from django.http import JsonResponse
from django.core import serializers

def index(request):
    return render(request, 'ask_chat/index.html')

class GPTChatView(TemplateView):
    template_name = 'ask_chat/ask-anything.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form = ChatForm()

    def get_context_data(self, *args, **kwargs):
        context = super(GPTChatView, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['api_response'] = None
        context['user_question'] = None
        return context

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            context = self.get_context_data(**kwargs)
            temperature = request.POST.get('temperature')
            context_present = request.POST.get('context')
            question = request.POST.get('question')
            answer = request.POST.get('answer')
            try:
                if(context_present == "YES"):
                    prompt = f"{question}"
                    response = getCHAT(prompt, temperature)
                    dialog = response.strip()
                    self.form = ChatForm({
                        'answer': f"{prompt}",
                        'response':f"{dialog}\n",
                        'context': context,
                        'temperature': temperature,
                    })
                    context['api_response'] = response

                else:
                    prompt = question
                    response = getCHAT(prompt, temperature)
                    dialog = response.strip()
                    self.form = ChatForm({
                        'answer' :f"AARON: {dialog}",
                        'context':context,
                        'temperature':temperature
                    })
                    context['api_response'] = f"AARON: {response}"
#     openai.error.RateLimitError: The server had an error while processing your request. Sorry about that!
#             openai.error.ServiceUnavailableError: The server is overloaded or not ready yet.
            except openai.error.RateLimitError:
                context['api_response'] = 'Too Many Requests. Wait!'

            context['form'] = self.form
            context['user_question'] = question
            return JsonResponse({'api_response': context['api_response'], 'user_question': context['user_question']})


        return super().post(request, *args, **kwargs)

def error_401(request):
    return render(request, 'ask_chat/../user/templates/user/401.html')