#added this after to screen for errors 
# Function to get a valid integer input
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt)) #checks if input is int
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Function to get a valid string input
def get_valid_string(prompt):
    while True:
        value = input(prompt).lower() 
        if value.isalpha(): #checks it's a string
            return value
        else:
            print("Invalid input. Please enter a valid string.")

# Asking user input while calling function
city_flight = get_valid_string("What city are you flying to? ")
num_nights = get_valid_int("How many nights are you staying? ")
rental_days = get_valid_int("How many days will you be hiring a car? ")


#asking user input
#city_flight = input("What city are you flying to? ").lower()
#um_nights = int(input("How many nights are you staying? "))
#rental_days = int(input("How many days will you be hiring a car? "))

#decided to use dictionaries to make sets of city vs price for stuff to practice from last lesson 
city = {
    "milan" : 194.50,
    "london" : 165.50,
    "berlin" : 150.35,
    "new york" : 1112.75,
    "lagos" : 1055.50,
    "seoul" : 1074.60,
    "tokyo" : 1280.40,
    "beijin" : 178.47
}

hotels = {
    "milan" : 94.50,
    "london" : 65.50,
    "berlin" : 50.35,
    "new york" : 112.75,
    "lagos" : 155.50,
    "seoul" : 174.60,
    "tokyo" : 180.40,
    "beijin" : 78.47
}

cars = {
    "milan" : 14.50,
    "london" : 25.50,
    "berlin" : 10.35,
    "new york" : 12.75,
    "lagos" : 15.50,
    "seoul" : 74.60,
    "tokyo" : 80.40,
    "beijin" : 8.47
}

#used to calculate hotel prices
def hotel_cost (num_nights):
    if city_flight in hotels: #checks if input is in dictionary 
        total_hotel_cost = round((num_nights * hotels[city_flight]),2)
        print(f"The total hotel cost is £{total_hotel_cost}")
    else: #if not return 0 and print a sorry 
        total_hotel_cost = 0
        print("Hotel unavailable")
    return(total_hotel_cost)

#used to calculate flight costs 
def plane_cost (city_flight):
    if city_flight in city:
        cost_flight = city[city_flight] #checks if city is in dic and then prints flight price 
        print(f"The total flight cost is £{cost_flight}")
    else:
        cost_flight = 0
        print("Flight unavailable")
    return(cost_flight)

#used to calculate car rental 
def car_rental (rental_days):
    if city_flight in cars: 
        car_cost = round((cars[city_flight] * rental_days),2)
        print(f"The total care rental cost is £{car_cost}")
    else:
        car_cost = 0
        print("car rental unavailable")
    return(car_cost)

#assigns whatever the function returns to a value, also calls above functions and inputs the values 
hoteltotal = hotel_cost (num_nights)
planetotal = plane_cost (city_flight)
cartotal = car_rental (rental_days)

#calculates total costs 
def holiday_cost (hotel,plane,car):
    total_cost = (hotel + plane + car)
    print(f"The total overall cost is £{total_cost}")
    return(total_cost)

#calls last function an dinputs needed values 
holiday_cost (hoteltotal,planetotal,cartotal)
