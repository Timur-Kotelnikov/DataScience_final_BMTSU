from flask import Flask, request, render_template
from tensorflow import keras

app = Flask(__name__)


@app.route('/')
def choose_prediction_method():
    return render_template('main.html')


def filler(params):
    model = keras.models.load_model('model_filler')
    prediction = model.predict([params])[0][0]
    return prediction

def strength(params):
    model = keras.models.load_model('model_strength')
    prediction = model.predict([params])[0][0]
    return prediction

def resilience(params):
    model = keras.models.load_model('model_resilience')
    prediction = model.predict([params])[0][0]
    return prediction


@app.route('/filler/', methods=['POST', 'GET'])
def get_filler():
    message = ''
    if request.method == 'POST':
        param_list = ('p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12')
        params = []
        for i in param_list:
            param = float(request.form.get(i))
            params.append(param)
        message = f'Прогнозируемое значение Соотношения матрица-наполнитель: {filler(params)}'
    return render_template('filler.html', message=message)

@app.route('/strength/', methods=['POST', 'GET'])
def get_strength():
    message = ''
    if request.method == 'POST':
        param_list = ('p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12')
        params = []
        for i in param_list:
            param = float(request.form.get(i))
            params.append(param)
        message = f'Прогнозируемое значение Прочности при растяжении: {strength(params)} МПа'
    return render_template('strength.html', message=message)

@app.route('/resilience/', methods=['POST', 'GET'])
def get_resilience():
    message = ''
    if request.method == 'POST':
        param_list = ('p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12')
        params = []
        for i in param_list:
            param = float(request.form.get(i))
            params.append(param)
        message = f'Прогнозируемое значение Модуля упругости при растяжении: {resilience(params)} ГПа'
    return render_template('resilience.html', message=message)

if __name__ == '__main__':
    app.run()