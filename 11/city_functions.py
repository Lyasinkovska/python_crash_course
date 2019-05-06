from location import location_name

print("If you want to quit, please enter 'q'.")


while True:
    city = input("Enter your city name: ")
    if city == 'q':
        break

    country = input("Enter your country name: ")
    if country == 'q':
        break
    your_location = location_name(city, country)
    print(your_location)

