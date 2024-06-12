print("🌸Project 1 - Building a Garden🌸")

length = float(input("Enter the length of the garden in feet: "))
width = float(input("Enter the width of the garden in feet: "))

print("Our inventory of plants:")
print("1. Roses - $1.00 per square foot")
print("2. Carnation - $2.00 per square foot")
print("3. Sunflowers - $3.00 per square foot")

choice = int(input("Enter the number of the plant you want to choose (1, 2, or 3): "))
if choice == 1:
    plant_name = "Roses"
    plant_price = 1.00
elif choice == 2:
    plant_name = "Carnation"
    plant_price = 2.00
elif choice == 3:
    plant_name = "Sunflowers"
    plant_price = 3.00
else:
    print("Invalid choice. Please choose a valid plant.")
    exit()

quantity = float(input(f"Good choice! How many {plant_name} do you want? "))

garden = length * width
print(f"The area of the garden is {garden} square feet.")
print(f"The total area of {plant_name} is {quantity} square feet.")

plant_cost = quantity * plant_price
print(f"The total cost of {quantity} {plant_name} is ${plant_cost:.2f}")
total_cost = plant_cost
print(f"The grand total is ${total_cost:.2f}.")

