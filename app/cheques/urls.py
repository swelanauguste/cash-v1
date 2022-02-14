from django.urls import path

from . import views

app_name = "cheques"

urlpatterns = [
    path("", views.ChequeListView.as_view(), name="list"),
    path("new", views.ChequeCreateView.as_view(), name="create"),
    path("detail/<int:pk>", views.ChequeDetailView.as_view(), name="detail"),
    path("edit/<int:pk>", views.ChequeUpdateView.as_view(), name="update"),
    path("del/<int:pk>", views.ChequeDeleteView.as_view(), name="delete"),
]
