from statistics import mode
from flask import Flask, send_from_directory, render_template
from flask import request
import requests
 
app = Flask(__name__)

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api')
def abc():
  data = request.args.get('loc')
  findDistMatrix(data)
  return {
        "user": "John Doe",
    }

def findDistMatrix(cord,mode="driving"):
  URL = "https://api.mapbox.com/directions-matrix/v1/mapbox/driving/"+cord[:-1]+"?approaches=curb;curb;curb;curb&access_token=pk.eyJ1Ijoia3VzaDc4IiwiYSI6ImNsMzVqZHF3djBmMWMza3A1c2MzY3Y1NjkifQ.-PI6HfCVSnQVi5MguiQISQ"

  # sending get request and saving the response as response object
  r = requests.get(url = URL) 
  
  # extracting data in json format
  data = r.json()
  print(data['durations'])
  return data




if __name__ == '__main__':
  app.run(debug=True)