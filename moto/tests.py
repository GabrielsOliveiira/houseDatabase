from datetime import date

from django.test import TestCase
from django.urls import reverse

from usuario.forms import UsuarioForm
from usuario.models import Usuario

from .models import Chain, Moto, Oleo, Washed


class NeedChangeOilTests(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(email="TesteTando@gmail.com")
        self.usuario.set_password("12345")

        self.moto = Moto.objects.create(
            usuario=self.usuario, cor="Amarelo", placa="12332112"
        )
        self.oleo = Oleo.objects.create(
            price=50, date=date(2026, 2, 25), kms=0, moto=self.moto
        )

    def test_change_oil_returns_true_when_km_exceeds_limit(self):
        self.assertTrue(self.oleo.need_to_change(1501))

    def test_change_oil_returns_true_when_km_is_in_limit(self):
        self.assertTrue(self.oleo.need_to_change(1500))

    def test_change_oil_returns_false_when_km_is_bellow_limit(self):
        self.assertFalse(self.oleo.need_to_change(1499.5))


class ExpiredTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(email="TesteTando@gmail.com")
        self.usuario.set_password("12345")

        self.moto = Moto.objects.create(
            usuario=self.usuario, cor="Amarelo", placa="12332112"
        )
        self.washed = Washed.objects.create(date=date(2026, 8, 20), moto=self.moto)
        self.oleo_corrente = Chain.objects.create(
            date=date(2026, 8, 20), moto=self.moto
        )

    def test_washed_is_not_expired(self):
        self.assertFalse(self.washed.expired(data=date(2026, 8, 26)))

    def test_washed_is_expired(self):
        self.assertTrue(self.washed.expired(data=date(2026, 8, 27)))

    def test_oleo_corrente_is_not_expired(self):
        self.assertFalse(self.oleo_corrente.expired(data=date(2026, 8, 27)))

    def test_oleo_corrente_is_expired(self):
        self.assertTrue(self.oleo_corrente.expired(data=date(2026, 8, 28)))


class MotoFunctionsTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(email="TesteTando@gmail.com")
        self.usuario.set_password("12345")

        self.moto = Moto.objects.create(
            usuario=self.usuario, cor="Amarelo", placa="12332112"
        )
        self.oleo = Oleo.objects.create(
            price=50, date=date(2026, 2, 25), kms=0, moto=self.moto
        )

    def test_check_last_oil_func(self):
        self.assertEqual(self.moto.ultimo_oleo, self.oleo)


class TestSenha(TestCase):
    def teste_email_invalido(self):
        form = UsuarioForm(data={"email": "1234abcd"})
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)


class AlteracaoDeItem(TestCase):
    def setUp(self):
        self.usuario1 = Usuario.objects.create(
            email="user1@gmail.com", first_name="123", username="user1@gmail.com"
        )
        self.usuario2 = Usuario.objects.create(
            email="user2@gmail.com", first_name="123", username="user2@gmail.com"
        )

        self.moto = Moto.objects.create(
            usuario=self.usuario1, cor="Cinza", placa="1234"
        )
        self.oleo = Oleo.objects.create(
            price=50, date=date(2026, 2, 25), kms=1000, moto=self.moto
        )

    def test_excluir_moto_de_outro_usuario(self):
        self.client.force_login(self.usuario2)

        response = self.client.post(reverse("usuario:delMoto", args=[self.moto.id]))

        self.assertEqual(response.status_code, 404)
        self.assertTrue(Moto.objects.filter(id=self.moto.id).exists())

    def test_excluir_propria_moto(self):
        self.client.force_login(self.usuario1)

        response = self.client.post(reverse("usuario:delMoto", args=[self.moto.id]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Moto.objects.filter(id=self.moto.id).exists())

    def test_excluir_oleo_de_outro_usuario(self):
        self.client.force_login(self.usuario2)

        response = self.client.post(reverse("moto:delete", args=["oil", self.oleo.id]))

        self.assertEqual(response.status_code, 404)
        self.assertTrue(Oleo.objects.filter(id=self.oleo.id).exists())

    def test_excluir_proprio_oleo(self):
        self.client.force_login(self.usuario1)

        response = self.client.post(reverse("moto:delete", args=["oil", self.oleo.id]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Oleo.objects.filter(id=self.oleo.id).exists())

    def test_alterar_oleo_de_outro_usuario(self):
        self.client.force_login(self.usuario2)

        response = self.client.post(
            reverse("moto:update", args=["oil", self.oleo.id]),
            data={"price": 10, "date": date(2026, 2, 22), "kms": 0, "moto": self.moto},
        )

        self.assertEqual(response.status_code, 404)

        self.oleo.refresh_from_db()
        self.assertEqual(self.oleo.price, 50)

    def test_alterar_proprio_oleo(self):
        self.client.force_login(self.usuario1)

        response = self.client.post(
            reverse("moto:update", args=["oil", self.oleo.id]),
            data={"price": 10, "date": date(2026, 2, 22), "kms": 0, "moto": self.moto},
        )

        self.assertEqual(response.status_code, 302)

        self.oleo.refresh_from_db()
        self.assertEqual(self.oleo.price, 10)
