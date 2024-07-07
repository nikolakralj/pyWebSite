from flask import Flask, jsonify, render_template
from psycopg2 import connect
from neon_connect import create_connection_pool

app = Flask(__name__)

pool = create_connection_pool()
print(pool)
@app.route("/")
def hello():
    print("Hey help MEEEE")
    return render_template('home.html',jobs=pool)
    
@app.route("/api/jobs")
    #this is a decorator generating second url. SO when someone call this url 
    #it execute the function below and function return json data to same url 
def list_jobs():#this is a function retruning json data 
    return jsonify(jobs=pool)
# when people say rest API or JSON API or API endpoint that mean that my webserver 
# is not returning only html but it is returning json data or rest data...
# so when someone call this url it will return json data to same url
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)