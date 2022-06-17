from django.urls import path
from blo.views import IndexView, PostView

app_name = "blo"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('<slug:slug>/', PostView.as_view(), name="post")
]
