from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Ativo


class AtivoModelTests(TestCase):
    def test_ativo_str_representation(self):
        ativo = Ativo.objects.create(
            tipo="Computador",
            nome="Dell",
            numero_patrimonio="ABC123",
            status="disponível",
        )
        self.assertEqual(str(ativo), "Computador - Dell (ABC123)")


class AtivoListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="testpass")

    def test_list_view_authenticated(self):
        self.client.login(username="tester", password="testpass")
        response = self.client.get(reverse("ativo_list"))
        self.assertEqual(response.status_code, 200)
