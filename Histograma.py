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

		'''
		LUT - Look-up table
		'''
		l = 255
		
		rk = np.zeros(l) #Quantidade de níveis de cinza
		nk = np.zeros(l) #Quantidade de pixels de mesmo nível
		pr_rk = np.zeros(l) #Probabilidades (nk/total_pixels)
		freq = np.zeros(l) #Soma das frequências(freq[i] + freq[i-1])
		eq = np.zeros(l) #Eq é o novo pr(rk)*(L-1)
		novo_rk = np.zeros(l) #É o valor arredondado de Eq
		
		m1 = self.m if self.m%2==0 else self.m-1
		n1 = self.n if self.n%2==0 else self.n-1
		
		saida = np.zeros([m1, n1])
		
		'''
		Salva a quantidade de pixels em um mesmo nível (nk)
		'''
		for i in range(m1):
			for j in range(n1):
				for	k in range(l-1):
					if self.matriz[i][j] >= (k/(l-1))*255 and self.matriz[i][j] < ((k+1)/(l-1))*255:
						nk[k] += 1
		
		#Total de Pixels
		total = m1*n1
		
		'''
		Salva os valores de pr(rk), das frequências, dos valores equalizados e do novo rk
		'''
		for i in range(l):
			pr_rk[i] = (nk[i])/(total)
			
			#Frequência
			if i == 0:
				freq[i] = pr_rk[i]
			else:
				freq[i] = freq[i-1] + pr_rk[i]
		
			eq[i] = freq[i]*(l-1)
			novo_rk[i] = round(eq[i])

		
		colunas = ['rk', 'nk', 'Pr(rk)', 'Freq', 'Eq', 'Novo rk']
		rows  = ['%d' % i for i in range(l)]
		data  = [nk, pr_rk, freq, eq, novo_rk]
		
		'''
		Imprime a Look-up Table.
		'''
		for i in range(len(colunas)):
			print("{}".format(colunas[i]), end = '\t')		
		
		print("")
		for i in range(l):
			print("{}\t{}\t{}\t{}\t{}\t{}".format(i, round(nk[i],2), round(pr_rk[i],2), round(freq[i],2), round(eq[i],2), round(novo_rk[i],2)))

		
		'''
		Adiciona valores do novo rk na nova Imagem(saida)
		'''	
		for i in range(m1):
			for j in range(n1):
				for	k in range(l-1):
					if self.matriz[i][j] >= (k/(l-1))*255 and self.matriz[i][j] < ((k+1)/(l-1))*255:
						saida[i][j] = (novo_rk[k]/(l-1))*255
					
		#Imprime Imagem Original
		self.img.show()
		imagem = Image.fromarray(saida)	
		#Imprime Imagem Equalizada
		imagem.show()
		
		
		'''
		Imprime Histograma Original
		'''
		n, bins, patches = plt.hist(x=nk, bins=50, color='#0504aa', alpha=0.7, rwidth=0.85)
		
		plt.grid(axis='y', alpha=0.75)
		plt.xlabel('Nível de Cinza (rk)')
		plt.ylabel('Probabilidade de rk (nk)')
		plt.title('Histograma da Imagem')
		plt.text(23, 45, r'$\mu=15, b=3$')	
		plt.show()
		
		'''
		Imprime Histograma da Nova Imagem
		'''
		n, bins, patches = plt.hist(x=novo_rk, bins=50, color='#0504aa', alpha=0.7, rwidth=0.85)
		
		plt.grid(axis='y', alpha=0.75)
		plt.xlabel('Nível de Cinza (rk)')
		plt.ylabel('Probabilidade de rk (nk)')
		plt.title('Novo Histograma da Imagem')
		plt.text(23, 45, r'$\mu=15, b=3$')
		plt.show()
		
		