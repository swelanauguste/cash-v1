import decimal, random

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User

from ...models import Cheque, ChequeComment

CATEGORIES = [
    "person",
    "address",
    "internet",
    "phone_number",
    "company",
    "credit_card",
]



class Provider(faker.providers.BaseProvider):
    def e_cat(self):
        return self.random_element(CATEGORIES)


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        # fake = Faker()
        
        # for _ in range(10):
        #     company = fake.company().upper()[:8]
        #     vendor = ''.join(e for e in company if e.isalnum())
        #     payment_method = fake.currency_code()
        #     pricetag = fake.pricetag().replace('$', '')
        #     pricetag = pricetag.replace('.', '')
        #     pricetag = pricetag.replace(',', '')
        #     amount = decimal.Decimal(pricetag)
        #     note = fake.paragraph()
        #     is_deleted = fake.boolean()
        #     created_by = User.objects.get(pk=random.randint(1, 2))
        #     updated_by = User.objects.get(pk=random.randint(1, 2))
        #     cheque = Cheque.objects.get_or_create(vendor=vendor, payment_method=payment_method, amount=amount, note=note, is_deleted=is_deleted, created_by=created_by, updated_by=created_by)
        cheques = Cheque.objects.all()
        for ch in cheques:
            ch.is_printed = False
            ch.save()
            # print()
        # print("Adding faker data to the database")
        
        # fake.add_provider(Provider)
        # company = fake.company().upper()[:8]
        # vendor = ''.join(e for e in company if e.isalnum())

        # print(fake.e_cat())

        # boolean
        # paragraph
        # pricetag
        # currency_code
