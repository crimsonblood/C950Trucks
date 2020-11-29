import packageDistance
import packageImport

# Empty lists for deliveries and distances
deliveries = [[], [], []]
distances = [[], [], []]

# First, second, and third leave times
leave_times = [['8:00:00'], ['9:10:00'], ['11:00:00']]


# Update delivery start time to the set truck leave time
# Space-time complexity -> O(N)
def update_delivery_time(delivery_list, leave_time, delivery):
    for i, v in enumerate(delivery_list):
        delivery_list[i][9] = leave_time[0]
        delivery.append(delivery_list[i])


# Compare truck addresses to address list
# Space-time complexity -> O(N^2)
def compare_address(delivery, truck_distances):
    for i, o in enumerate(delivery):
        for n in packageDistance.get_address():
            if o[2] == n[2]:
                truck_distances.append(o[0])
                delivery[i][1] = n[0]


# Calculate total distance of the first truck and distance of each package
# Space-time complexity -> O(n)
def calculate_distance(truck_index, leave_time, truck_list, delivery):
    td = 0
    for i in range(len(truck_index)):
        try:
            td = packageDistance.get_distance(int(truck_index[i]), int(truck_index[i + 1]), td)

            dp = packageDistance.get_time(packageDistance.get_current_distance(int(truck_index[i]), int(truck_index[i + 1])),
                                          leave_time)

            truck_list[i][10] = (str(dp))
            packageImport.get_hashmap().update(int(truck_list[i][0]), delivery)
        except IndexError:
            pass
    return td


# Get distance of all packages
# Space-time complexity O(N)
def total_distance():
    td = 0
    # Loops through all three truck lists in order to calculate the total distance traveled
    for i in range(3):
        # Update delivery start time to the set truck leave time
        update_delivery_time(packageImport.get_deliveries(i), leave_times[i], deliveries[i])
        # Compare truck addresses to address list
        compare_address(deliveries[i], distances[i])
        # Calls sorting algorithm
        packageDistance.get_shortest_route(deliveries[i], i, 0)
        # Calculate total distance of the first truck and distance of each package
        td += calculate_distance(packageDistance.get_truck_indices(i), leave_times[i], packageDistance.get_truck(i),
                                 deliveries[i])

    return td
