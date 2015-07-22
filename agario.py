#agario
import pygame
import sys
import random

pygame.init() #potřeba zadat
weight = 1250
height = 750
foodnb = weight*height/6250
screen = pygame.display.set_mode((weight, height)) #vel.okna
pygame.display.set_caption("Agar.io")#název okna
pygame.display.set_icon(pygame.image.load("pic/icon32.png"))
clock = pygame.time.Clock()
bg_color=(0,0,30)

#jídlo_obrazky
food_img = []
for i in range(1, 6):
    food_img.append(pygame.image.load("pic/food"+str(i)+".png").convert_alpha())

#generovani jídla
food = pygame.sprite.Group()

while True:
	clock.tick(60)
	for event in pygame.event.get():
		if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): #jestli zmáčku křížek/Alt+F4/ze správce úloh
			print("shutting down")
			sys.exit()

	##pohyb
	#palka.rect.left += palka.speedX
	#if palka.rect.left < 0:
	#    palka.rect.left=0
	#elif palka.rect.right > 400:
	#    palka.rect.right=400

	##mizení jídla
	#for mic in micky:
	#    if mic.rect.bottom > 588:
	#        micky.remove(mic)

	#doplnění jídla
	if len(food) < foodnb:
		onefood = pygame.sprite.Sprite()
		onefood.image = random.choice(food_img)
		onefood.rect = onefood.image.get_rect()
		onefood.rect.topleft = (random.randint(0, weight - 4), random.randint(0, height - 4))
		food.add(onefood)

	## powerupy -> kolize
	#for powerup in powerups:
	#	powerup.rect.centery += 5
	#for powerup in pygame.sprite.spritecollide(palka, powerups, 1):
	#	mic = pygame.sprite.Sprite()
	#	mic.image = mic_img
	#	mic.rect = mic_img.get_rect()
	#	mic.rect.bottom = palka.rect.top
	#	mic.rect.left = palka.rect.left
	#	mic.speed = [0.0, 5.0]
	#	mic.speed2 = [0, 0]
	#	mic.sticky = True
	#	micky.add(mic)

	##vypisování skóre
	#screen.fill((0, 0, 0), (0, 588, 400, 12)) #(left, top, width, height)
	#screen.blit(score.img, score.rect)
	#for i in range(len(score.lis)):
	#    screen.blit(text.num[int(score.lis[i])], score.Nrect[i])

	##kresleni
	screen.fill(bg_color) #5.vyplní okno barvou
	#screen.blit(palka.image, palka.rect)#zobrazí pálku na souřadnice
	#powerups.draw(screen)
	#micky.draw(screen)
	food.draw(screen) #vykresli jidlo

	pygame.display.update()
input("DONE")