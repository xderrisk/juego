import pygame

pygame.init()
screen = pygame.display.set_mode((240, 480))
pygame.display.set_caption("Juego")
clock = pygame.time.Clock()
running = True

limite = pygame.Rect(25, 25, 190, 430)
jugador = pygame.Vector2(120,35)
gravedad = 25
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jugador.y -= 300 * dt #sub
    if keys[pygame.K_s]:
        jugador.y += 300 * dt #cae
    if keys[pygame.K_a]:
        jugador.x -= 300 * dt #izq
    if keys[pygame.K_d]:
        jugador.x += 300 * dt #der

    jugador.y += gravedad * dt
    if jugador.y + 10 > limite.bottom:
        jugador.y = limite.bottom - 10
    if jugador.x - 10 < limite.left:
        jugador.x = limite.left + 10
    if jugador.x + 10 > limite.right:
        jugador.x = limite.right - 10

    screen.fill('black')
    pygame.draw.rect(screen, 'red', limite, 1)
    pygame.draw.circle(screen, 'orange', jugador, 10)
    pygame.display.flip()
    clock.tick(60)
    dt = clock.tick(60) / 1000

pygame.quit()