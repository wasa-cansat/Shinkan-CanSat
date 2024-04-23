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