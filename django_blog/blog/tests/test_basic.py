import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_post_list_renders(client):
resp = client.get(reverse('post_list'))
assert resp.status_code == 200


@pytest.mark.django_db
def test_create_post_requires_login(client):
resp = client.get(reverse('post_create'))
assert resp.status_code in (302, 403)
