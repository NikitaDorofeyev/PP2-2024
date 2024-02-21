import json

with open ("sample-data.json") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))