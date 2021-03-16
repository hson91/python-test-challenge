#!/usr/bin/env python3

from config import Config
from utilities import read_file_json
from .base import Base

class Ticket(Base):

    def __init__(self):
        self.data = []
        self.tickets_by_assignee = {}
        self.tickets_by_submitter = {}
        self.tickets_by_orgs ={}

    def load_data(self):
        self.data = read_file_json(Config.TICKET_DATA)
        self.get_user_and_organization()

    def get_user_and_organization(self):
        '''
            Convert tickes data to user dict with key is 'assignee_id" and 'submitter_id' \n
            and convert organizations dict with key is 'organization_id'
        '''
        if len(self.data) == 0:
            return
        
        assignees = {}
        submiters = {}
        organizations = {}
        for ticket in self.data:
            if "assignee_id" not in ticket:
                continue

            if "submitter_id" not in ticket:
                continue

            if "organization_id" not in ticket:
                continue
                
            if ticket["assignee_id"] not in assignees:
                assignees[ticket["assignee_id"]] = []
            
            if ticket["submitter_id"] not in submiters:
                submiters[ticket["submitter_id"]] = []
            
            if ticket["organization_id"] not in organizations:
                organizations[ticket["organization_id"]] = []
            
            assignees[ticket["assignee_id"]].append(ticket)
            submiters[ticket["submitter_id"]].append(ticket)
            organizations[ticket["organization_id"]].append(ticket)
        
        self.tickets_by_assignee = assignees
        self.tickets_by_submitter = submiters
        self.tickets_by_orgs = organizations
    
    def finds(self, term, value):
        if len(self.data) == 0:
            return []
        
        tickets = []
        for ticket in self.data:
            if term not in ticket:
                continue

            if type(ticket[term]).__name__ == "list":
                if value in ticket[term]:
                    tickets.append(ticket)
                    continue
            
            if str(ticket[term]) == str(value):
                tickets.append(ticket)

        return tickets

    @property
    def fields(self):
        if len(self.data) == 0:
            return []
        
        return [x for x in self.data[0].keys()]
