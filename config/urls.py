from django.contrib import admin
from django.conf.urls import url, include
from app.account import views as account_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', account_views.index, name='index'),
]
