from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestests(TestCase):
    def setUp(self):
        self.dados = {
            "nome": "Foo Bar",
            "email": "foo@bar.com",
            "assunto": "The subject",
            "mensagem": "The mensagem",
        }

        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy("index"), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Foobar',
            'assunto': 'The subject'
        }
        request = self.client.post(reverse_lazy("index"), data=dados)
        self.assertEquals(request.status_code, 200)
