import os
from dotenv import load_dotenv
import json
import requests
from geopy.geocoders import Nominatim
from twilio.rest import Client

# def obtener_coordenadas(ciudad):
#     try:
#         location = geolocator.geocode(ciudad)
#         if location:
#             return location.latitude, location.longitude
#         else:
#             return "Ciudad no encontrada"
#     except Exception as e:
#         return f"Error: {e}"
#
# #ciudad = "Algarrobo, Chile"
# ciudad = "Santiago, Chile"
# # Inicializar el geocodificador (user_agent es obligatorio, pon cualquier nombre)
# geolocator = Nominatim(user_agent="mi_aplicacion_geocoding")
# lat, lon = obtener_coordenadas(ciudad)
# print(lat, lon)

lat=-33.4376995
lon=-70.6510671
load_dotenv()
WEATHER_API_KEY = os.environ["WEATHER_API_KEY"]
if not WEATHER_API_KEY:
    raise ValueError("Missing WEATHER_API_KEY. Create a .env file.")

response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric&lang=es&cnt=8")
datos=response.json()
#print(json.dumps(datos, indent=4))

#print(response.status_code)
if response.status_code != 200:
    raise Exception(f"API error: {response.status_code}")
else:
    #print("OK")
    #print(datos["list"][0]["weather"][0]["id"])
    llueve = False
    each2 = None
    #print("Santiago:")
    tiempo = "Santiago:"
    for each in datos["list"]:
        id = int(each["weather"][0]["id"])
        if id < 700:
            llueve = True
        each2=each
        #print("  ",each["dt_txt"]," Temp:",each["main"]["temp"]," ",each["weather"][0]["description"])
        tiempo = tiempo+"\n"+each["dt_txt"]+" Temp:"+str(each["main"]["temp"])+" "+each["weather"][0]["description"]
    #print(json.dumps(each, indent=4))
#print(json.dumps(each2, indent=4))
if llueve:
    print("Recomendación: Usar paragüas")
print(tiempo)

# account_sid = os.environ["account_sid"]
# auth_token  = os.environ["auth_token"]
# client = Client(account_sid, auth_token)
# phone_number = os.environ["phone_number"]
# message = client.messages.create(
#     body="Tiempo en Santiago"+f"{tiempo}",
#     from_="+12764441713",
#     to=f"{phone_number}",
# )
# print(message.body)
