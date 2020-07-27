from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hell0 world"),200

@app.route('/notfound')
def notfound():
    return jsonify(message='Something went wrong ,Not fount'),404

@app.route('/param')
def param():
    name=request.args.get('name')
    age=int(request.args.get('age'))
    if age<18:
        return jsonify(message="Sorry"+name+"you age us under 18"),401
    else:
        return jsonify(message='Success'),200
@app.route('/url/<string:name>/<int:age>')
def urlvar(name:str,age:int):
    if age<18:
        return jsonify(message="Sorry"+name+"you age us under 18"),401
    else:
        return jsonify(message='Success'),200



if __name__=='__main__':
    app.run()