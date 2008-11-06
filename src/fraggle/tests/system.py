"System tests test functions, commands and template tags"

from fraggle.tests.common import Common

class System(Common):
    "System test suite"
    
    def test_template_tag_renders_content(self):
        self.assert_render_contains("test", 
            "{% load render_fragment %}{% render_fragment 1 %}")
        self.assert_render_contains("test", 
            "{% load render_fragment %}{% render_fragment 2 %}")
    
    def test_textile_transform_in_template_tag(self):
        self.assert_render("<p>test</p>", 
            "{% load render_fragment %}{% render_fragment 1 %}")
        self.assert_render("<h2>test</h2>", 
            "{% load render_fragment %}{% render_fragment 2 %}")
        
    def test_passing_invalid_fragment_identifier_renders_nothing(self):
        self.assert_render("", 
            "{% load render_fragment %}{% render_fragment 3 %}")
        self.assert_render("", 
            "{% load render_fragment %}{% render_fragment 'a' %}")