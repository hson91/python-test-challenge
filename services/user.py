#!/usr/bin/env python3

from config import Config
from utilities import read_file_json
from .base import Base

class User(Base):

    def __init__(self):
        self.data = []
        self.userByOrg = {}
        self.userById = {}

    def load_data(self):
        self.data = read_file_json(Config.USER_DATA)
        self.get_user_by_orgs()
    
    def get_user_by_orgs(self):
        '''
            convert user data to organization dict with key is 'organization_id' \n 
            and user dict with key is '_id'
        '''
        orgs = {}
        users = {}
        if len(self.data) == 0:
            return orgs
        
        for user in self.data:
            if "organization_id" not in user:
                continue 

            if user["organization_id"] not in orgs:
                orgs[user["organization_id"]] = []
            
            orgs[user["organization_id"]].append(user)
            users[user["_id"]] = user
        
        self.userByOrg = orgs
        self.userById = users
    
    def finds(self, term, value):
        if len(self.data) == 0:
            return []
        
        users = []
        for user in self.data:
            if term not in user:
                continue

            if type(user[term]).__name__ == "list":
                if value in user[term]:
                    users.append(user)
                    continue
            
            if str(user[term]) == str(value):
                users.append(user)

        return users

    @property
    def fields(self):
        if len(self.data) == 0:
            return []
        
        return [x for x in self.data[0].keys()]