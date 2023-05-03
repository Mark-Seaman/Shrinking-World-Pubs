import json
import pandas as pd


def read_json(infile):
    with open(infile) as f:
        return json.load(f)


def write_json(outfile, json):
    open(outfile, 'w').write(json.dumps(json, indent=4))


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
    # write_json(outfile, output)


# Define the JSON data as a Python list

def create_table_from_JSON(infile, outfile):
    # Open the JSON file and read its contents
    with open(infile) as f:
        json_data = json.load(f)

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


def normalize_json(infile, outfile):
    # Open the JSON file and read its contents
    with open(infile) as f:
        data = json.load(f)

    # Convert the JSON data to a pandas DataFrame
    df = pd.json_normalize(json_data)

    # Save the DataFrame to a CSV file
    df.to_csv(outfile, index=False)


def perform_tasks():
    json = read_json('Plan2.json')
    print(json)
    # convert_JSON_records('Plan.json', 'Plan2.json')
    # normalize_json('Plan2.json', , 'Plan3.json')
    # table = create_table_from_JSON('Plan2.json', 'Plan3.md')
    # print_table(table)

# # convert JSON data to Python list
# data = json.loads(json_data)


perform_tasks()

