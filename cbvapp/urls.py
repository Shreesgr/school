from django.urls import path
from cbvapp import views

app_name='cbvapp'

urlpatterns =[
    
    path('',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>',views.SchoolDetails.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>',views.SchoolUpdate.as_view(),name='update'),
    path('delete/<int:pk>',views.SchoolDelete.as_view(),name='delete'),

]