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
			
		self.disque=((parted.getAllDevices())[-1].path) #Unite disque ,dernier p.e /dev/sdb
		if '/dev/sda' in self.disque:#Disque principal systeme
			sys.exit()
		else:
			print ("Disque = ",self.disque)		
		
		self.dev = parted.Device(self.disque) #Parted device
		self.partitions=parted.Disk(self.dev) #Partition	
		time.sleep(1)		
	
	def demonterDisque(self):
		"""Demonter disques"""
		print ("Demonter disques \n")
		
		for partition in (self.partitions).partitions:	
			print ("PARTITION  = ",partition.path)	
				
			if partition.busy:#Travaille la partition ?
				print (" démonter la partition ",partition.path ) #Chemin de partition
				commande='umount '+partition.path
				os.system (commande)
			else:
				print (partition.path + " NOT BUSY ! ")	
			
			#Remove partition
			print ("Efface PARTITION ",partition.path)
			self.partitions.deletePartition(partition=self.partitions.getPartitionByPath(partition.path))	
							
		time.sleep(1)			
					
	def creeTablePartition(self):
		"""Créer une nouvelle table de partition sur un disque"""	
		dev=parted.Device(self.disque)
		table=parted.freshDisk(dev,'gpt') #gpt msdos
		if not table.commit(): #Si c'est Vrai on le commit 
			sys.exit()
		else:
			print ("Nouvelle table de partition ")

		
		time.sleep(3)	
		
	def createPartitions(self,start,end):
		""" Cree des partition  fat32 et ext4"""	
		#dev=parted.Device(self.disque)
		#p=parted.Disk(dev)
		print ("\n disque =",self.disque," , START = ",start,", END = ",end)
		ptype=_ped.PARTITION_NORMAL	
		
		geometry=parted.Geometry(device=self.dev,start=start,end=end)
		partition=parted.Partition(disk=self.partitions,type=ptype,geometry=geometry)
		constraint=parted.Constraint(exactGeom=geometry)
		
		if self.partitions.addPartition(partition=partition,constraint=constraint):
			self.partitions.commit()
		else:
			print ("Error disk.addPartition in "+self.disque)
		time.sleep(1)	

	def resetPartitions(self):
		"""Efface signatures /dev/sdb1 /sdb2"""
		
		for partition in (self.partitions).partitions:
			commande ="wipefs --all "+partition.path
			print("Efface signature ",commande)
			os.system (commande)	
			
	def dernierSecteur(self):
		"""Récupérer le dernier secteur du disque"""
		#return (parted.getAllDevices())[-1].path().length		
		return parted.getAllDevices()[-1].length
	
	def creeSystemeFichiers(self,tipo):

		if tipo=='ext4':
			commande='mkfs.ext4 -F -L "rootfs" '+self.disque+'2'
		else:
			commande='mkfs.fat -F32 -v -I -n "BOOT" '+self.disque+'1'
		
		print ("Cree systeme de fichiers",commande)	
		os.system(commande)
		time.sleep(1)	
		

#Boucle principal 
	
disque= disk()
disque.demonterDisque() #Demonter disques

disque.creeTablePartition() #Cree nouvelle Table Partitions 

print ("Cree Partition fat")
disque.createPartitions(PREMIER_SECTEUR_FAT,DERNIER_SECTEUR_FAT) #Cree partition FAT32 BOOT
print ("Cree Partition ext4")
disque.createPartitions(DERNIER_SECTEUR_FAT+1,disque.dernierSecteur()-2048) #Cree partition EXT4 rootfs

disque.resetPartitions()#Reset Partitions /sdx1 /sdx2

#Cree systeme de fichiers fat32 et ext4
print ("Cree Systeme fichiers fat")
disque.creeSystemeFichiers('fat32')#Fat
print ("Cree Systeme fichiers ext4")
disque.creeSystemeFichiers('ext4')#ext4

