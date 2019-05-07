def location_name(city, country, population=""):
    if population:
        location = city + ", " + country + " - population " + population
    else:
        location = city + ", " + country
    return location.title()