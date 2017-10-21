import amadeus
from amadeus import Hotels

hotels = Hotels('k8aoh1A2jdvL2FzowmGrM30GOffQzIbJ')
resp = hotels.search_airport(
    check_in='2017-12-08',
    check_out='2017-12-13',
    location='BLR',
    currency='USD',
    max_rate=100)

print("testing")
print(resp)
