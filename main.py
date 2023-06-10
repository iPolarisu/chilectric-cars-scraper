from enum import auto
from bs4 import BeautifulSoup
import requests
import csv

FILE_NAME = "electric_cars_chile.csv"
URL = "https://energia.gob.cl/electromovilidad/catalogo?page="
MIN = 1
MAX = 13

cars_data = []

# iterate over catalogue pages and get information about cars
for page_number in range(MAX):

    # url and parser
    page_url = URL+str(page_number+1)
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # get all cars
    page_catalogue = soup.find(id="catalogo")
    page_cars = page_catalogue.findAll(True, {'class':['catalogofichagrande catalogobordeelectricopuro', 'catalogofichagrande catalogobordehibridoexterior']})

    # obtain data for each car and append to parsed cars list
    for page_car in page_cars:
        
        car = []

        # parsing car type
        car_type = page_car.find(True, {'class': ['catalogofichagrandetitulo catalogofondoelectricopuro', 'catalogofondohibridoexterior']}).text
        car.append(car_type)

        # parsing brand
        brand = page_car.find(True, {'class': ['catalogofichagrandetextomarca catalogofondohibridoexterior', 'catalogofichagrandetextomarca catalogofondoelectricopuro']}).text
        brand = brand.replace("> ", "")
        car.append(brand)

        other_info = page_car.findAll(True, {'class': ['catalogofichagrandetexto']})

        # parsing model (removing leading modelo:)
        model = other_info[0].text
        model = model.replace("· Modelo: ", "")
        car.append(model)

        # parsing car body
        car_body = other_info[1].text
        car_body = car_body.replace("· Carrocería: ", "")
        car.append(car_body)

        # parsing co2_emissions
        co2_emissions = other_info[2].text
        co2_emissions = co2_emissions.replace("· Emisiones de CO₂: ", "")
        co2_emissions = co2_emissions.replace(" [g de CO2/km]", "")
        co2_emissions = co2_emissions.replace(",", ".")
        car.append(co2_emissions)

        # parsing battery
        battery = other_info[3].text
        battery = battery.replace("· Capacidad de batería: ", "")
        battery = battery.replace(" [kWh]", "")
        battery = battery.replace(",", ".")
        car.append(battery)

        # parsing performance
        performance = other_info[4].text
        performance = performance.replace("· Rendimiento eléctrico: ", "")
        performance = performance.replace(" [km/kWh]", "")
        performance = performance.replace(",", ".")
        car.append(performance)

        # parsing autonomy
        autonomy = other_info[5].text
        autonomy = autonomy.replace("· Autonomía eléctrica: ", "")
        autonomy = autonomy.replace(" [km]", "")
        autonomy = autonomy.replace(",", ".")
        car.append(autonomy)
        
        # parsing web site
        web_site = other_info[6].text
        web_site = web_site.replace("· Sitio web: ", "")
        car.append(web_site)

        cars_data.append(car)


HEADERS = ['type', 'brand', 'model', 'body', 'emissions', 'battery', 'performance', 'autonomy', 'website']

with open(FILE_NAME, 'w', encoding="UTF8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(HEADERS)
    
    writer.writerows(cars_data)