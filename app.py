from flask import Flask ,jsonify, request
app = Flask(__name__)

"""@app.route('/')
def hola():
    response_saluda = {'saluda':'hola'}
    return jsonify(response_saluda)"""

@app.route('/',methods = ['POST','GET'])
def recibe():
    return jsonify({'variable':0})    

@app.route('/suma',methods = ['POST'])
def suma():
    valor = request.json.get('variable')
    valor = valor + 1
    return jsonify({'variable':valor})

if __name__ == "__main__":
    app.run(host='localhost',debug=True)
