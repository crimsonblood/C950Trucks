# TODO Update for submission
import csv
import datetime

# Read WGUPS Distance Table and WGUPS Name Table to determine distances
with open('./datacsv/WGUPS Distance Table.csv') as file:
    distance_csv = list(csv.reader(file, delimiter=','))

with open('./datacsv/WGUPS Name Table.csv') as namefile:
    name_csv = list(csv.reader(namefile, delimiter=','))

    # Get address for package
    # Space-time complexity -> O(1)
    def get_address():
        return name_csv

    # Calculate total distance from csv distance table
    # Space-time complexity -> O(1)
    def get_distance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return total + float(distance)

    # Calculate current distance from csv distance table
    # Space-time complexity -> O(1)
    def get_current_distance(row, col):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return float(distance)

    # Calculate total distance for the given truck list
    # Space-time complexity -> O(n)
    def get_time(distance, truck_list):
        future_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(future_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_list:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        return total


    # these lists represent the sorted trucks that are put in order of efficiency in the function below

    # Arrays to store truck and truck indices lists
    trucks = [[], [], []]
    trucks_indices = [[], [], []]

    # Insert 0 for the first index of each index list
    for truck_num in range(3):
        trucks_indices[truck_num].insert(0, '0')

    # This algorithm uses the 'greedy approach' in order to determine the best location to visit
    # next based on the current location. This algorithm recursively determines the best location
    # to visit based on the current location. Its use results in sorted delivery lists to decrease
    # total mileage.

    # This algorithm has three parameters: List of packages, truck number, and current location of the truck
    # It works in the following fashion:

    # The first for loop is used to find the shortest distance to the next location. The shortest value will change
    # until a minimum value is found.

    # The second for loop iterates through all of the packages to determine the closest one to add to the specified
    # truck list. The selected package is removed from the list and then the current location moves to the next
    # location determined by the first for loop. A recursive call is made at the end of this loop to look for the
    # next optimal location with the shortened list. Recursive calls will be made until the base case is met, which
    # terminates the function and returns an empty list.

    # Space-Time Complexity -> O(N^2)
    def get_shortest_route(delivery_list, num, curr_location):
        if not len(delivery_list):
            return delivery_list

        lowest_value = 1000
        location = 0

        for i in delivery_list:
            value = int(i[1])
            if get_current_distance(curr_location, value) <= lowest_value:
                lowest_value = get_current_distance(
                    curr_location, value)
                location = value

        for i in delivery_list:
            if get_current_distance(curr_location, int(i[1])) == lowest_value:
                trucks[num].append(i)
                trucks_indices[num].append(i[1])
                delivery_list.pop(delivery_list.index(i))
                curr_location = location
                get_shortest_route(delivery_list, num, curr_location)

    # Returns specified truck list
    # Space-time complexity -> O(1)
    def get_truck(num):
        return trucks[num]

    # Returns specified truck indices list
    # Space-time complexity -> O(1)
    def get_truck_indices(num):
        return trucks_indices[num]
