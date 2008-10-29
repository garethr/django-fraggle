from django.test import TestCase
from django.template import Context, Template
from fraggle.models import Fragment

class Fraggle(TestCase):

    def setUp(self):
        self.fragment1 = Fragment(
            title='fragment1',
            content='test'
        ).save()
        self.fragment2 = Fragment(
            title='fragment2',
            content='h2. test'
        ).save()
        
    def tearDown(self):
        Fragment.objects.all().delete()

    tag_libraries = []

    # helper methods

    def render(self, template, **kwargs):
        template = "".join(["{%% load %s %%}" % lib for lib in self.tag_libraries]) + template
        return Template(template).render(Context(kwargs)).strip()

    # custom assertions
    
    def assert_equal(self, *args, **kwargs):
        "Assert that two values are equal"
        return self.assertEqual(*args, **kwargs)

    def assert_not_equal(self, *args, **kwargs):
        "Assert that two values are not equal"
        return not self.assertEqual(*args, **kwargs)

    def assert_contains(self, needle, haystack):
        return self.assert_(needle in haystack, "Content should contain `%s' but doesn't:\n%s" % (needle, haystack))

    def assert_doesnt_contain(self, needle, haystack):
        return self.assert_(needle not in haystack, "Content should not contain `%s' but does:\n%s" % (needle, haystack))

    def assert_render_contains(self, expected, template, **kwargs):
        "Asserts than a given template and context rendering contains a given fragment"
        self.assert_contains(expected, self.render(template, **kwargs))

    def assert_render_doesnt_contain(self, expected, template, **kwargs):
        "Asserts than a given template and context rendering does not contain a given fragment"
        self.assert_render_doesnt_contain(expected, self.render(template, **kwargs))

    def assert_render(self, expected, template, **kwargs):
        "Asserts than a given template and context render a given fragment"
        self.assert_equal(expected, self.render(template, **kwargs))

    def assert_count(self, expected, model):
        "Assert that their are the expected number of instances of a given model"
        actual = model.objects.count()
        self.assert_equal(expected, actual, "%s should have %d objects, had %d" % (model.__name__, expected, actual))

    def assert_counts(self, expected_counts, models):
        "Assert than a list of numbers is equal to the number of instances of a list of models"
        if len(expected_counts) != len(models):
            raise("Number of counts and number of models should be equal")
        actual_counts = [model.objects.count() for model in models]
        self.assert_equal(expected_counts, actual_counts, "%s should have counts %s but had %s" % ([m.__name__ for m in models], expected_counts, actual_counts))
        
    def assert_raises(self, *args, **kwargs):
        "Assert than a given function and arguments raises a given exception"
        return self.assertRaises(*args, **kwargs)