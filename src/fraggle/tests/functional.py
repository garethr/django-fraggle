"Functional tests test system behaviour by accessing views"

from fraggle.tests.common import Common, login_as_admin
from fraggle.models import Fragment

class Functional(Common):
    "Functional test suite"
    
    def test_admin_exists(self):
        login_as_admin()
        response = self.client.get('/admin/fraggle/fragment/')
        self.assert_code(response, 200)

    def test_add_view_in_admin_exists(self):
        login_as_admin()
        response = self.client.get('/admin/fraggle/fragment/add/')
        self.assert_code(response, 200)
        
    def test_fragment_admin_view_exists(self):
        Fragment.objects.all().delete()
        self.assert_counts([0], [Fragment])
        fragment1 = Fragment(
            title='fragment1',
        )
        fragment1.save()
        self.assert_counts([1], [Fragment])
        login_as_admin()
        response = self.client.get('/admin/fraggle/fragment/%s' 
            % str(fragment1.id))
        self.assert_code(response, 302)
        response = self.client.get('/admin/fraggle/fragment/%s/' 
            % str(fragment1.id))
        self.assert_code(response, 200)