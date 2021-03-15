#!/usr/bin/env python3

from .user import User
from .ticket import Ticket
from .organization import Organization

class Services(object):
    def __init__(self):
        self.User = User()
        self.Ticket = Ticket()
        self.Organization = Organization()
    
    def load_data(self):
        try:
            self.User.load_data()
            self.Ticket.load_data()
            self.Organization.load_data()
        except Exception as e:
            print(e)
    
    def find_users(self, term, value):
        users = self.User.finds(term, value)
        for u in users:
            u["tickets"] = []
            if "organization_id" in u and u["organization_id"] in self.Organization.orgs_by_ids:
                u["organization_name"] = self.Organization.orgs_by_ids[u["organization_id"]]["name"]

            if u["_id"] in self.Ticket.tickets_by_assignee:
                for t  in self.Ticket.tickets_by_assignee[u["_id"]]:
                    u["tickets"].append(t["subject"])

            if u["_id"] in self.Ticket.tickets_by_submitter:
                for t in self.Ticket.tickets_by_submitter[u["_id"]]:
                    u["tickets"].append(t["subject"])
                
        return users
    
    def find_tickets(self, term, value):
        tickets = self.Ticket.finds(term, value)
        for t in tickets:
            if t["assignee_id"] in self.User.userById:
                t["assignee_name"] = self.User.userById[t["assignee_id"]]["name"]

            if t["submitter_id"] in self.User.userById:
                t["submitter_name"] = self.User.userById[t["submitter_id"]]["name"]


        return tickets

    def find_organizations(self, term, value):
        organizations =  self.Organization.finds(term, value)
        for o in organizations:
            o["tickets"] = []
            o["users"] = []

            if o["_id"] in self.Ticket.tickets_by_orgs:
                for t  in self.Ticket.tickets_by_orgs[o["_id"]]:
                    o["tickets"].append(t["subject"])

            if o["_id"] in self.User.userByOrg:
                for u in self.User.userByOrg[o["_id"]]:
                    o["users"].append(u["name"])
                    
        return organizations