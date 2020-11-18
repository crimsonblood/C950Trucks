# This is a sample Python script.
from packageImport import get_hash_map
from packages import total_distance
import datetime

class Main:
    print(get_hash_map().get_value(str(38)))

    print('-' * 20)
    print('WGUPS Routing Program')
    print('-' * 20)
    print(f'Route was completed in {total_distance():.2f} miles.\n')
    #route total distance print

    n = input("""Please select an option below or type 'exit' to exit: 
    1. Display all packages at time
    2. Lookup specific package
    """)

    while n != 'exit':
        #option 1: display all packages at time
        if n == '1':
            try:
                input_time = input('Enter a time (HH:MM:SS): ')
                (hrs, mins, secs) = input_time.split(':')
                convert_user_time = datetime.timedelta(int(hrs), int(mins), int(secs))

                # Complexity ->  O(n^2)
                for count in range(1, 40):
                    print(get_hash_map().get_value(str(count)))
                    try:
                        first_time = get_hash_map().get_value(str(count))[9]
                        second_time = get_hash_map().get_value(str(count))[10]
                        (hrs, mins, secs) = first_time.split(':')
                        convert_first_time = datetime.timedelta(int(hrs), int(mins), int(secs))
                        (hrs, mins, secs) = second_time.split(':')
                        convert_second_time = datetime.timedelta(int(hrs), int(mins), int(secs))
                    except ValueError:
                        pass

                    # Determine which packages have left the hub
                    if convert_first_time >= convert_user_time:
                        get_hash_map().get_value(str(count))[10] = 'At Hub'
                        get_hash_map().get_value(str(count))[9] = 'Leaves at ' + first_time

                        # Print package's current info
                        print(
                            f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                            f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
                        )

                    # Determine which packages have left but have not been delivered
                    elif convert_first_time <= convert_user_time:
                        if convert_user_time < convert_second_time:
                            get_hash_map().get_value(str(count))[10] = 'In transit'
                            get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time

                            # Print package's current info
                            print(
                                f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                                f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
                            )

                        # Determine which packages have already been delivered
                        else:
                            get_hash_map().get_value(str(count))[10] = 'Delivered at ' + second_time
                            get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time

                            # Print package's current info
                            print(
                                f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                                f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
                            )


            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid input')
                exit()

        #option 2: display specific package
        elif n == '2':
            try:
                print('Option 2 stuff')
            except ValueError:
                print('Invalid input')
                exit()

        #exit
        elif n == 'exit':
            exit()

        else:
            print('Invalid input')
            exit()