from django.urls import path

from . import views

app_name = "cheques"

urlpatterns = [
    path("", views.ChequeListView.as_view(), name="list"),
    path("new", views.ChequeCreateView.as_view(), name="create"),
    path("detail/<int:pk>", views.ChequeDetailView.as_view(), name="detail"),
    path("mark-printed/<int:pk>", views.mark_as_printed, name="mark-printed"),
    path("del/<int:pk>", views.ChequeDeleteView.as_view(), name="delete"),
]
