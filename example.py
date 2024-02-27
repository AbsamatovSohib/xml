import xml.etree.ElementTree as ET
mytree = ET.parse("example1.xml")
my_root= mytree.getroot()


# print(my_root.tag)
# print("\t",my_root[0].tag)
# requestIdxxx = my_root[0]
# print( my_root[0].text)

pricedItin = my_root[1]
# print(pricedItin.tag)

flights_0 = pricedItin[0]

onward = flights_0[0]

flight_in_on = onward[0]


#  1-vazifani javobi
#  start
reys_names_dict = []
reys_names = []
#
depar_arrival_time = []

for flights_0 in pricedItin:
    for onward in flights_0:
        for flight_in_on in onward:
            for x in flight_in_on:
                carrier = x[0].text
                dep_time = x[4].text
                arr_time = x[5].text
                flight_num = x[1].text

                if carrier not in reys_names:
                    reys_names.append(carrier)
                    reys_names_dict.append({"Company":carrier})

                depar_arrival_time.append({"FLight number":flight_num, "Departure time":dep_time, "Arrival time":arr_time})
                flight_number = x[1]
                destination = x[2]

for x in reys_names_dict:
    print(x["Company"])

#1-vazifa end

# 2-vazifa javobi
# for x in depar_arrival_time:
#     print("flight number -->", x["FLight number"])
#     print("Departure time -->", x["Departure time"])
#     print("Arrival time -->",x["Arrival time"],"\n")

# 2 task end

# for x in pricing:


# for flight_in_on in pricedItin:
# n = 0
# for flights_0 in pricedItin:
#     n += 1
#     pricing = flights_0[2]
#     base_fare = pricing[0].text
#     airline_taxes = pricing[1].text
#     total = pricing[2].text
#     print(f"{n}) ",base_fare, airline_taxes, total)
