import pygame as pyg
import player as p
import coordinate as coord


def main():

    playerCoord = coord.position(500,360)
    plr = p.user(playerCoord)

    player_x = 0
    player_y = 0

    pyg.init()
    screen = pyg.display.set_mode((1000,720))

    #ADDITIONAL SETTING
    pyg.display.set_caption("Hello world")
    pyg.display.set_icon(
        pyg.image.load('t.png')
    )
    isRunning = True

    while isRunning:

        screen.fill((0,0,0))
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                isRunning = False

            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_a:
                    player_x = -1
                if event.key == pyg.K_d:
                    player_x =  1

                if event.key == pyg.K_w:
                    player_y = -1
                if event.key == pyg.K_s:
                    player_y =  1

            if event.type == pyg.KEYUP:
                if event.key == pyg.K_a or event.key == pyg.K_d:
                    player_x = 0
                if event.key == pyg.K_w or event.key == pyg.K_s:
                    player_y = 0


        plr.position = coord.position(plr.position.x + player_x, plr.position.y + player_y)

        screen.blit(plr.sprite, (plr.position.x, plr.position.y))
        pyg.display.update()

if __name__ == "__main__":
    main()