# Name: Evan Blanke
# Student ID: #001236257
from packageImport import get_hashmap
from schedule import total_distance
import datetime


# Function for converting a string into a datetime object
# Space-time complexity -> O(1)
def convert_time(time):
    (h, m, s) = time.split(':')
    return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


input_string = """Please select an option below or type 'exit' to exit: 
    1. Display all packages at time
    2. Lookup specific package

 """


class Main:
    # Calculates the total distance traveled to deliver all packages and displays it
    route_total_distance = total_distance()
    print('-' * 20)
    print('WGUPS Routing Program')
    print(f'Route was completed in {route_total_distance:.2f} miles.\n')
    print('-' * 20)

    # Displays the main menu option
    # Users can select 1 to view all packages at a select time
    # Users can select 2 to view a specific package at a select time
    menu = input(input_string)

    # Main menu loop
    while menu != 'exit':
        # Option 1: Display all packages at select time
        # Space-time complexity -> O(N)
        if menu == '1':
            try:
                # Asks user for time formatted HH:MM:SS to check package status at that time
                input_time = input('Enter a time (HH:MM:SS): ')
                delta_input_time = convert_time(input_time)

                # Loops through all packages and displays delivery status information
                # Space-time complexity ->  O(N)
                for package_index in range(1, 41):
                    try:
                        # Initialize time variables
                        start_time = get_hashmap().get_value(str(package_index))[9]
                        end_time = get_hashmap().get_value(str(package_index))[10]

                        delta_start_time = convert_time(start_time)
                        delta_end_time = convert_time(end_time)
                    except ValueError:
                        pass

                    Status = 'Status: '

                    # Packages at hub
                    if delta_start_time >= delta_input_time:
                        Status += 'At Hub, Leaving at ' + start_time
                    # Packages that have left
                    elif delta_start_time <= delta_input_time:
                        # Not delivered
                        if delta_input_time < delta_end_time:
                            Status += 'Out for Delivery, Arriving at ' + end_time
                        # Already Delivered
                        else:
                            Status += 'Delivered at ' + end_time

                    print('Package ID: ', get_hashmap().get_value(str(package_index))[0], ', ', Status)
                print('DONE!\n\n')
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid input')
                exit()
            menu = "*"
        # Option 2: Display a specific package at a select time
        elif menu == '2':
            try:
                # Initialize time variables
                lookup_id = input('Enter a valid package ID: ')
                start_time = get_hashmap().get_value(str(lookup_id))[9]
                end_time = get_hashmap().get_value(str(lookup_id))[10]
                # Asks user for time formatted HH:MM:SS to check package status at that time
                input_time = input('Enter a time (HH:MM:SS): ')

                # Convert times to datetime object
                delta_input_time = convert_time(input_time)
                delta_start_time = convert_time(start_time)
                delta_end_time = convert_time(end_time)

                # Packages at hub
                if delta_start_time >= delta_input_time:
                    truck_status = 'At Hub'
                    delivery_status = 'Leaves at ' + start_time

                # Determine which packages have left but have not been delivered
                elif delta_start_time <= delta_input_time:
                    if delta_input_time < delta_end_time:
                        truck_status = 'In transit'
                        delivery_status = 'Left at ' + start_time

                    # Determine which packages have already been delivered
                    else:
                        truck_status = 'Left at ' + start_time
                        delivery_status = 'Delivered at ' + end_time

                # Print package's current info
                print(
                    '\nPACKAGE\n'
                    f'  Package ID: {get_hashmap().get_value(str(lookup_id))[0]}\n'
                    f'  Street address: {get_hashmap().get_value(str(lookup_id))[2]}\n'
                    f'  Delivery Deadline: {get_hashmap().get_value(str(lookup_id))[6]}\n'
                    f'  Package weight: {get_hashmap().get_value(str(lookup_id))[7]}\n'
                    '   Shipping Status:\n'
                    f'      Truck: {truck_status}\n'
                    f'      Delivery: {delivery_status}\n'
                )
                print('DONE!\n\n')
            except ValueError:
                print('Invalid input')
                exit()
            menu = "*"
        # exit
        elif menu == 'exit':
            exit()
        # restart menu after successfully completing an option
        elif menu == '*':
            menu = input(input_string)

        else:
            print('Invalid input')
            exit()
