from flask import Flask, request, render_template
from apps.manualpred import predict1, predict2, predict3, predict4, predict5, predict6,predict7, predict8, predict9, predict10, predict11, predict12
#from apps.tensorflow import getfile, prepare_model, load_model, DataResult1

app = Flask(__name__, template_folder='template')




@app.route('/',  methods=['GET'])
def index():

    return render_template('final.html')


@app.route('/manualpreds1', methods=['POST'])
def manualpred1():
    pred = predict1()
    print(pred)
    return pred		

@app.route('/manualpreds2', methods=['POST'])
def manualpred2():
    pred = predict2()
    print(pred)
    return pred

@app.route('/manualpreds3', methods=['POST'])
def manualpred3():
    pred = predict3()
    print(pred)
    return pred	

@app.route('/manualpreds4', methods=['POST'])
def manualpred4():
    pred = predict4()
    print(pred)
    return pred

@app.route('/manualpreds5', methods=['POST'])
def manualpred5():
    pred = predict5()
    print(pred)
    return pred

@app.route('/manualpreds6', methods=['POST'])
def manualpred6():
    pred = predict6()
    print(pred)
    return pred

@app.route('/manualpreds7', methods=['POST'])
def manualpred7():
    pred = predict7()
    print(pred)
    return pred

@app.route('/manualpreds8', methods=['POST'])
def manualpred8():
    pred = predict8()
    print(pred)
    return pred

@app.route('/manualpreds9', methods=['POST'])
def manualpred9():
    pred = predict9()
    print(pred)
    return pred

@app.route('/manualpreds10', methods=['POST'])
def manualpred():
    pred = predict10()
    print(pred)
    return pred

@app.route('/manualpreds11', methods=['POST'])
def manualpred11():
    pred = predict11()
    print(pred)
    return pred

@app.route('/manualpreds12', methods=['POST'])
def manualpred12():
    pred = predict12()
    print(pred)
    return pred

@app.route('/about')
def aboutproject():
    return render_template("about.html")

@app.route('/adopt')
def adopt():
    return render_template("adopt.html")


if __name__ == "__main__":
	app.run(debug=True)