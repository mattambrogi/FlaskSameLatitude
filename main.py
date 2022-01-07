from flask import Flask
from flask import request
import random
from pandas import pandas as pd



app = Flask('app')

@app.route('/')
def index():
    lat = request.args.get("latitude", "")
    if lat:
        city = get_city(lat)
    else:
        city = ""
    return (
        """<form action="" method="get">
                Your latitude: <input type="text" name="latitude">
                <input type="submit" value="Submit">
            </form>"""
        + "City with the same latitude: "
        + city
    )
    
def get_city(lat):
  big_cities = pd.read_csv("big_cities.csv")
  lat = float(lat)
  lat_near_min = lat - 0.5
  lat_near_max = lat + 0.5
  cities_near = big_cities.loc[(big_cities['Latitude'] >= lat_near_min) & (big_cities['Latitude'] <= lat_near_max)]
  cities_near['Delta'] = abs(cities_near['Latitude'] - lat)
  cities_near.sort_values(by=['Delta'])
  return cities_near.iloc[0,3] +", " + cities_near.iloc[0,1].upper()


app.run(host='0.0.0.0', port=8080)