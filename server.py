from flask import Flask,redirect, url_for, request, jsonify, render_template, url_for
import funcoes
import json
from flask_cors import CORS
import uuid
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return render_template("index.html",name="index")

@app.route('/register', defaults={"name":False,'lastname':False,'participation':False}, methods=['POST'])
def register(name,lastname,participation):
    if funcoes.valid_register(request.form['name'],
                    request.form['lastname'],
                    request.form['participation']):
        form = dict(request.form)
        form["uniqID"] = str(str(uuid.uuid4().int)[:9])
        funcoes.registerJson(form)
 

    return render_template("index.html",name="index"),200
    


    

    

@app.route('/view', defaults={"options":False},methods=['GET'])
@app.route('/view/<options>',methods=['GET'])
def view(options):
    if options == "percentage":
        data = funcoes.forPorcent()
    elif options == False:
        data = funcoes.getTable()
    response = {
            "data":data,
            "status":200,
            "mimetype":'application/json'
            }
    
    return jsonify(response)


@app.route('/delete/<uniqID>',methods=['GET','POST'])
def delete(uniqID):

    data = funcoes.getTable()
    json.dumps(data)
    forRemove = []
    for row in data:
        if row["uniqID"] == uniqID:
            forRemove.append(row)
    for row in forRemove:
        data.remove(row)
    funcoes.alterJson(data)
    response = response = {
    "status":200,
    "mimetype":'application/json'
    }
    return jsonify(response)

app.run()

