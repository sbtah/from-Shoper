from django.urls import path
from panel import views


app_name = "panel"


urlpatterns = [
    path("", views.PanelView.as_view(), name="panel"),
    path("login/", views.LoginUserView.as_view(), name="login"),
]
