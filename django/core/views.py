from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import TemplateView, FormView, ListView
from django.http import HttpResponseRedirect

from .forms import send_msg_form
from .models import email_data


# Create your views here.
class core_view(TemplateView):
    template_name = "core/core_index.html"


class home_view(TemplateView):
    template_name = "core/index.html"


class send_email_msg(TemplateView):
    model = email_data
    template_name = "core/send_msg.html"


# def send_msg(request):
#     form = send_msg_form(request.GET)
#     if request.method == "POST":
#         form = send_msg_form(request.POST)
#         if form.is_valid():
#             # form.save()
#             print(form.cleaned_data)
#             email_data.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         'form': form
#     }
#     return render(request, 'core/send_msg.html', context)


def send_msg(request):
    form = send_msg_form(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'core/send_msg.html', context)

# class send_email_msg(FormView):
#     """Send email."""
#     def contact_us(request):
#         if request.method == 'POST':
#             form = send_msg_form(request.POST)
#             if form.is_valid():
#                 sender = form.cleaned_data['sender']
#                 recipient = form.cleaned_data['recipient']
#                 subject = form.cleaned_data['subject']
#                 message = form.cleaned_data['message']
#                 cc_myself = form.cleaned_data['cc_myself']
#                 return(HttpResponseRedirect('/thanks/'))
#         else:
#             form = send_msg_form()
#         return render(request, 'send_msg.html', {'form': form})

