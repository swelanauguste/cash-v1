from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from hitcount.views import HitCountDetailView, HitCountMixin
from django.shortcuts import render, get_list_or_404
from .models import Cheque, ChequeComment


class ChequeCreateView(CreateView):
    model = Cheque
    fields = ["vendor", "payment_method", "amount", "note"]

    def get_context_data(self, *args, **kwargs):
        context = super(ChequeCreateView, self).get_context_data(*args, **kwargs)
        context["cheques_created_by_user"] = get_list_or_404(
            Cheque.objects.order_by("-updated"),
            created_by=self.request.user,
            is_deleted=False,
        )
        context["cheques_printed"] = (
            Cheque.objects.filter(is_deleted=False)
            .filter(is_printed=True)
            .order_by("-updated")
        )
        return context


class ChequeListView(HitCountMixin, ListView):
    model = Cheque
    paginate_by = 25
    count_hit = True

    def get_queryset(self):
        queryset = Cheque.cheque_objects.all()
        return queryset


class ChequeUpdateView(UpdateView):
    model = Cheque
    fields = ["vendor", "payment_method", "amount", "note"]


class ChequeDeleteView(DeleteView):
    model = Cheque
    success_url = "/cheques/"


class ChequeDetailView(HitCountDetailView):
    model = Cheque
    count_hit = True
