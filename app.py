from flask import Flask, render_template
import requests


app= Flask(__name__)

def get_weather_data(city):
   APY_KEY ='e046257c07a0053d2e28ef4fb10d967f'
   url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=es&appid={APY_KEY}'
   r = requests.get(url).json()
   return r

@app.route("/")
def hello():
  data=get_weather_data('Guayaquil')
  return render_template('index.html', context = data)

@app.route("/defaz")
def defaz():
    return "<p>defaz</p>"

if __name__ == "__main__":
   app.run(debug = True)



