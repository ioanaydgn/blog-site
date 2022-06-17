from django.urls import path
from blo.views import IndexView, PostView, SearchView

app_name = "blo"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('search/', SearchView.as_view(), name='search'),
    path('<slug:slug>/', PostView.as_view(), name="post"),
    
]
