from django.urls import path

# from . import views
from .views import core_view, home_view, send_email_msg, send_msg

app_name = 'core'

urlpatterns = [
    path('core/', core_view.as_view()),
    # path('core/send_msg/', send_email_msg.as_view(), name='send_email_msg'),
    path('core/send_msg/', send_msg, name='send_email_msg'),
    path('', home_view.as_view()),
]