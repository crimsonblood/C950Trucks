#TODO Update for submisison
import csv
from hashmap import HashMap

# Read CSV files
with open('./datacsv/WGUPS Package File.csv') as file:
    package_csv = csv.reader(file, delimiter=',')

    hashmap = HashMap()  # Create an instance of HashMap class
    first_delivery = []  # first truck delivery
    second_delivery = []  # second truck delivery
    final_delivery = []  # final truck delivery

    # Insert values from csv file into key/value pairs of the hash table -> O(n)
    for row in package_csv:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        mass = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'

        package = [id, address_location, address, city, state, zip, delivery, mass, note, delivery_start,
                   delivery_status]

        # Conditional statements to determine which truck a package should be located and
        # put these packages into a nested list for quick indexing

        # Correct incorrect package details
        if '84104' in package[5] and '10:30' not in package[6]:
            final_delivery.append(package)
        if 'Wrong address listed' in package[8]:
            package[2] = '410 S State St'
            package[5] = '84111'
            final_delivery.append(package)
        # First truck's first delivery
        if package[6] != 'EOD' and ('Must' in package[8] or 'None' in package[8]):
            first_delivery.append(package)

        # Second truck's delivery
        if 'Can only be' in package[8] or 'Delayed' in package[8]:
            second_delivery.append(package)

        # Check remaining packages
        if package not in first_delivery and package not in second_delivery and package not in final_delivery:
            second_delivery.append(package) if len(second_delivery) < len(final_delivery) else final_delivery.append(
                package)

        # Insert value into the hash table
        hashmap.insert(id, package)

    # Get packages on the first delivery -> O(1)
    def get_first_delivery():
        return first_delivery

    # Get packages on the second delivery -> O(1)
    def get_second_delivery():
        return second_delivery

    # Get packages on the final delivery -> O(1)
    def get_final_delivery():
        return final_delivery

    # Get full list of packages -> O(1)
    def get_hash_map():
        return hashmap
