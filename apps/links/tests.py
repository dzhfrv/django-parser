from rest_framework import status
from rest_framework.test import APIClient

from apps.authentication.tests import BaseTestClass, create_user
from .models import Link
from .serializers import CreateLinkSerializer


class TestLinkResource(BaseTestClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.endpoint = '/api/v1/links/'

    def setUp(self):
        super().setUp()
        self.link = Link.objects.create(
            user=self.base_user,
            link='https://example.com',
            status=1,
        )
        Link.objects.create(
            user=create_user('new@email.com'),
            link='https://example2.com',
            status=1,
        )
        self.new_link = {
            'link': 'https://new-example.com',
            'status': 1,
        }

    def test_get_all_links_unauth(self):
        anonimus = APIClient()
        resp = anonimus.get(self.endpoint)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_all_links_success(self):
        resp = self.client.get(self.endpoint)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        expected = CreateLinkSerializer(
            Link.objects.all(),
            many=True).data
        self.assertEqual(resp.json(), expected)

    def test_add_link_unauth(self):
        anonimus = APIClient()
        resp = anonimus.post(self.endpoint)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_add_link_success(self):
        resp = self.client.post(self.endpoint, self.new_link)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Link.objects.count(), 3)
        self.assertEqual(resp.json(), {'id': Link.objects.last().id})

    def test_create_link_status_type(self):
        self.new_link['status'] = 'text'
        resp = self.client.post(self.endpoint, self.new_link)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_link_unauth(self):
        anonimus = APIClient()
        resp = anonimus.get(f'{self.endpoint}{self.link.id}/')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_link_not_exists(self):
        resp = self.client.get(f'{self.endpoint}999/')
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_link_success(self):
        resp = self.client.get(f'{self.endpoint}{self.link.id}/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        expected = CreateLinkSerializer(
            Link.objects.get(pk=self.link.pk)).data
        self.assertEqual(resp.json(), expected)

    def test_update_link(self):
        resp = self.client.post(f'{self.endpoint}{self.link.id}/')
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
