#!/usr/bin/env python3
# -*- coding: utf-8 -*

from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt

class Histograma:

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
	
		#Dimensões MxN
		self.m, self.n = self.matriz.shape
		
		print("Linhas: {}\nColunas: {}\n".format(self.m, self.n))
		#print(self.matriz)

	'''
	Executar
	'''
	def executar(self):
		#Histograma
		a = 0 #Menor valor da faixa
		b = 255 #Maior valor da faixa
		
		c = float('-inf') #Menor valor da imagem
		d = float('inf') #Maior valor da imagem

		'''
		F(i,j) = G(F(i,j))
		Se a = 0 e b = 255
		G(F(i,j)) = (F(i,j)-c)*(255/(d-c)) 
		'''
		
		'''
		LUT - Look-up table
		'''
		l = 8
		
		rk = np.zeros(l) #Quantidade de níveis de cinza
		nk = np.zeros(l) #Quantidade de pixels de mesmo nível
		pr_rk = np.zeros(l) #Probabilidades (nk/total_pixels)
		freq = np.zeros(l) #Soma das frequências(freq[i] + freq[i-1])
		eq = np.zeros(l) #Eq é o novo pr(rk)*(L-1)
		novo_rk = np.zeros(l) #É o valor arredondado de Eq
		
		m1 = self.m if self.m%2==0 else self.m-1
		n1 = self.n if self.n%2==0 else self.n-1
		
		saida = np.zeros([m1, n1])
		
		for i in range(m1):
			for j in range(n1):
				for	k in range(l-1):
					if self.matriz[i][j] >= (k/(l-1))*255 and self.matriz[i][j] < ((k+1)/(l-1))*255:
						nk[k] += 1
		
		#Total de Pixels
		total = m1*n1
		
		for i in range(l):
			pr_rk[i] = (nk[i])/(total)
			
			#Frequência
			if i == 0:
				freq[i] = pr_rk[i]
			else:
				freq[i] = freq[i-1] + pr_rk[i]
		
			eq[i] = freq[i]*(l-1)
			novo_rk[i] = round(eq[i])

			
		print(nk)
		print(pr_rk)
		print(freq)
		print(eq)
		print(novo_rk)
		
		n, bins, patches = plt.hist(x=novo_rk, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
		
		plt.grid(axis='y', alpha=0.75)
		plt.xlabel('Value')
		plt.ylabel('Frequency')
		plt.title('My Very Own Histogram')
		plt.text(23, 45, r'$\mu=15, b=3$')
		maxfreq = n.max()
		# Set a clean upper y-axis limit.
		plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
				