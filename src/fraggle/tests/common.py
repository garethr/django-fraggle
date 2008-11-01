from django.db import connection
from django.contrib.auth.models import User
from django.test import TestCase
from django.template import Context, Template

from fraggle.models import Fragment

class Fraggle(TestCase):

    def setUp(self):
        self.fragment1 = Fragment(
            title='fragment1',
            content='test'
        )
        self.fragment1.save()
        self.fragment2 = Fragment(
            title='fragment2',
            content='h2. test'
        )
        self.fragment2.save()
        
    def tearDown(self):
        Fragment.objects.all().delete()

    tag_libraries = []

    # helper methods
          
    def login_as_admin(self):
        "Create, then login as, an admin user"
        user = User.objects.create_user('admin', 'admin@example.com', 'password')
        user.is_staff = True
        user.is_superuser = True
        user.save()

    def render(self, template, **kwargs):
        template = "".join(["{%% load %s %%}" % lib for lib in self.tag_libraries]) + template
        return Template(template).render(Context(kwargs)).strip()

    # custom assertions
    
    def assert_code(self, response, code):
        "Assert that a given response returns a given HTTP status code"
        self.assertEqual(code, response.status_code, "HTTP Response status code %d expected, but got %d" % (code, response.status_code))
    
    def assert_equal(self, *args, **kwargs):
        "Assert that two values are equal"
        return self.assertEqual(*args, **kwargs)

    def assert_contains(self, needle, haystack):
        return self.assert_(needle in haystack, "Content should contain `%s' but doesn't:\n%s" % (needle, haystack))

    def assert_render_contains(self, expected, template, **kwargs):
        "Asserts than a given template and context rendering contains a given fragment"
        self.assert_contains(expected, self.render(template, **kwargs))

    def assert_render(self, expected, template, **kwargs):
        "Asserts than a given template and context render a given fragment"
        self.assert_equal(expected, self.render(template, **kwargs))

    def assert_counts(self, expected_counts, models):
        "Assert than a list of numbers is equal to the number of instances of a list of models"
        actual_counts = [model.objects.count() for model in models]
        self.assert_equal(expected_counts, actual_counts, "%s should have counts %s but had %s" % ([m.__name__ for m in models], expected_counts, actual_counts))