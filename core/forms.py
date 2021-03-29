from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail", max_length=100)
    assunto = forms.CharField(label="Assunto", max_length=100)
    mensagem = forms.CharField(
        label="Mensagem", widget=forms.Textarea(), max_length=500
    )

    def send_mail(self):
        nome = self.cleaned_data.get("nome")
        email = self.cleaned_data.get("email")
        assunto = self.cleaned_data.get("assunto")
        mensagem = self.cleaned_data.get("mensagem")

        conteudo = (
            f"Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nmensagem: {mensagem}"
        )

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email="contato@fusion.com.br",
            to=["contato@fusion.com.br"],
            headers={"Reply-to": email},
        )

        mail.send()
