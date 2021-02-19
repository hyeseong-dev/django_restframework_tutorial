from django.urls    import include, path
from rest_framework import routers
from quickstart     import views

urlpatterns = [
    path('',  include('snippets.urls')),

]

