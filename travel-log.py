# 100 Days of Python
# Day 9.2 - Travel Log
# Practice with dictionaries
# Sarah Vigstol
# 5/27/21

travelLog = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def addNewCountry(country, visits, cities):
    travelLog.append(
    {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    )
# alternative code solution
# def addNewCountry(countryVisted, timesVisited, citiesVisited)
#   newCountry = {}
#   newCountry["country"] = countryVisted
#   newCountry["visits"] = timesVisited
#   newCountry["cities"] = citiesVisited
#   travelLog.append(newCountry)

addNewCountry("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travelLog)
