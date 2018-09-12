#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Histograma import Histograma

if __name__ == '__main__':
	print("Processamento de Imagens.")

	histograma = Histograma("img/lena-gray.png")
	histograma.carregarImagem()

	histograma.executar()
			
	print("Fim execução!!")
