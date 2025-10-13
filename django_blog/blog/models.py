from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Tag(models.Model):
name = models.CharField(max_length=50, unique=True)
slug = models.SlugField(max_length=60, unique=True, blank=True)


def save(self, *args, **kwargs):
if not self.slug:
self.slug = slugify(self.name)
super().save(*args, **kwargs)


def __str__(self):
return self.name


class Post(models.Model):
author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
title = models.CharField(max_length=200)
slug = models.SlugField(max_length=220, unique=True, blank=True)
body = models.TextField()
created = models.DateTimeField(auto_now_add=True)
updated = models.DateTimeField(auto_now=True)
published = models.BooleanField(default=False)
tags = models.ManyToManyField(Tag, blank=True)


class Meta:
ordering = ["-created"]
permissions = [
("can_publish", "Can publish posts"),
]


def save(self, *args, **kwargs):
if not self.slug:
self.slug = slugify(self.title)
super().save(*args, **kwargs)


def get_absolute_url(self):
return reverse("post_detail", args=[self.slug])


def __str__(self):
return self.title


class Comment(models.Model):
post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
body = models.TextField()
created = models.DateTimeField(auto_now_add=True)
updated = models.DateTimeField(auto_now=True)


class Meta:
ordering = ["created"]


def __str__(self):
return f"Comment by {self.author} on {self.post}"
