from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^index/',views.index),
    url(r'^add/',views.add),
    url(r'^get/',views.get),
]