from fraggle.tests.common import Fraggle
from fraggle.models import Fragment

class Unit(Fraggle):

    def test_object_creation(self):
        self.assert_counts([2,], [Fragment,])
