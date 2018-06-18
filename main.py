from flask import Flask
from flask import render_template
from flask import redirect
from flask_socketio import SocketIO
#import time
#from parser_level_upper_capacity import parser_level_upper_capacity

import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

stand_data = {
    'valve': False,
    'pump': False,
    'bottom_capacity': 30,
    'upper_capacity': 20,
    'valve_perc': 0,
}

@app.route('/')
def index():
    return render_template('index.html', title='Заглавная страница', stand_data=stand_data)

@socketio.on('starting_pump', namespace='/flask')
def pumping(msg):
    global stand_data
    if not stand_data['pump'] and msg == 'on_pump':
        stand_data['pump'] = True
        while stand_data['upper_capacity'] < 100 and stand_data['pump'] and msg != 'off_pump':
            socketio.sleep(1)
            stand_data['upper_capacity'] += 10
            print('Насос в работе и уровень в верхней ёмкости: ', stand_data['upper_capacity'])
            socketio.emit('filling_upper_capacity', stand_data, namespace='/flask')
    else:
        print('Насос уже включен', stand_data['pump'])
    print('Функция on_pump выполнена', stand_data['pump'])

@app.route("/off_pump", methods=['POST'])
def off_pump():
    stand_data['pump'] = False
    print('Функция off_pump выполнена', stand_data['pump'])
#    print(parser_level_upper_capacity())
    return redirect('/')

#print(parser_level_upper_capacity())

if __name__ == '__main__':
    socketio.run(app, debug=True)

'''@socketio.on('stop_pump', namespace='/flask')
def stop_pumping(msg):
    global stand_data
    if msg == 'off_pump':
        stand_data['pump'] = False
        print('Функция off_pump выполнена', stand_data['pump'])
        socketio.emit('stop_filling_upper_capacity', stand_data, namespace='/flask')'''

'''@socketio.on('pump_control', namespace='/flask')
def pumping(msg):
    if not stand_data['pump'] and msg == 'on_pump':
        stand_data['pump'] = True
        while stand_data['upper_capacity'] < 100 and msg != 'off_pump' and stand_data['pump']:
            print(msg)
            socketio.sleep(1)
            stand_data['upper_capacity'] += 10
            print('Насос в работе и уровень в верхней ёмкости: ', stand_data['upper_capacity'])
            socketio.emit('filling_upper_capacity', stand_data, namespace='/flask')
    elif msg == 'off_pump':
        print(msg)
        stand_data['pump'] = False
        print('Насос уже включен', stand_data['pump'])
        socketio.emit('stop_filling_upper_capacity', stand_data, namespace='/flask')
    print('Функция on_pump выполнена', stand_data['pump'])'''

'''@socketio.on('valve_opening', namespace='/flask')
def change_valve_opening(msg):
    global stand_data
    stand_data[msg['data']] = msg['value']
    print('msg = ', msg)
#    print('stand_data = ', stand_data)
    socketio.emit('valve_status', stand_data, namespace='/flask')'''