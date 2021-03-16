import unittest
from services.organization import Organization

class TestOrganizationSrv(unittest.TestCase):
    def __init__(self, methodName=""):
        super(TestOrganizationSrv, self).__init__(methodName)
        self.organizationSrv = Organization()
        self.organizationSrv.data = [{
            "_id": 100,
            "domain_names": ["dm100", "dm102", "dm103"],
            "tags": ["tag1", "tag11", "tag111"],
            "name": "organization 1"
        },
        {
            "_id": 200,
            "domain_names": ["dm201", "dm202", "dm203"],
            "tags": ["tag2", "tag22", "tag222"],
            "name": "organization 2"
        },
        {
            "_id": 300,
            "domain_names": ["dm301", "dm302", "dm303"],
            "tags": ["tag3", "tag33", "tag333"],
            "name": "organization 3"
        }]

    def test_get_orgs_by_id(self):
        
        self.organizationSrv.get_orgs_by_id()
        org = self.organizationSrv.orgs_by_ids[200]
        self.assertIsNotNone(org)
        self.assertEqual(org["name"], "organization 2")


    
    def test_find_organizations(self):
        organizations = self.organizationSrv.finds("domain_names", "dm301")
        self.assertTrue(len(organizations) == 1)
        self.assertEqual(organizations[0]["name"], "organization 3")
        self.assertEqual(organizations[0]["_id"], 300)

        organizations = self.organizationSrv.finds("tags", "tag22")
        self.assertTrue(len(organizations) == 1)
        self.assertEqual(organizations[0]["name"], "organization 2")
        self.assertEqual(organizations[0]["_id"], 200)

        organizations = self.organizationSrv.finds("tags", "tag444")
        self.assertTrue(len(organizations) == 0)
    
    def test_list_fields(self):
        fields = self.organizationSrv.fields
        self.assertTrue("_id" in fields)
        self.assertTrue("tags" in fields)
        self.assertTrue("domain_names" in fields)
