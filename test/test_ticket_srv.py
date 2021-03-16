import unittest
from services.ticket import Ticket

class TestTicketSrv(unittest.TestCase):
    def __init__(self, methodName=""):
        super(TestTicketSrv, self).__init__(methodName)
        self.ticketSrv = Ticket()
        self.ticketSrv.data = [{
            "_id": "tickit-1",
            "subject": "ticket 1",
            "organization_id": 1,
            "submitter_id": 1,
            "assignee_id": 2
        },
        {
            "_id": "ticket-2",
            "subject": "ticket 2",
            "organization_id": 2,
            "submitter_id": 2,
            "assignee_id": 3
        },
        {
            "_id": "ticket-3",
            "subject": "ticket 3",
            "organization_id": 3,
            "submitter_id": 1,
            "assignee_id": 2
        }]

    def test_get_user_and_organization(self):
        self.ticketSrv.get_user_and_organization()
        self.assertTrue(len(self.ticketSrv.tickets_by_assignee.keys()) > 0)
        self.assertTrue(len(self.ticketSrv.tickets_by_submitter.keys()) == 2)
        self.assertTrue(len(self.ticketSrv.tickets_by_orgs.keys()) > 0)


    
    def test_find_tickets(self):
        tickets = self.ticketSrv.finds("subject", "ticket 3")
        self.assertTrue(len(tickets) > 0)
        self.assertEqual(tickets[0]["subject"], "ticket 3")
        self.assertEqual(tickets[0]["organization_id"], 3)
        self.assertEqual(tickets[0]["assignee_id"], 2)

        tickets = self.ticketSrv.finds("assignee_id", 2)
        self.assertTrue(len(tickets) == 2)
    
    def test_list_fields(self):
        fields = self.ticketSrv.fields
        self.assertTrue("_id" in fields)
        self.assertTrue("organization_id" in fields)
        self.assertTrue("subject" in fields)
        self.assertTrue("submitter_id" in fields)
        self.assertFalse("name" in fields)
