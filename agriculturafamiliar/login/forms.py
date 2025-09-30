from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class EmailLoginForm(forms.Form):
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("E-mail ou senha inválidos")
            
            self.user_cache = authenticate(username=user.username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("E-mail ou senha inválidos")
        return self.cleaned_data

    def get_user(self):
        return getattr(self, "user_cache", None)
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput)
    email = forms.EmailField(label="E-mail")
    telefone = forms.CharField(label="Telefone")
    cidade = forms.CharField(label="Cidade")

    class Meta:
        model = User
        fields = ["username", "email"]  # username vai ser o nome completo
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")
        if p1 != p2:
            raise ValidationError("As senhas não coincidem")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            # salvar os dados extras em um perfil separado
            from .models import UserProfile
            profile = UserProfile(
                user=user,
                telefone=self.cleaned_data["telefone"],
                cidade=self.cleaned_data["cidade"]
            )
            profile.save()
        return user
