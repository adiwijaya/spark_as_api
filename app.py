from flask import Flask, render_template, request,session,jsonify,json
import connexion
from spark_jobs import count_length

#FLASK INIT
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/spark', methods = ['POST'])
def run_spark_job():
    if request.headers['Content-Type'] == 'application/json':
        parameters = request.json
        word = parameters['word']
        result = count_length(word)
        return jsonify(length=result)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
