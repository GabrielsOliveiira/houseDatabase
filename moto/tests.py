from django.test import TestCase
from datetime import date

from .models import Moto, Oleo, Washed, Chain

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

class ExpiredTest(TestCase):
    def setUp(self):
        self.moto = Moto.objects.create(dono="Lucas")
        self.washed = Washed.objects.create(date=date(2026,8,20), moto=self.moto)
        self.oleo_corrente = Chain.objects.create(date=date(2026,8,20), moto=self.moto)

    def test_washed_is_not_expired(self):
        self.assertFalse(self.washed.expired(data=date(2026,8,27)))

    def test_washed_is_expired(self):
        self.assertTrue(self.washed.expired(data=date(2026,8,28)))

    def test_oleo_corrente_is_not_expired(self):
        self.assertFalse(self.oleo_corrente.expired(data=date(2026,8,27)))

    def test_oleo_corrente_is_expired(self):
        self.assertTrue(self.oleo_corrente.expired(data=date(2026,8,28)))

class MotoFunctionsTest(TestCase):

    def setUp(self):
        self.moto = Moto.objects.create(dono="Rodrigo")
        self.oleo = Oleo.objects.create(price=50, date=date(2026, 2, 25), kms=0, moto=self.moto)

    def test_check_last_oil_func(self):
        self.assertEqual(self.moto.ultimo_oleo, self.oleo)

