# Four functions calculate or sort the three costs and the overall final cost

def hotel_cost(hotel_price, num_nights):
    return int(hotel_price) * int(num_nights)

def plane_cost(city_flight):
    if city_flight == "r":
        return 1989
    elif city_flight == "a":
        return 1425
    elif city_flight == "b":
        return 899
    elif city_flight == "l":
        return 600

def car_rental(rental_days, daily_rental_cost):
    return int(rental_days) * daily_rental_cost

def holiday_cost(hotel_price, num_nights, city_flight, rental_days, daily_rental_cost):

    return hotel_cost(hotel_price, num_nights) + plane_cost(city_flight) \
    + car_rental(rental_days, daily_rental_cost)

# User inputs inside while loops checks user input for letter, 
# special character and whitespace before taking it to the function
daily_rental_cost = 50
print("\nThis is a holiday calculator that is going to calculate \
      the total cost of your holiday")
while True:
    hotel_price = input("\nEnter the cost of your hotel per night ")
    if hotel_price.isdigit():
        break
    else:
        print("That was not a number, please try again")

while True:
    num_nights = input("\nEnter the number of nights you will be staying ")
    if num_nights.isdigit():
        break
    else:
        print("That was not a number, please try again")

print("\nDuring your holiday you will need to hire a car to travel any distance")
while True:
    rental_days = input("\nEnter how many days you would like to hire a car for ")
    if rental_days.isdigit():
        break
    else:
        print("That was not a number, please try again")
    
print("\nThe four options for where you are flying to are Rome, Athens, Budapest and London")
while True:
    city_flight = input("\nEnter which city you are flying to. R for Rome, \
                        A for Athens, B for Budapest and L for London ").lower()
    if city_flight == "r" or city_flight == "a" or city_flight == "b" or city_flight == "l":
        break
    else:
       print("\nYou have not typed a valid input, please try again")

# functions stored as variables to be formatted into whole sentences within print statements
hotel = hotel_cost(hotel_price, num_nights)
plane = plane_cost(city_flight)
car = car_rental(rental_days, daily_rental_cost)
total_holiday_cost = holiday_cost \
(hotel_price, num_nights, city_flight, rental_days, daily_rental_cost)
print("\n\nYour holiday costs are as follows:\n\nHotel Cost = £{}\n \
      Return Flight Plane Costs = £{}\nCar Rental Costs = £{}".format(hotel, plane, car))
print("\n\nThe total cost of your holiday = £{}. \
      Have a nice holiday!\n".format(total_holiday_cost))
