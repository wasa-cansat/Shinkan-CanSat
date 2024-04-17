import time
import pygame
import serial
import serial.tools.list_ports 

pygame.init()
pygame.joystick.init()

target_name = "Gamepad F310" #controller name
desired_hwid_part = "9C9C1FCBD5EE" #Bluetooth ID
target_controller = None
ports = list(serial.tools.list_ports.comports())

if pygame.joystick.get_count() == 0: # ゲームパッドが接続されているか確認
    print("No controllers found.")
    quit()

for i in range(pygame.joystick.get_count()): # 指定の名前を含むゲームパッドを探す
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    if target_name in joystick.get_name():
        target_controller = joystick
        print("Target controller found:", target_controller.get_name())
        break

if target_controller is None:
    print("Target controller not found.")
    quit()

for p in ports:
    if desired_hwid_part in p.hwid:
        print("ESP32_1のポートを見つけました:", p.name) #p.hwid 
        ser = serial.Serial(port=p.device, baudrate=9600)
        break
        
#Main program
done = False

while not done:
    print("Event")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("a")

            ser.close()
            done = True

    # 左スティックの値を取得
    n = target_controller.get_axis(1)
    m = target_controller.get_axis(3)

    command = None

    # ボタン
    if target_controller.get_button(0) == 1:  # Green A button
        command = b'A'
    elif target_controller.get_button(1) == 1:  # Red B button
        command = b'B'
    elif target_controller.get_button(2) == 1:  # Blue X button
        command = b'X'
    elif target_controller.get_button(3) == 1:  # Yellow Y button
        command = b'Y'

    elif n >= 0.4 and m >= 0.4:
        command = b'1'
    elif n < 0.4 and n > -0.4 and m >= 0.4:
        command = b'2'
    elif n <= 0.4 and m >= 0.4:
        command = b'3'
    elif n >= 0.4 and m < 0.4 and m > -0.4:
        command = b'4'
    elif n < 0.4 and n > -0.4 and m < 0.4 and m > -0.4:
        command = b'5'
    elif n <= 0.4 and m < 0.4 and m > -0.4:
        command = b'6'
    elif n >= 0.4 and m <= -0.4:
        command = b'7'
    elif n < 0.4 and n > -0.4 and m <= -0.4:
        command = b'8'
    elif n <= -0.4 and m <= -0.4:
        command = b'9'

    if command is not None:
        ser.write(command)
        print(command.decode())  # バイトを文字列に変換して出力

    time.sleep(0.001)