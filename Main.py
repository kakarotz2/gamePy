
import pygame
import sys
from Game import*
def birdAnimation(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -birdMove*2, 1)
    return new_bird
def bird_animation():
    new_bird = bird_list[index]
    new_bird_rect = new_bird.get_rect(center = (100,birdRect.centery))
    return new_bird ,new_bird_rect
while True:
    # Draw backgroud x,y = (0,0)
    screen.blit(backGround, (0, 0))
    # Draw chim
    rotated_bird = birdAnimation(bird)
    screen.blit(rotated_bird, birdRect)
    # Trọng lực của chim
    birdMove += gravity
    birdRect.centery += birdMove
    # Sàn di chuyển
    floorPos -= 4
    screen.blit(floor, (floorPos, 620))
    screen.blit(floor, (floorPos + 480, 620))
    if floorPos <= -480:
        floorPos = 0
    # Draw ống xuống
    tubeImgDow_1 = pygame.transform.scale(tubeDow, (tube_Width, tubeHeight_1))
    tubeDow_1 = screen.blit(tubeImgDow_1, (tube1_x, 0))

    tubeImgDow_2 = pygame.transform.scale(tubeDow, (tube_Width, tubeHeight_2))
    tubeDow_2 = screen.blit(tubeImgDow_2, (tube2_x, 0))

    tubeImgDow_3 = pygame.transform.scale(tubeDow, (tube_Width, tubeHeight_3))
    tubeDow_3 = screen.blit(tubeImgDow_3, (tube3_x, 0))
    # Draw ống lên
    tubeImgUp = pygame.transform.scale(
        tubeUp, (tube_Width, 720 - (tubeHeight_1 + tube_k)))
    tubeUp_1 = screen.blit(tubeUp, (tube1_x, tubeHeight_1 + tube_k))

    tubeImgUp = pygame.transform.scale(
        tubeUp, (tube_Width, 720 - (tubeHeight_2 + tube_k)))
    tubeUp_2 = screen.blit(tubeUp, (tube2_x, tubeHeight_2 + tube_k))

    tubeImgUp = pygame.transform.scale(
        tubeUp, (tube_Width, 720 - (tubeHeight_3 + tube_k)))
    tubeUp_3 = screen.blit(tubeUp, (tube3_x, tubeHeight_3 + tube_k))

    # Ống di chuyển
    tube1_x -= tubeMove
    tube2_x -= tubeMove
    tube3_x -= tubeMove
    if tube1_x <= -tube_Width:
        tube1_x = 550
        tubeHeight_1 = randint(100, 400)
        tubePass_1 = False
    if tube2_x <= -tube_Width:
        tube2_x = 550
        tubeHeight_2 = randint(100, 400)
        tubePass_2 = False
    if tube3_x <= -tube_Width:
        tube3_x = 550
        tubeHeight_1 = randint(100, 400)
        tubePass_3 = False
    # Score
    score_txt = font.render('Score: ' + str(score), True, '#FFFFFF')
    screen.blit(score_txt, (5, 5))
    if tube1_x + tube_Width <= x_bird and tubePass_1 == False:
        score += 1
        sound_score.play()
        tubePass_1 = True
    if tube2_x + tube_Width <= x_bird and tubePass_2 == False:
        score += 1
        sound_score.play()
        tubePass_2 = True
    if tube3_x + tube_Width <= x_bird and tubePass_3 == False:
        score += 1
        sound_score.play()
        tubePass_3 = True
    # xử lý va chạm
    tubes = [tubeDow_1, tubeDow_2, tubeDow_3, tubeUp_1, tubeUp_2, tubeUp_3]
    for tube in tubes:
        if birdRect.colliderect(tube) or birdRect.top <= 0 or birdRect.bottom >= 620:
            gravity = 0
            birdMove = 0
            tubeMove = 0
            floorPos = 0
            screen.blit(gameOver, (120, y/2 - 50))
            scoreEndGame = font1.render('Score: ' + str(score), True, '#0000FF') 
            screen.blit(scoreEndGame, (x/2 - 50, y/2))
            spaceContinue = font1.render('Press Space to continue!', True, '#0000FF') 
            screen.blit(spaceContinue, (x/2 - 150, y/2 + 30))
            gameActivity = True
    # Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                birdMove = 0
                birdMove -= 8
                sound.play()
                if gameActivity:
                    x_bird = 100
                    y_bird = y/2
                    tube1_x = 400
                    tube2_x = 600
                    tube3_x = 800
                    tubeMove = 4
                    gravity = 0.5
                    score = 0
                    gameActivity = False
                    
        if event.type == birdFlap:
            if index < 2:
                index +=1
            else:
                index = 0
        bird, birdRect = bird_animation()
    pygame.display.update()
    Fps.tick(fps)
