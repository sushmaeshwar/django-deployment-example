from django.conf.urls import re_path
from basicapp import views

#template urls
app_name='basicapp'

urlpatterns=[
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login,name='user_login'),
]