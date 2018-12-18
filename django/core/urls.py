from django.urls import path

# from . import views
from .views import core_view, email_create, email_delete, email_detail,\
    email_update,home_view, send_email_msg, send_msg, show_all_email,\
    signup, sign_up,view_sent_email

app_name = 'core'

urlpatterns = [
    path('core/', core_view.as_view()),
    path('core/send_msg/', send_msg, name='send_email_msg'),
    path('core/send_email_msg/', send_email_msg.as_view(), name='send_email_msg'),
    path('core/signup/', signup, name='signup'),
    path('core/view_sent_email/', view_sent_email),
    path('core/sign_up/', sign_up.as_view(), name='sign_up'),
    path('core/show_all_email/', show_all_email.as_view(), name="show_all_email"),
    # path('core/<int:pk>/', email_detail.as_view(), name="email_detail"),
    path('core/<int:id>/', email_detail.as_view(), name="email_detail"),
    path('core/<int:id>/update/', email_update.as_view(), name="email_update"),
    path('core/<int:id>/delete/', email_delete.as_view(), name="email_delete"),
    path('core/create_email/', email_create.as_view(), name="email_create"),
    path('', home_view.as_view(), name='app_home'),
]