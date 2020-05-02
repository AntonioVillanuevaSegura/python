#https://github.com/thepasterover/alien_invasion/issues/1

import pygame


def explosion (pantalla,x,y,rectangulo,img):
	color=(255,0,0)	
	
	#recupera informacion de la imagen
	rectangulo=img.get_rect()
	mitad=rectangulo.width/2 #mitad de la imagen
	
	ancho=20
	alto=3
	
	#Crea un cuadrado en x,y de 5x5
	while ancho>=5:
		
		if (mitad - ancho/2)>=0:
			x=(mitad - ancho/2)
		else:
			x=0
			
		print ("rectangulo en ",x,y)
		
		forma=pygame.Rect(x,y,ancho,alto)	
		pygame.draw.rect (img,color,forma)
		

		ancho-=5 #reduce 5 por cada lado 
		y+=alto #desciende 5

	return img
	
def test():
	""" imagen 110x80"""
	color = (0, 50, 0,255) #un color RGB
	pantalla=pygame.display.set_mode((1200,800)) #ALTO x ANCHO pantalla
	rect_pantalla=pantalla.get_rect() #rect de pantalla	
	pantalla.fill(color) #color pantalla de fondo
	
	#print (rect_pantalla)
		
	image=pygame.image.load('imagenes/ShieldImage.xpm')
	rect=image.get_rect() #rectangulo del bunker
	
	#posicion de la imagen del bunker
	rect.x=0
	rect.y=0
	
	#recibe disparo en 
	x=0
	y=0
	
	"""  creamos una explosion en 110,0 p.e"""
	image=explosion(pantalla,x,y,rect,image)
	
	#print (rect)
	pantalla.blit(image,rect)


pygame.init()
test()
pygame.display.flip()	
pygame.time.wait(2000)
pygame.quit()
