#!/usr/bin/env python3
# -*- coding: utf-8 -*

from PIL import Image
import numpy as np
import math

class Histograma():

	def __init__(self, nome_imagem):
		self.nome_imagem = nome_imagem
		self.m = 0
		self.n = 0
		self.matriz = []
		self.img = []

	'''
	Abrindo o arquivo e pegando dimensões MxN
	'''
	def carregarImagem(self):
		img = Image.open(self.nome_imagem)
		self.img = img
		#Converte Imagem Object para Matriz
		self.matriz = np.asarray(img.convert('L'))
		#Dimensão M
		self.m = np.size(self.matriz, 0)	
		#Dimensão N
		self.n = np.size(self.matriz, 1)
		print("Linhas: {}\nColunas: {}\n".format(self.m, self.n))
		print(self.matriz)

	'''
	Executar
	'''
	def executar(self):
		m = np.zeros([self.m,self.n])
		m1 = np.size(m, 0)
		n1 = np.size(m, 1)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))


		#Ternário em Python
		m1 = self.m if self.m%2==0 else self.m-1
		n1 = self.n if self.n%2==0 else self.n-1

		theta = -1*((30*math.pi)/180)
		px = m1/2
		py = n1/2

		for i in range(m1):
			for j in range(n1):
				x = int((i-px)*math.cos(theta) - (j-py)*math.sin(theta)) + px-1 
				y = int((j-py)*math.sin(theta) + (i-px)*math.cos(theta)) + py-1
				x = i*math.cos(theta) - j*math.sin(theta)
				y = j*math.sin(theta) + i*math.cos(theta)

				if x > 0 or y > 0 or x < m1-1 or y < n1-1:
					m[i][j] = 255
				else:
					m[i][j] = m[x][y]
				
		for i in range(m1):
			for j in range(n1):
				if m[i][j] != 255:
					print(int(m[i][j]),end='')
			print('')

		imagem = Image.fromarray(m)
		#self.img.show()		
		imagem.show()