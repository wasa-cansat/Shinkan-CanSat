import pygame
pygame.init()
pygame.joystick.init()

target_name = "Wireless Gamepad F710"

# ゲームパッドが接続されているか確認
if pygame.joystick.get_count() == 0:
    print("No controllers found.")
    quit()

# 指定の名前を含むゲームパッドを探す
target_controller = None
for i in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    if target_name in joystick.get_name():
        target_controller = joystick
        print("Target controller found:", target_controller.get_name())
        break

if target_controller is None:
    print("Target controller not found.")
    quit()

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYAXISMOTION:
            if event.joy == target_controller.get_id():
                # 特定のコントローラーからの入力の処理
                print("Controller input from:", target_controller.get_name())
                # ここに入力の処理を追加
                # 例えば、ボタンが押された場合の処理や、軸の動きに対する処理を書く

# 終了処理
pygame.quit()