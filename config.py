#!/usr/bin/env python3

import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    USER_DATA=basedir + "/data/users.json"
    TICKET_DATA=basedir + "/data/tickets.json"
    ORGANIZATION_DATA=basedir + "/data/organizations.json"