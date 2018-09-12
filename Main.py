#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Histograma import Histograma

if __name__ == '__main__':
	print("Processamento de Imagens.")

	histograma = Histograma("img/4x4.png")
	histograma.carregarImagem()

	histograma.executar()
			
	print("Fim execução!!")
