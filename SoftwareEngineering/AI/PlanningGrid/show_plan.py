import json

# Open the JSON file and read its contents
with open('Plan.json') as f:
    data = json.load(f)

# Print the JSON data
output = []
table = data['lessons']['table']
for m in table:
    for l in m:
        x = l.get('delivery')
        if x:
            output.append ((x['role'],x['milestone'],x['deliverable'],x['details']))

open('Plan2.json', 'w').write(json.dumps(output, indent=4))

