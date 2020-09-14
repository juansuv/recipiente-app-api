from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@juansuarez.com", password=("test123."))
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@juansuarez.com", password="test123.",
            name="nombredelusuariotest")

    def test_user_listed(self):
        """mira que se muestres todos los usuarios"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """test que mira si se crea la pagina para cada usuari"""
        url=reverse('admin:core_user_change',args=[self.user.id])
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, 200)
    
    def test_user_add_page(self):
        """test que mira si se crea la pagina para cada usuari"""
        url=reverse('admin:core_user_add')
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, 200)