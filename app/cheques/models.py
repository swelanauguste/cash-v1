from django.conf import settings
from django.db import models
from django.urls import reverse
from django.shortcuts import redirect
from hitcount.models import HitCountMixin

User = settings.AUTH_USER_MODEL


# class ChequeStatus(models.Model):
#     name = models.CharField(max_length=20)

#     class Meta:
#         ordering = ["name"]
#         verbose_name_plural = "Cheque statuses"

#     def __str__(self):
#         return self.name


class ChequeManager(HitCountMixin, models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False, is_printed=False, is_delivered=False, is_cancelled=False, is_processing=True)


class Cheque(models.Model):
    """
    Model for cheques.
    """

    # status = models.ForeignKey(ChequeStatus, on_delete=models.CASCADE, default=1)
    vendor = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    note = models.TextField(blank=True)
    is_processing = models.BooleanField(default=True)
    is_cancelled = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_printed = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cheques_created_by"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cheques_updated_by"
    )
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    cheque_objects = ChequeManager()

    class Meta:
        ordering = ["-created"]

    def get_absolute_url(self):
        return reverse("cheques:detail", kwargs={"pk": self.pk})
    
    def mark_as_printed(self, *args, **kwargs):
        if self.is_printed == False:
            self.is_printed = True
        super(Cheque, self).save(*args, **kwargs)
        return redirect("/")

    # def mark_as_printed(self):
    #     if self.is_printed == False:
    #         return self.is_printed == True
    #     return self.is_printed

    def __str__(self):
        return self.vendor + " - " + self.payment_method + " - $" + str(self.amount)


class ChequeComment(models.Model):
    """
    Model for comments.
    """

    cheque = models.ForeignKey(Cheque, on_delete=models.CASCADE)
    comment = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_created_by"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_updated_by"
    )
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.comment + " - " + str(self.cheque)
