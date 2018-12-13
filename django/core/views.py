from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import TemplateView, FormView, ListView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import send_msg_form
from .models import email_data


# All Class-based-views
class core_view(TemplateView):
    template_name = "core/core_index.html"


class home_view(View):
    template_name = "core/index.html"
    def get(self, request, *args, **kwargs):
        count = User.objects.count()
        context = {
            'count': count
        }
        return render(request, self.template_name, context)

# Signup forms
class sign_up(FormView):
    """This class signs user into the DB."""
    template_name = "core/signup.html"
    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/signup_successful.html")


# Send email
class send_email_msg(FormView):
    """This class will send emails and insert into the DB."""
    template_name = "core/send_msg.html"
    def get(self, request, *args, **kwargs):
        form = send_msg_form() # No request.GET else form validation takes place.
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = send_msg_form(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('/')
            return render(request, 'core/send_msg_successful.html')


# List all the sent e-mails
class show_all_email(ListView):
    paginate_by = 3
    queryset = email_data.objects.all()
    # template_name = "core/email_data_list.html"
    # def get(self, request):
    #     queryset = email_data.objects.all()
    #     context = {
    #         'object_list': queryset
    #     }
    #     return render(request, self.template_name, context)


# ALL Function-based-views below.
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

def home(request):
    count = User.objects.count()
    context = {
        'count': count
    }
    return render(request, "core/index.html", context)

# Display all signed-up users
def view_sent_email(request):
    template_name = "core/email_data_list.html"
    queryset = email_data.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)


# Function based view send_msg moved tp class based view send_email_msg
def send_msg(request):
    form = send_msg_form(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'core/send_msg.html', context)


# Function based view signup moved to class based view
def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "core/signup.html", context)