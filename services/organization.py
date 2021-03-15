#!/usr/bin/env python3

from config import Config
from utilities import read_file_json
from .base import Base

class Organization(Base):

    def __init__(self):
        self.data = []
        self.orgs_by_ids = {}

    def load_data(self):
        self.data = read_file_json(Config.ORGANIZATION_DATA)
        self.orgs_by_ids = self.get_orgs_by_id()
    
    def get_orgs_by_id(self):
        orgs = {}
        if len(self.data) == 0:
            return orgs
        
        for org in self.data:
            if "_id" not in org:
                continue 

            orgs[org["_id"]] = org    
        
        return orgs
    
    @property
    def fields(self):
        if len(self.data) == 0:
            return []
        
        return [x for x in self.data[0].keys()]

    def finds(self, term, value):
        if len(self.data) == 0:
            return []
        
        organizations = []
        for org in self.data:
            if term not in org:
                continue

            if type(org[term]).__name__ == "list":
                if value in org[term]:
                    organizations.append(org)
                    continue
            
            if str(org[term]) == str(value):
                organizations.append(org)

        return organizations