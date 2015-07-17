#! coding: utf-8

# Bad Solution
# weather_dict = {}
#
# while True:
#     city = raw_input("Enter the city name: ")
#     if city:
#         tmp = raw_input("Enter the tmp value: ")
#         weather_dict[city] = weather_dict.get(city, 0) + int(tmp)
#     else:
#         for city, tmp in weather_dict.items():
#             print "{}: {}".format(city, tmp)
#         break

# Good Solution
rainfall = {}

while True:
    city_name = raw_input("Enter city name: ")
    if not city_name:
        break

    mm_rain = raw_input("Enter mm rain: ")
    rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)     # 1.1

for city, rain in rainfall.items():     # 1.2
    print("{}: {}".format(city, rain))

## 1.1 Usando o get para pegar o valor, pois poderia dar erro se não tivesse nenhum valor setado.
## 1.2 O for colocado fora do while pra não ser executado quando não tiver nenhuma cidade.