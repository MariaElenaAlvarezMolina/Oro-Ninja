from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "secret_key"

def actividad(accion, oro, locacion):
    timestamp = datetime.datetime.now()
    return '%s %d desde %s! (%s)' % (accion, oro, locacion, timestamp)

@app.route('/')
def index():
    if 'oro' not in session:
        session['oro'] = 0
    if 'actividades' not in session:
        session['actividades'] = []

    return render_template('index.html', oro=session['oro'], actividades=session['actividades'])

@app.route('/process_money', methods=['POST'])
def process_money():

    if request.form.get('accion') == "granja":
        oro_ganado = random.randrange(10, 20)
        session['oro'] += oro_ganado
        session['actividades'].insert(0, ['ganado', actividad('Ganado', oro_ganado, 'Granja')])
    
    if request.form.get('accion') == "cueva":
        oro_ganado = random.randrange(5, 10)
        session['oro'] += oro_ganado
        session['actividades'].insert(0, ['ganado', actividad('Ganado', oro_ganado, 'Cueva')])
    
    if request.form.get('accion') == "casa":
        oro_ganado = random.randrange(2, 5)
        session['oro'] += oro_ganado
        session['actividades'].insert(0, ['ganado', actividad('Ganado', oro_ganado, 'Casa')])

    if request.form.get('accion') == "casino":
        oro_ganado = random.randrange(-50, 50)
        session['oro'] += oro_ganado
        if oro_ganado > 0:
            session['actividades'].insert(0, ['ganado', actividad('Ganado', oro_ganado, 'Casino')])
        else:
            session['actividades'].insert(0, ['perdido', actividad('Perdido', -oro_ganado, 'Casino')])

    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)