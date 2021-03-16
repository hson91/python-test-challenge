import unittest
from services.user import User

class TestUserSrv(unittest.TestCase):
    def __init__(self, methodName=""):
        super(TestUserSrv, self).__init__(methodName)
        self.userSrv = User()
        self.userSrv.data = [{
            "_id": 1,
            "organization_id": 1,
            "name": "name 1",
            "shared_tickets": False,
        },
        {
            "_id": 2,
            "organization_id": 2,
            "name": "name 2",
            "shared_tickets": False,
        },
        {
            "_id": 3,
            "organization_id": 3,
            "name": "name 3",
        }]

    def test_get_user_by_orgs(self):
        self.userSrv.get_user_by_orgs()
        self.assertTrue(len(self.userSrv.userByOrg.keys()) > 0)
        self.assertEqual(self.userSrv.userByOrg[1][0]["name"], "name 1")
    
    def test_find_user(self):
        users = self.userSrv.finds("_id", 2)
        self.assertTrue(len(users) > 0)
        self.assertEqual(users[0]["name"], "name 2")

        users = self.userSrv.finds("shared_tickets", False)
        self.assertTrue(len(users) == 2)
    
    def test_list_fields(self):
        fields = self.userSrv.fields
        self.assertTrue("_id" in fields)
        self.assertTrue("organization_id" in fields)
        self.assertTrue("name" in fields)
