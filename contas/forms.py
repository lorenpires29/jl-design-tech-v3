from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm,SetPasswordForm,UserCreationForm
from django.core.exceptions import ValidationError
User=get_user_model()
class CadastroForm(UserCreationForm):
 email=forms.EmailField(required=True)
 first_name=forms.CharField(label="Nome",max_length=150,required=True)
 class Meta:
  model=User
  fields=("username","first_name","email","password1","password2")
 def clean_email(self):
  email=self.cleaned_data["email"].strip().lower()
  if User.objects.filter(email__iexact=email).exists(): raise ValidationError("Este e-mail já está cadastrado.")
  return email
class PerfilForm(forms.ModelForm):
 class Meta:
  model=User
  fields=("first_name","last_name","email")
 def __init__(self,*args,**kwargs):
  super().__init__(*args,**kwargs)
  for field in self.fields.values(): field.required=True
 def clean_email(self):
  email=self.cleaned_data["email"].strip().lower()
  if User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists(): raise ValidationError("E-mail já cadastrado.")
  return email
