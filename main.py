# GOOD
from packageImport import get_hash_map
from packages import total_distance
import datetime


def convert_time(time):
    (hrs, mins, secs) = time.split(':')
    return datetime.timedelta(int(hrs), int(mins), int(secs))


class Main:
    print('-' * 20)
    print('WGUPS Routing Program')
    print(f'Route was completed in {total_distance():.2f} miles.\n')
    print('-' * 20)
    # route total distance print

    input = input("""Please select an option below or type 'exit' to exit: 
    1. Display all packages at time
    2. Lookup specific package
    
:: """)

    while input != 'exit':
        # option 1: display all packages at time
        if input == '1':
            try:
                input_time = input('Enter a time (HH:MM:SS): ')
                delta_input_time = convert_time(input_time)

                # Complexity ->  O(n^2)
                for count in range(1, 40):
                    try:
                        start_time = get_hash_map().get_value(str(count))[9]
                        end_time = get_hash_map().get_value(str(count))[10]

                        delta_start_time = convert_time(start_time)
                        delta_end_time = convert_time(end_time)
                    except ValueError:
                        pass

                    # Determine which packages have left the hub
                    if delta_start_time >= delta_input_time:
                        # Print package's current info
                        print(
                            f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                            f'Delivery status: At Hub, Leaving at {start_time}'
                        )

                    # Determine which packages have left but have not been delivered
                    elif delta_start_time <= delta_input_time:
                        if delta_input_time < delta_end_time:
                            # Print package's current info
                            print(
                                f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                                f'Delivery status: Out for Delivery at {start_time}'
                            )

                        # Determine which packages have already been delivered
                        else:
                            # Print package's current info
                            print(
                                f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                                f'Status: Delivered at {end_time}'
                            )
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid input')
                exit()

        # option 2: display specific package
        elif input == '2':
            try:
                count = input('Enter a valid package ID: ')
                start_time = get_hash_map().get_value(str(count))[9]
                end_time = get_hash_map().get_value(str(count))[10]
                input_time = input('Enter a time (HH:MM:SS): ')

                # convert times to datetime object
                delta_input_time = convert_time(input_time)
                delta_start_time = convert_time(start_time)
                delta_end_time = convert_time(end_time)

                # Determine which packages have left the hub
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
                    f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
                    f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
                    f'Delivery Deadline: {get_hash_map().get_value(str(count))[6]}\n'
                    f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
                    'Shipping Status:\n'
                    f'  Truck: {truck_status}\n'
                    f'  Delivery: {delivery_status}\n'
                )
            except ValueError:
                print('Invalid input')
                exit()

        # exit
        elif input == 'exit':
            exit()

        else:
            print('Invalid input')
            exit()
