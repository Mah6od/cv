from django.urls import path, include
from cv.views import index

app_name = 'cv'

urlpatterns = [
    # urls , view, name
    path('', index, name= 'index'),
]