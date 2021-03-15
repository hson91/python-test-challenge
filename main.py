#!/usr/bin/env python3
import sys
import json
from services import Services
from utilities import prints_data, print_fiels

srv = Services()
srv.load_data()

break_line = "\n------------------------------------------------------------"

def read_command(message="")->(str, bool):
    cmd = input(message).strip()
    if cmd == "quit":
        return "", True

    return cmd, False

def handle_cmd(cmd)->bool:
    try:
        option = int(cmd)
        
        if option == 1:
            return action_search()
        
        if option == 2:
            return action_searchable_fields()

    except Exception as e:
        print(e)
    
    return False

def action_search()->bool:
    text_options = "Select 1) Users, 2) Tickets, 3) Organizations or type 'quit' to exit: "
    cmd, is_quit = read_command(text_options)
    if is_quit:
        return True
    
    option = int(cmd)
    if option not in [1, 2, 3]:
        return action_search()
    
    term, is_quit = read_command("Enter search term: ")
    if is_quit:
        return True

    value, is_quit = read_command("Enter search value: ")
    if is_quit:
        return True

    if option == 1:
        searching_users(term, value)
        return
    
    if option == 2:
        searching_tickets(term, value)
        return

    if option == 3:
        searching_organizations(term, value)
        return

    return False

def searching_users(term, value):
    print("\nSearching users for {term} with a value of {value}".format(term=term, value=value))
    users = srv.find_users(term, value)
    prints_data(users)

def searching_tickets(term, value):
    print("\nSearching tickets for {term} with a value of {value}".format(term=term, value=value))
    tickets = srv.find_tickets(term, value)
    prints_data(tickets)

def searching_organizations(term, value):
    print("\nSearching organizations for {term} with a value of {value} \n".format(term=term, value=value))
    organizations = srv.find_organizations(term, value)
    prints_data(organizations)

def action_searchable_fields()->bool:
    print(break_line)
    print("\nList of searchable fields for the user")
    print_fiels(srv.User.fields)
    
    print(break_line)
    print("\nList of searchable fields for the ticket")
    print_fiels(srv.Ticket.fields)
    
    print(break_line)
    print("\nList of searchable fields for the organization")
    print_fiels(srv.Organization.fields)

    return False

def main():
    text_welcome = """\nType 'quit' to exit at any time, Press 'Enter' to continue \n
        Select search options:
        * Press 1 to search
        * Press 2 to view a list of searchable fields
        * Type 'quit' to exit \n
    """

    while True:
        print(text_welcome)
        cmd, is_quit = read_command("Select: ")
        if is_quit :
            sys.exit()
        
        if handle_cmd(cmd):
            sys.exit()

if __name__ == "__main__":
    main()
        
