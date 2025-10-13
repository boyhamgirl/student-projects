from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
class Meta:
model = Post
fields = ["title", "body", "published", "tags"]


class CommentForm(forms.ModelForm):
class Meta:
model = Comment
fields = ["body"]


class SignUpForm(UserCreationForm):
class Meta:
model = User
fields = ("username", "email")
