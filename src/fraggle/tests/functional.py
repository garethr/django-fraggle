from django.test.client import Client

from fraggle.tests.common import Fraggle
from fraggle.models import Fragment

class Functional(Fraggle):
    
    def test_admin_exists(self):
        self.login_as_admin()
        response = self.client.get('/admin/fraggle/fragment/')
        self.assert_code(response, 200)

    def test_add_view_in_admin_exists(self):
        self.login_as_admin()
        response = self.client.get('/admin/fraggle/fragment/add/')
        self.assert_code(response, 200)
        
    def test_fragment_admin_view_exists(self):
        Fragment.objects.all().delete()
        self.assert_counts([0,], [Fragment,])
        fragment1 = Fragment(
            title='fragment1',
        )
        fragment1.save()
        self.assert_counts([1,], [Fragment,])
        self.login_as_admin()
        response = self.client.get('/admin/fraggle/fragment/%s' % str(fragment1.id))
        self.assert_code(response, 302)
        response = self.client.get('/admin/fraggle/fragment/%s/' % str(fragment1.id))
        self.assert_code(response, 200)
