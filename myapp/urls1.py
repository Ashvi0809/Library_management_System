from django.urls import path
from . import views1

app_name = 'myapp'

urlpatterns = [
    path('', views1.index, name='index'),
    path('about/', views1.about, name='about'),
    path('<int:book_id>/', views1.detail, name='detail'),
    path('feedback/', views1.getFeedback, name='feedback1'),  # updated URL name to 'feedback1'
    path('findbooks/', views1.findbooks, name='findbooks'),
    path('place_order/', views1.place_order, name='place_order'),

]

