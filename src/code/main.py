import pygame

pygame.init()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
running = True
dt = 0
suelo = pygame.Rect(0, screen.get_height() -50, screen.get_width(), 50)
jugador = pygame.Vector2(screen.get_height() / 2, screen.get_width() / 2)
gravedad = 400

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    
    pygame.draw.rect(screen, "green", suelo)
    pygame.draw.circle(screen, "orange", jugador, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jugador.y -= 1000 * dt
    if keys[pygame.K_s]:
        jugador.y += 300 * dt
    if keys[pygame.K_a]:
        jugador.x -= 300 * dt
    if keys[pygame.K_d]:
        jugador.x += 300 * dt

    jugador.y += gravedad * dt
    if jugador.y + 40 > suelo.top:
        jugador.y = suelo.top - 40

    pygame.display.flip()
    clock.tick(60)
    dt = clock.tick(60) / 1000

pygame.quit()