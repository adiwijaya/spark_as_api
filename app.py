from flask import Flask, render_template, request,session,jsonify,json
import connexion
from spark_jobs import count_length,read_table
from settings import *
from spark import terminate_spark

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
        result = 0
        result = count_length(word)
        return jsonify(length=result)

@app.route('/query', methods = ['POST'])
def read_tables_hive():
    if request.headers['Content-Type'] == 'application/json':
        parameters = request.json
        table_name = parameters['table_name']
        result = read_table(table_name)
        return result

#def main():
#    try:
#        app.run(host=HOST,debug=DEBUG,port=PORT)
    #finally:
        #terminate_spark()

if __name__ == '__main__':
    app.run(host=HOST,debug=DEBUG,port=PORT)
