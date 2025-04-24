def print_rooms(rooms, vacuum_location):
    for i, status in enumerate(rooms):
        print(f"Room {'A' if i == 0 else 'B'}: {status} {'(V)' if i == vacuum_location else ''}")

def main():
    rooms = []
    rooms.append(input("Enter the status of Room A (C for Clean, D for Dirty): ").strip().upper())
    rooms.append(input("Enter the status of Room B (C for Clean, D for Dirty): ").strip().upper())
    
    if any(status not in ['C', 'D'] for status in rooms):
        print("Invalid input! Use 'C' for Clean or 'D' for Dirty.")
        return

    initial_position = input("Enter the initial position of the vacuum cleaner (A or B): ").strip().upper()
    if initial_position not in ['A', 'B']:
        print("Invalid input! Use 'A' or 'B'.")
        return

    vacuum_location = 0 if initial_position == 'A' else 1
    print("\nInitial State:")
    print_rooms(rooms, vacuum_location)

    for step in range(5):
        print(f"\nStep {step + 1}:")
        if rooms[vacuum_location] == 'D':
            print(f"Cleaning Room {'A' if vacuum_location == 0 else 'B'}")
            rooms[vacuum_location] = 'C'
        else:
            print(f"Room {'A' if vacuum_location == 0 else 'B'} is already clean.")
            vacuum_location = 1 - vacuum_location
            print(f"Moving to Room {'A' if vacuum_location == 0 else 'B'}")

        print_rooms(rooms, vacuum_location)
        if all(status == 'C' for status in rooms):
            print("\nBoth rooms are clean. Ending function.")
            break

if __name__ == "__main__":
    main()
