from django.conf.urls import url
from registerApp import views

# TEMPLATE TAGGING
app_name = 'registerApp'

urlpatterns = [
    #url(r'^$',views.index,name='registerApp/index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
