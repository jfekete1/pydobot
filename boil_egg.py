from serial.tools import list_ports

import pydobot

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[0].device

device = pydobot.Dobot(port=port, verbose=True)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print("DEVICE POSITION:")
print(f'x:{x} y:{y} z:{z} r:{r} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')



#remove the lid of the kettle

device.grip(False) #AA AA:4:63:3:01 00:189
device.move_to(255.49, -166.37, 145.97, r, wait=True)
device.move_to(256.34, -166.93, 116.31, r, wait=True)
device.wait(1000)
device.grip(True) #AA AA:4:63:3:01 01:188
device.wait(3000)
device.move_to(255.49, -166.37, 145.97, r, wait=True)
device.move_to(227.07, 5.83, 154.74, r, wait=True)
device.wait(1000)
device.move_to(170.13, -18.9, 51.5, r, wait=True)
device.wait(1000)
device.grip(False) #AA AA:4:63:3:01 00:189
device.wait(1000)
device._stop_gripper(True) #AA AA:4:63:3:00 00:190


#grab the egg, and put it into the boiling water.

device.grip(False) #AA AA:4:63:3:01 00:189
device.move_to(302.2, -22.39, 73.47, r, wait=True)
device.move_to(332.42, -37.21, -39.21, r, wait=True)
device.wait(1000)
device.grip(True) #AA AA:4:63:3:01 01:188
device.wait(3000)
device.grip(False) #AA AA:4:63:3:01 00:189
device.wait(1000)
device._stop_gripper(True) #AA AA:4:63:3:00 00:190



#x:243.48606872558594 y:-21.171403884887695 z:168.03648376464844 r:0.8283419609069824 j1:-4.969437122344971 j2:7.907989501953125 j3:-7.883204936981201 j4:5.797779083251953
#x:179.7049102783203 y:-2.0299017429351807 z:41.55010986328125 j1:-0.6471713185310364 j2:0.1679840087890625 j3:46.60279846191406 j4:5.960464477539063e-08
#x:227.2191925048828 y:11.741277694702148 z:20.91040802001953 j1:2.958059549331665 j2:23.342988967895508 j3:52.34479904174805 j4:5.960464477539063e-08




device.close()
