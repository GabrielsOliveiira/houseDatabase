from django.test import TestCase
from datetime import date

from .models import Moto, Oleo

# Create your tests here.
class NeedChangeOilTests(TestCase):

    def setUp(self):
        self.moto = Moto.objects.create(dono="Lucas")
        self.oleo = Oleo.objects.create(price=50, date=date(2026, 2, 25), kms=0, moto=self.moto)

    def test_change_oil_returns_true_when_km_exceeds_limit(self):
        self.assertTrue(self.oleo.need_to_change(1501))

    def test_change_oil_returns_true_when_km_is_in_limit(self):
        self.assertTrue(self.oleo.need_to_change(1500))

    def test_change_oil_returns_false_when_km_is_bellow_limit(self):
        self.assertFalse(self.oleo.need_to_change(1499.5))