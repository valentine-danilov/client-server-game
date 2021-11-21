import pygame
from network import Network

width = 500
height = 500

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Client")


def redrawWindow(window, player, otherPlayers):
    window.fill((255, 255, 255))
    player.draw(window)
    for op in otherPlayers:
        op.draw(window)
    pygame.display.update()


def main():
    run = True
    n = Network()

    p = n.getPlayer()
    a = 0

    clock = pygame.time.Clock()
    while run:
        clock.tick(60)

        otherPlayers = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, otherPlayers)


main()
