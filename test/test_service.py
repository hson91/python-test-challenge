import unittest
from services import Services

class TestServices(unittest.TestCase):
    def __init__(self, methodName=""):
        super(TestServices, self).__init__(methodName)
        self.srv = Services()
        self.set_data_test()

    def set_data_test(self):
        self.srv.User.data = [{
            "_id": 1,
            "organization_id": 100,
            "name": "name 1",
            "shared_tickets": False,
        },
        {
            "_id": 2,
            "organization_id": 200,
            "name": "name 2",
            "shared_tickets": False,
        },
        {
            "_id": 3,
            "organization_id": 300,
            "name": "name 3",
        }]

        self.srv.User.get_user_by_orgs()

        self.srv.Ticket.data = [{
            "_id": "tickit-1",
            "subject": "ticket 1",
            "organization_id": 100,
            "submitter_id": 1,
            "assignee_id": 2
        },
        {
            "_id": "ticket-2",
            "subject": "ticket 2",
            "organization_id": 200,
            "submitter_id": 2,
            "assignee_id": 3
        },
        {
            "_id": "ticket-3",
            "subject": "ticket 3",
            "organization_id": 300,
            "submitter_id": 1,
            "assignee_id": 2
        }]
        self.srv.Ticket.get_user_and_organization()

        self.srv.Organization.data = [{
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
        self.srv.Organization.get_orgs_by_id()


    def test_find_users(self):
        users = self.srv.find_users("_id", 1)
        self.assertTrue(len(users) == 1)
        for u in users:
            self.assertTrue("tickets" in u)
            self.assertTrue("organization_name" in u)

        users = self.srv.find_users("organization_id", 300)
        self.assertTrue(len(users) == 1)
        self.assertEqual(users[0]["organization_name"], "organization 3")
        self.assertEqual(users[0]["_id"], 3)
        self.assertTrue("ticket 2" in users[0]["tickets"])


    def test_find_tickets(self):
        tickets = self.srv.find_tickets("subject", "ticket 2")
        self.assertTrue(len(tickets) == 1)
        self.assertTrue("submitter_name" in tickets[0])
        self.assertEqual(tickets[0]["submitter_name"], "name 2")
        self.assertEqual(tickets[0]["assignee_name"], "name 3")

    def test_find_organizations(self):
        organizations = self.srv.find_organizations("tags", "tag33")
        self.assertTrue(len(organizations) == 1)
        self.assertTrue(len(organizations[0]["tickets"]) == 1)
        self.assertEqual(organizations[0]["tickets"][0], "ticket 3")
        self.assertTrue(organizations[0]["users"][0], "name 3")