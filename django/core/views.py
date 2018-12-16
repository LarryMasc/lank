from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView, DeleteView, DetailView, FormView, ListView, TemplateView,
    UpdateView, View
    )
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .forms import send_msg_form
from .models import email_data


# ToDo
"""
    - Filter to display all emails by ID ASC
    - Every item in the ListView should be selectable for
        - Update
        - Delete 
"""

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
    r"""ListView using ClassView

    In a listview, the defaults are as followw
    template_name = <app>/<model>_<view>.html

    eg below shows how the class would be defined if the defaults are not
    used.

    class show_all_email(ListView)
    template_name = "core/email_data_list.html"
    def get(self, request):
        queryset = email_data.objects.all()
        context = {
            'object_list': queryset
        }
        return render(request, self.template_name, context)
    """
    # queryset = email_data.objects.all()
    # queryset = email_data.objects.order_by("-id").filter(sender="larry.masc@gmail.com")
    queryset = email_data.objects.order_by("-id")


# Show details of a row
class email_detail(DetailView):
    r"""Display details of a row using Classviews.

    In a detailview, the defaults are as followw
    template_name = <app>/<model>_<view>.html

    eg below shows how the class would be defined if the defaults are not
    used.

    class email_detail(DetailView)
    template_name = "core/email_data_detail.html"
    def get(self, request):
        queryset = email_data.objects.all()
        context = {
            'object_list': queryset
        }
        return render(request, self.template_name, context)
    """
    # queryset = email_data.objects.all()
    template_name = "core/email_data_detail.html"
    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(email_data, id=id_)


# Create view
class email_create(CreateView):
    r"""Example of CreateView using ClassViews.

    """
    template_name = "core/email_data_create.html"
    form_class = send_msg_form
    queryset = email_data.objects.all()
    # success_url = "/"

    r"""Display details of the form in the server log."""
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return "/"


# Create view
class email_update(UpdateView):
    r"""Example of UpdateView using ClassViews.

    """
    template_name = "core/email_data_create.html"
    form_class = send_msg_form
    # Not needed queryset = email_data.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(email_data, id=id_)

    r"""Display details of the form in the server log."""
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# Delete a row
class email_delete(DeleteView):
    r"""Delete a row using Classviews."""
    # queryset = email_data.objects.all()
    template_name = "core/email_data_delete.html"

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(email_data, id=id_)

    def get_success_url(self):
        return reverse("core:show_all_email")







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