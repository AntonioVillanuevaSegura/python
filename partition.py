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
	""" Classe pour effectuer des opérations de disque"""
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
		"""Demonter et effacer disques"""
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
		"""Créer une nouvelle table d
		Efface signaturev disque   wipefs --all /dev/sdb2
		/dev/sdb2 : 2 octets ont été effacés à l'index 0x00000438 (ext4) : 53 ef
		Cree Systeme fichiers fat

		Créé le systeme de fichiers  mkfs.fat -F32 -v -I -n "BOOT" /dev/sdb1
		mkfs.fat 3.0.28 (2015-05-16)
		/dev/sdb1 has 255 heads and 63 sectors per track,
		hidden sectors 0x0800;
		logical sector size is 512,
		using 0xf8 media descriptor, with 2048000 sectors;
		drive number 0x80;
		filesystem has 2 32-bit FATs and 8 sectors per cluster.
		FAT size is 1997 sectors, and provides 255496 clusters.
		There are 32 reserved sectors.
		Volume ID is 2107cb40, volume label BOOT       .
		Cree Systeme fichiers ext4
		e partition sur un disque"""	
		dev=parted.Device(self.disque)
		table=parted.freshDisk(dev,'gpt') #gpt msdos
		if not table.commit(): #Si c'est Vrai on le commit 
			sys.exit()
		else:
			print ("\nNouvelle table de partition "+self.disque)

		
		time.sleep(3)	
		
	def createPartitions(self,start,end):
		""" Cree des partition  fat32 et ext4"""	
		print ("\nDisque =",self.disque," , START = ",start,", END = ",end)
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
		"""Efface signatures /dev/sdX1 /sdX2"""		
		for partition in (self.partitions).partitions:
			commande ="wipefs --all "+partition.path
			print("\nEfface signaturev disque  ",commande)
			os.system (commande)	
			
	def dernierSecteur(self):
		"""Récupéré le dernier secteur du disque"""	
		return parted.getAllDevices()[-1].length
	
	def creeSystemeFichiers(self,tipo):
		""" Créé le système de fichiers selon l'argument fat32 ou ext4 """
		if tipo=='ext4':
			commande='mkfs.ext4 -F -L "rootfs" '+self.disque+'2'
		else:
			commande='mkfs.fat -F32 -v -I -n "BOOT" '+self.disque+'1'
		
		print ("\nCréé le systeme de fichiers ",commande)	
		os.system(commande)
		time.sleep(1)	
		
	def formatDisque (self):
		"""Boucle principal""" 
			
		#disque= disk()#Créé une instance de la classe disk

		self.demonterDisque() #Demonter disques

		self.creeTablePartition() #Cree nouvelle Table Partitions 

		print ("Cree Partition fat")
		self.createPartitions(PREMIER_SECTEUR_FAT,DERNIER_SECTEUR_FAT) #Cree partition FAT32 BOOT
		print ("Cree Partition ext4")
		self.createPartitions(DERNIER_SECTEUR_FAT+1,self.dernierSecteur()-2048) #Cree partition EXT4 rootfs

		self.resetPartitions()#Reset Partitions /sdx1 /sdx2

		#Cree systeme de fichiers fat32 et ext4
		print ("Cree Systeme fichiers fat")
		self.creeSystemeFichiers('fat32')#Fat
		print ("Cree Systeme fichiers ext4")
		self.creeSystemeFichiers('ext4')#ext4		
		
	def mountDisk(self):
		""" monter disques /dev/sdX1 /dev/sdX2"""
		""" udisksctl mount -b /dev/sde1"""

		commande="udisksctl mount -b "+str(self.disque)
		
		print (" montage des disques = ",commande)
		
		os.system(commande+"1")
		os.system(commande+"2")		


