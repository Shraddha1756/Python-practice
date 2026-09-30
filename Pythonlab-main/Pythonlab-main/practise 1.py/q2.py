n = int(input("Enter total number of seats: "))

seats = []
for i in range(n):
    x = int(input("Enter status of seat " + str(i + 1) + ": "))
    seats.append(x)

group = int(input("Enter number of people: "))

found = False

for i in range(n - group + 1):
    if all(seats[i + j] == 0 for j in range(group)):
        # Book the seats
        for j in range(group):
            seats[i + j] = 1

        # Seat numbers start from 1
        allocated = tuple(range(i + 1, i + group + 1))

        print("Allocated seat numbers:", allocated)
        print("Updated seat list:", seats)

        found = True
        break

if not found:
    print("Consecutive seats not available")
    print("Original seat list:", seats)
