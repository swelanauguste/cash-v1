from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from hitcount.views import HitCountDetailView, HitCountMixin
from django.shortcuts import render, get_list_or_404, redirect
from .models import Cheque, ChequeComment


class ChequeCreateView(CreateView):
    model = Cheque
    fields = ["vendor", "payment_method", "amount", "note"]
    success_url = "new"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

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
            .filter(is_delivered=False)
            .filter(is_processing=False)
            .filter(is_cancelled=False)
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


def mark_as_printed(request, pk):
    cheque = Cheque.objects.get(pk=pk)
    cheque.is_printed = True
    cheque.is_processing = False
    cheque.is_cancelled = False
    cheque.is_deleted = False
    cheque.is_delivered = False
    cheque.save()
    return redirect("cheques:list")


class ChequeDeleteView(DeleteView):
    model = Cheque
    success_url = "cheques:list"


class ChequeDetailView(HitCountDetailView):
    model = Cheque
    count_hit = True
