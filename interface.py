#!/usr/bin/env python3
# -*- coding: utf-8

"""
Antonio Villanueva Segura tkinter buttons
"""
from partition import disk
#import tkinter
from tkinter import *
import tkinter.ttk as ttk
import os #Appels système

class fenetre():
	""" Classe pour le gui graphique"""
	
	cartes=[ "RO B+ arm7 ", "RO B+ arm6", "Aria Ro","Rpi HD"] #Possibilités création sd hd
	roArm6=" /home/axiome/Bureau/Thomas/axisat2/ro/vB+ARM6_ro_axisat_v222_noDesktop/"
	roArm7=" /home/axiome/Bureau/Thomas/axisat2/ro/v11_ro_axisat_v222_noDesktop/"
	
#	boot=" /media/axiome/BOOT/"
#	rootfs=" /media/axiome/rootfs/"

	boot=" /media/root/BOOT/"
	rootfs=" /media/root/rootfs/"
	
	#image="sudo tar -xvjpSf "+bootB+.tar.bz2 -C /media/axiome/BOOT/	
	image="sudo tar -xvjpSf "
	
	disque=disk()
	
	def __init__(self,fenetre):
		self.fenetre=fenetre
		self.setupFenetre()
		self.elementsFenetre()
		
	def setupFenetre(self):
		"""Configuration fenetre """
		self.fenetre.geometry("250x90")
		self.fenetre.title("Creation HD SD")
	
	def elementsFenetre(self):
		"""Ajoute boutons ,etiquettes,menus déroulants ... """
		#Boutons
		ButtonDo=Button(self.fenetre,text="MAKE",command=lambda:self.make("MAKE"))
		
		#Etiquetes
		Etiquette=Label(self.fenetre,text="Sélectionnez l'option souhaitée")
	
		
		#Menus déroulants
		self.Sel = ttk.Combobox(self.fenetre, textvariable=self.cartes[1],values=self.cartes,state='readonly')	
		
		self.Sel.current(0) #Valeur par défaut menu déroulant 				
		
		#Grille Place les différents éléments sur la grille
		Etiquette.grid(column=1,row=0)		
		ButtonDo.grid(column=0,row=1)		
		self.Sel.grid(column=1,row=1)	
		
		
	def make(self,sel):
		"""Click button ,on peut récupérer la valeur du bouton dans sel"""
		
		#Préparer le disque pour la copie,table de partition, format ...
		self.disque.formatDisque()
		self.disque.mountDisk() #Monter disque pour copie	
		
		# Base de commande construction 
		commande=self.image
		
		print ("Créé = ",self.Sel.get())
		
		if self.Sel.get()==self.cartes[0]:#RO B+ arm7
			os.system (commande+self.roArm7+"boot900.tar.bz2 -C "+self.boot)
			os.system (commande+self.roArm7+"rootfs.tar.bz2 -C "+self.rootfs)
			os.system ("sync")				
			
		if self.Sel.get()==self.cartes[1]:#RO B+ arm6
			os.system (commande+self.roArm6+"bootB+.tar.bz2 -C "+self.boot)
			os.system (commande+self.roArm6+"rootfsB+.tar.bz2 -C "+self.rootfs)
			os.system ("sync")			

			
		if self.Sel.get()==self.cartes[2]:#Aria Ro
			print ("3 option")
			
		if self.Sel.get()==self.cartes[3]:#Rpi HD
			print ("4 option")	
		
		self.disque.demonterDisque() #Demonter disque
			
		sys.exit()		
				


#Boucle principale

window=Tk()

f=fenetre(window)

window.mainloop()
