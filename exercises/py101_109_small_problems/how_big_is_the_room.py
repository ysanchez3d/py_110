# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

def print_room_size(length, width):
    square_meters = length * width
    square_feet = square_meters * 10.7639

    print(f"Square Meters: {square_meters:.2f}")
    print(f"Square Feet: {square_feet:.2f}")


print("Enter the length and width of a room in meters:")
length = float(input("Length: "))
width = float(input("Width: "))

print_room_size(length, width)