#!/usr/bin/env python3
# -*- coding: utf-8

"""
Antonio Villanueva Segura partitionner un disque 
"""
import parted,_ped
import os #Appels système
import sys #système
import time #temps

PREMIER_SECTEUR_FAT =2048
DERNIER_SECTEUR_FAT =2050047

class disk ():
	
	def __init__(self):
			
		self.disque=(parted.getAllDevices()).path()[-1] #Unite disque ,dernier p.e /dev/sdb
		if '/dev/sda' in disque:#Disque principal systeme
			sys.exit()
		else:
			print ("Disque = ",disque)		
		
		self.dev = parted.Device(disque) #Parted device
		self.partitions=parted.Disk(self.dev) #Partition		
	
	def demonterDisque(self):
		"""Demonter disques"""
		for partition in self.partitions.partitions:			
			if partition.busy:#Travaille la partition ?
				print (" démonter la partition ",partition.path ) #Chemin de partition
				commande='umount '+partition.path
				os.system (commande)	
				
	def creeTablePartition(self):
		"""Créer une nouvelle table de partition sur un disque"""		
		table=parted.freshDisk(self.dev,'gpt') #gpt msdos
		if not table.commit(): #Si c'est Vrai on le commit 
			sys.exit()
		time.sleep(1)			
		
	def createPartitions(self,start,end):
		""" Cree des partition  fat32 et ext4"""
		
		print ("disque =",self.disque," , START = ",start,", END = ",end)
		ptype=_ped.PARTITION_NORMAL	
		
		geometry=parted.Geometry(device=self.dev,start=start,end=end)
		partition=parted.Partition(disk=self.partitions,type=ptype,geometry=geometry)
		constraint=parted.Constraint(exactGeom=geometry)
		
		if self.partitions.addPartition(partition=partition,constraint=constraint):
			self.partitions.commit()
		else:
			print ("Error disk.addPartition")
		time.sleep(1)	
		
	def dernierSecteur(self):
		"""Récupérer le dernier secteur du disque"""
		return (parted.getAllDevices()).path()[-1].length		
		
#Boucle principal 
	
disque= disk()
disque.demonterDisque() #Demonter disques
disque.creeTablePartition() #Cree nouvelle Table Partitions 
disque.createPartitions(PREMIER_SECTEUR_FAT,DERNIER_SECTEUR_FAT) #Cree partition FAT32 BOOT
#disque.createPartitions(DERNIER_SECTEUR_FAT+1,) #Cree partition EXT4 rootfs



#print ("Dernier secteur ",disque.dernierSecteur())
