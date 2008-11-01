from fraggle.tests.common import Fraggle
from fraggle.models import Fragment

class Unit(Fraggle):

    def test_object_creation(self):
        self.assert_counts([2,], [Fragment,])

    def test_creation_of_fragments(self):
        Fragment.objects.all().delete()
        self.assert_counts([0,], [Fragment,])
        fragment1 = Fragment(
            title='fragment1',
            content='test'
        )
        fragment1.save()
        self.assert_equal(fragment1.title, 'fragment1')
        self.assert_equal(fragment1.content, 'test')
        
        self.assert_counts([1,], [Fragment,])
        
    def test_creation_of_fragments_without_content(self):
        Fragment.objects.all().delete()
        self.assert_counts([0,], [Fragment,])
        fragment1 = Fragment(
            title='fragment1',
        )
        fragment1.save()
        self.assert_counts([1,], [Fragment,])
        self.assert_equal(fragment1.title, 'fragment1')
        self.assert_equal(fragment1.content, '')
        
    def test_creation_of_fragments_without_title(self):
        Fragment.objects.all().delete()
        self.assert_counts([0,], [Fragment,])
        fragment1 = Fragment(
            content='test'
        )
        fragment1.save()
        self.assert_counts([1,], [Fragment,])
        self.assert_equal(fragment1.title, '')
        self.assert_equal(fragment1.content, 'test')
        
    def test_html_is_saved_from_content(self):
        self.assert_equal(self.fragment1.html,"<p>test</p>")
        self.assert_equal(self.fragment2.html,"<h2>test</h2>")
        
    def test_html_from_formatted_content(self):
        self.assert_equal(self.fragment1.transform_content(),"<p>test</p>")
        self.assert_equal(self.fragment2.transform_content(),"<h2>test</h2>")
