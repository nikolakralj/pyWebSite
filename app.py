from flask import Flask, jsonify, render_template,jsonify
app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id':2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {   'id':3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 12,00,000'},
    {
        'id':4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$120,000'
    }
]

@app.route("/")
def hello():
    print("Hey help MEEEE")
    return render_template('home.html',jobs=JOBS)
    
@app.route("/api/jobs")
    #this is a decorator generating second url. SO when someone call this url 
    #it execute the function below and function return json data to same url 
def list_jobs():#this is a function retruning json data 
    return jsonify(jobs=JOBS)
# when people say rest API or JSON API or API endpoint that mean that my webserver 
# is not returning only html but it is returning json data or rest data...
# so when someone call this url it will return json data to same url
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)