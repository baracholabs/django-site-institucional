import uuid
from django.test import TestCase
from model_bakery import baker

from core.models import get_file_path

# baker.make(Service, 3 )
# baker.make()


class GetFilePathTestCase(TestCase):
    def setUp(self):
        self.filename = f"{uuid.uuid4()}.png"

    def test_get_file_path(self):
        filename = get_file_path(None, "test.png")
        self.assertTrue(len(filename), len(self.filename))


class ServiceTestCase(TestCase):
    def setUp(self):
        self.service = baker.make("Service")

    def test_str(self):
        self.assertEquals(str(self.service), self.service.service)


class TeamRoleTestCase(TestCase):
    def setUp(self):
        self.teamRole = baker.make("TeamRole")

    def test_str(self):
        self.assertEquals(str(self.teamRole), self.teamRole.role)


class TeamMemberTestCase(TestCase):
    def setUp(self):
        self.teamMember = baker.make("TeamMember")

    def test_str(self):
        self.assertEquals(str(self.teamMember), self.teamMember.name)
