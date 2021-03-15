#!/usr/bin/env python3

import json

def read_file_json(path):
    try:
        with open(path) as json_file:
            return json.load(json_file)
    except Exception as e:
        print(e)
    
    return []

def prints_data(data=[]):
    try:
        for item in data:
            print("---------------------------------------------------------- \n")
            for k, v in item.items():
                
                if type(v).__name__ == "list":
                    for index in range(len(v)):
                        print("+ {k}-{index}\t\t{v}".format(k=k, index=index, v=v[index]))
                    continue

                print("{k}\t\t\t{v}".format(k=k, v=v))
    except Exception as e:
        print(e)


def print_fiels(fields=[]):
    try:
        for field in fields:
            print(field)
    except Exception as e:
        print(e)