    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ser.close()
            done = True