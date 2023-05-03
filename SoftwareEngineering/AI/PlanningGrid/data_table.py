import json
import pandas as pd
import csv
from pathlib import Path


def read_json(infile):
    with open(infile) as f:
        return json.load(f)


def write_json(outfile, table):
    open(outfile, 'w').write(json.dumps(table, indent=4))


def convert_JSON_records(infile, outfile):

    data = read_json(infile)

    output = []
    table = data['lessons']['table']
    for m in table:
        for l in m:
            x = l.get('delivery')
            if x:
                output.append ((x['role'],x['milestone'],x['deliverable'],x['details']))
                print(x['role'],x['milestone'],x['deliverable'])
    write_json(outfile, output)            
    # Path(outfile).write_text(output)
    # open('Plan2.json', 'w').write(json.dumps(output, indent=4))



# Define the JSON data as a Python list
def create_table_from_JSON(json_data):
    
    # initialize the table with empty rows
    table = [[[], [], [], []] for _ in range(7)]

    # iterate over each item in the JSON data
    for item in json_data:
        role= item[0]
        milestone = item[1]
        print(milestone, role, item[2])
        deliverable = item[2]
        details = item[3]
        
        # add the deliverable and details to the table
        table[milestone][role].append(deliverable)
        table[milestone][role].append(details)
    return table


def print_table(table):
    for row in table:
        # print(row)
        for c in row:
            print('    ', c[0])
            for d in c[1]:
                print('        ', d)


def load_data_frame():

    data = [
        [0, 0, "Project Charter", ["Business proposition", "Project scope & budget", "Client communication", "Sprint Planning meetings"]],
        [1, 0, "Technology selection", ["Select Development Tools", "Infrastructure - Frameworks & Tools", "Setup Guide", "Create \"Hello World\"", "Decide on App deployment"]],
        [2, 0, "Version control", ["Setup Github account", "Setup Github Pages repository", "Decide how to publish your project docs", "User Guide for development workflow"]]
    ]

    df = pd.DataFrame(data, columns=["row", "col", "Deliverable", "Details"])
    table_html = df.to_html(index=False)

    print(table_html)


def save_html(outfile, json_data):
    df = pd.DataFrame(json_data, columns=["row", "col", "Deliverable", "Details"])
    table_html = df.to_html(index=False)
    Path(outfile).write_text(table_html)


def save_csv(outfile, json_data):
    df = pd.DataFrame(json_data, columns=["row", "col", "Deliverable", "Details"])
    df.to_csv(outfile, index=False)


def normalize_json(infile, outfile):

    json_data = read_json(infile)

    # Convert the JSON data to a pandas DataFrame
    df = pd.json_normalize(json_data)


def save_markdown(infile, outfile):
    df = pd.read_csv(infile)
    df.to_markdown(outfile, index=False)


def perform_tasks():
    # data = read_json('Plan.json')
    # data = convert_JSON_records(data)
    # write_json('Plan2.json', table)

    data = read_json('Plan2.json')
    # save_csv('Plan3.csv', data)
    # save_html('Plan3.html', data)

    # print(json)
    # normalize_json('Plan2.json', 'Plan3.csv')
    # load_data_frame()

    # with open('Plan3.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         print(row)

    save_markdown('Plan3.csv', 'Plan4.md')
    # table = create_table_from_JSON(data)
    # print_table(table)


perform_tasks()

