from django.urls import path
from .import views

urlpatterns = [
        # path('',views.index,name='index'),
        path('cbv/',views.Tasklistview.as_view(),name='cbv'),
        path('cbvdet/',views.Tasklistview.as_view(),name='cbvdet')

]