from serial.tools import list_ports

import pydobot

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[0].device

device = pydobot.Dobot(port=port, verbose=True)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print("DEVICE POSITION:")
print(f'x:{x} y:{y} z:{z} r:{r} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

device.close()
