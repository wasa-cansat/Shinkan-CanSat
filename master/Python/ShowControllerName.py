import pygame
pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("接続されているコントローラーがありません。")
else:
    print("接続されているコントローラーの名前一覧:")
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        print(f"{i + 1}. {joystick.get_name()}")

pygame.quit()