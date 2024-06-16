import psutil       # type: ignore #This module used to get CPU & Memory metric of my server
from flask import Flask, render_template

app = Flask(__name__) #     creating a flask app, parameter: name

@app.route("/")         #app will run on home("/") path
def index():
    cpu_percent = psutil.cpu_percent()      #hold the value of my CPU usage
    mem_percent = psutil.virtual_memory().percent       #hold the value of my memory usage
    Message = None          #message=Message
    if cpu_percent > 80 or mem_percent > 80:
        Message= "CPU or Memory Utilization is High: Plese take necessary steps to scale up"
    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=Message)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')