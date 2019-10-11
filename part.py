#!/usr/bin/env python3
# -*- coding: utf-8
"""
#Antonio Villanueva Segura partitionner un disque et copier les informations
http://huntingbears.com.ve/operaciones-de-lectura-y-escritura-de-particiones-con-python-parted.html
"""
import parted,_ped
import os #Appels système
import sys #système
import time #temps


def analyseDisques():
	""" Liste des disques et paramètres divers"""
	disques=parted.getAllDevices()

	for disk in disques:
		print ("Repertoire \t",disk.path) #répertoire disque
		print ("taille.sector \t",disk.sectorSize)	# La taille en bytes de chaque secteur
		print ("nombre.secteurs \t",disk.length ) #nombre de secteurs
		print ("Busy ? \t",disk.busy) #disque busy ?
		print ("Modele  \t",disk.model)	#Modele disque	
		print ("Taille.disque \t",disk.getSize(unit='GB')) #Taille disque en GB	

def analysePartition(disque='/dev/sdb'):
	"""Analise disques"""
	dev = parted.Device(disque)
	disque=parted.Disk(dev)
	
	print ("Tam.sector ",dev.sectorSize) #Normalemente 512 ...
	print ("Espacio libre ",disque.getFreeSpacePartitions())
	for particion in disque.partitions:
		print ("\n")
		print ("Type partition = ",particion.type) #Type partition
		print ("numéro de partition = ",particion.number) #numéro de partition
		print ("Chemin de partition = ",particion.path ) #Chemin de partition
		print ("Début de la partition en secteurs START= ",particion.geometry.start) #Début de la partition en secteurs
		print ("Fin de la partition en secteurs END=",particion.geometry.end) #Fin de la partition en secteurs
		print ("Taille de la partition en secteurs =",particion.geometry.length) #Taille de la partition en secteurs
		print ("Drapeaux de partition = ",particion.getFlagsAsString()) #Drapeaux de partition
		
		print ("----->" ,particion.fileSystem)
		
		if (particion.fileSystem!=None):
			print (particion.fileSystem.type ) #Type de système de fichiers								

def creaTablaParticion(disque='/dev/sdb'):
	"""Créer une nouvelle table de partition sur un disque"""
	
	dev=parted.Device(disque)	
	#tabla=parted.freshDisk(dev,'msdos')
	tabla=parted.freshDisk(dev,'gpt')
	if not tabla.commit(): #Si c'est Vrai on le commit 
		sys.exit()
	time.sleep(1)

def drapeaux(disk='/dev/sdb',activa=True):
	""" Créer et supprimer des drapeaux"""
	""" Nombre 	Constant _ped 	Sens
		1 	_ped.PARTITION_BOOT 	Drapeau de démarrage
		14 	_ped.PARTITION_DIAG 	Drapeau de diagnostic
		4 	_ped.PARTITION_HIDDEN 	Drapeau caché
		7 	_ped.PARTITION_LBA 		Drapeau pour les systèmes linéaires MSDOS
		6 	_ped.PARTITION_LVM 		Drapeau pour les arrangements LVM
		9 	_ped.PARTITION_PALO 	Drapeau de démarrage pour PALO
		10 	_ped.PARTITION_PREP 	Drapeau de démarrage pour PRPC PowerPC
		5 	_ped.PARTITION_RAID 	Drapeau de matrice RAID
	"""
	flag=_ped.PARTITION_BOOT
	dev=parted.Device(disk)
	disque=parted.Disk(dev)
	
	particion=disk.getPartitionByPath(disk,'1') #/dev/sdb1 p.e
	if activa:		
		if not partition.setFlag(flag): #Assigne PARTITION_BOOT
			return
			
	else:
		if not partition.unsetFlag(flag):# désactiver PARTITION_BOOT
			return
		
	#Vérifier l'opération précédente avant commit	
	disk.commit()

def createPartition(disque='/dev/sdb',start=2048,end=2050047):
	""" Créer une partition """
	#start et end ils sont des secteurs !!!!!
	#Vous ne pouvez pas partitionner là où une partition existe Les secteurs doivent être libres
	#Une partition ne peut pas commencer là où une autre se termine
	#L'argument parted.Partition doit être un numéro de table

	"""
	Nombre 	Constant _ped 	Sens
	0 	_ped.PARTITION_NORMAL 	Partition primaire
	1 	_ped.PARTITION_LOGICAL 	Partition logique
	2 	_ped.PARTITION_EXTENDED	Partition étendue
	"""
	
	print ("disque =",disque," , START = ",start,", END = ",end)
	ptype=_ped.PARTITION_NORMAL	
	dev=parted.Device(disque)
	disk=parted.Disk(dev)
	
	geometry=parted.Geometry(device=dev,start=start,end=end)
	partition=parted.Partition(disk=disk,type=ptype,geometry=geometry)
	constraint=parted.Constraint(exactGeom=geometry)
	
	if disk.addPartition(partition=partition,constraint=constraint):
		disk.commit()
	else:
		print ("Error disk.addPartition")
	time.sleep(1)		
		
		
def creeSystemeFichiers(disque='/dev/sdb1',tipo='fat32'):
	"""
	Cree système de fichiers
	btrfs 	mkfs.btrfs [PART] 	btrfs filesystem resize [TAM] [PART]
	ext2 	mkfs.ext2 -q -F -F [PART] 	resize2fs -f [PART] [TAM]
	ext3 	mkfs.ext3 -q -F -F [PART] 	resize2fs -f [PART] [TAM]
	ext4 	mkfs.ext4 -q -F -F [PART] 	resize2fs -f [PART] [TAM]
	fat16 	mkfs.vfat [PART] 	fatresize -q -s [TAM] [PART]
	fat32 	mkfs.vfat [PART] 	fatresize -q -s [TAM] [PART]
	ntfs 	mkfs.ntfs -q -F [PART] 	ntfsresize -f -P -b -s [TAM] [PART]
	hfs 	hformat -f [PART] 	N/A
	hfs+ 	mkfs.hfsplus [PART] 	N/A
	jfs 	mkfs.jfs -q [PART] 	N/A
	swap 	mkswap -f [PART] 	N/A
	reiser4 	mkfs.reiser4 -y -f [PART] 	N/A
	reiserfs 	mkfs.reiserfs -q -f -f [PART] 	resize_reiserfs -q -f -s [TAM] [PART]
	xfs 	mkfs.xfs -q -f [PART] 	N/A
	"""

	if tipo=='ext4':
		commande='mkfs.ext4 -F -L "rootfs" '+disque
	else:
		commande='mkfs.fat -F32 -v -I -n "BOOT" '+disque
	
	print ("Cree systeme de fichiers",commande)	
	os.system(commande)
	time.sleep(1)

def demonterDisque(disque='/dev/sdb'):
	"""Analyser les partitions montées sdb1 sdb2 sdb3
	les disques apparaissent dans /etc/mtab ou /etc/mount
	"""	
	dev = parted.Device(disque)
	disque=parted.Disk(dev)

	for particion in disque.partitions:
		
		if particion.busy:#Travaille la partition ?
			print (" desmontando ",particion.path ) #Chemin de partition
			commande='umount '+particion.path
			os.system (commande)

def resetPartition(disque='/dev/sdb'):
	"""Efface signatures /dev/sdb1 /sdb2"""
	commande ="wipefs --all "+disque
	print("Efface signature ",commande)
	os.system (commande)	
	

#-----------------------------------------------------------------------
	
print (" - Axiome Concept -")

disques=parted.getAllDevices() #Recupere touts les disques 
disque=str(disques[-1].path) #Recupere le dernier disque ça evite /dev/sda
fin=disques[-1].length #Recupere nombre de secteurs 
dernierSect=fin-1 #Dernier Secteur
print ("Repertoire = ,",disque)

if '/dev/sda' in disque: #Si seulement disque de systeme exit 
	sys.exit()

print ("fin =",fin)

#analyseDisques()
#analysePartition(disque)
#creaTablaParticion()

#Demonter disque
demonterDisque(disque)

#Cree Table de Partition
creaTablaParticion(disque)

#Cree Partition HD
createPartition(disque,2048,2050047) #Fat
#createPartition('/dev/sdb',2050048,976773119) #Ext4
createPartition(disque,2050048,dernierSect-2048) #Ext4 dernier Secteur -2048

#Reset Partition 
resetPartition(disque+'1')
resetPartition(disque+'2')

#Cree systeme de fichiers fat32 et ext4
creeSystemeFichiers(disque+'1','fat32')#Fat
creeSystemeFichiers(disque+'2','ext4')#ext4

