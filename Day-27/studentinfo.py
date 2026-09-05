import json

# with open('data.json', 'r') as file:
#     data = json.load(file)

# print(data)
# data['username'] = 'Venkat'
# data['batch'] = 7
# data['skills'].append('MySql')

# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)


student = {
    'name': 'Bharat',
    'course': 'PFS',
    'batch': 'batch-5'
}

json_data = json.dumps(student)
print(json_data)
print(type(json_data))

student = json.loads(json_data)
print(student)
print(type(student))