import csv
from hashmap import HashMap

# Reads WGUPS Package File to import package details
with open('./datacsv/WGUPS Package File.csv') as file:
    package_csv = csv.reader(file, delimiter=',')

    hashmap = HashMap()  # Creates an object of HashMap
    deliveries = [[], [], []]
    delivery_one = []  # List for delivery one on the first truck
    delivery_two = []  # List for delivery two on the second truck
    delivery_three = []  # List for delivery three on the final truck

    # Insert values from csv file into key/value pairs of the hash table
    # Space-time complexity -> O(n)
    for row in package_csv:
        package_id = row[0]
        address_location = ''
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        deadline = row[5]
        weight = row[6]
        notes = row[7]
        delivery_start = ''
        delivery_end = ''

        package = [package_id, address_location, address, city, state, zip_code, deadline, weight, notes,
                   delivery_start, delivery_end]

        # Conditional statements to determine incorrect package details and to update them
        if '84104' in package[5] and '10:30' not in package[6]:
            deliveries[2].append(package)
        if 'Wrong address listed' in package[8]:
            package[2] = '410 S State St'
            package[5] = '84111'
            deliveries[2].append(package)

        # Adding specific packages to delivery lists
        # Delivery One
        if package[6] != 'EOD' and ('Must' in package[8] or 'None' in package[8]):
            deliveries[0].append(package)
        # Delivery Two
        if 'Can only be' in package[8] or 'Delayed' in package[8]:
            deliveries[1].append(package)

        # Puts remaining packages into delivery lists
        if package not in deliveries[0] and package not in deliveries[1] and package not in deliveries[2]:
            if len(deliveries[1]) < len(deliveries[2]):
                deliveries[1].append(package)
            else:
                deliveries[2].append(package)

        # Insert package value into hash table
        hashmap.insert(package_id, package)


# Returns packages for the specified delivery number
# Space-time complexity -> O(1)
def get_deliveries(num):
    return deliveries[num]


# Returns full list of packages
# Space-time complexity -> O(1)
def get_hashmap():
    return hashmap
