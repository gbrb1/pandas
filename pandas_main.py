import pandas as pnd
import numpy as npy


def main(args):

	pnd.set_option('display.max_columns', None) #formatando colunas
	df_infoMunicipios['Municipio      '] = 'Acegua', 'Acrelandia', 'Alecrim', 'Almeirim', 'Alta Floresta Doeste','Alto Alegre','Alto Alegre dos Parecis', 'Amaraji', 'Antonio Joao', 'Aral Moreira'
	df_infoMunicipios['Estado     '] = 'Rio Grande do Sul', 'Acre', 'Rio Grande do Sul', 'Para', 'Rondonia', 'Roraima', 'Rondonia', 'Roraima', 'Mato Grosso do Sul', 'Mato Grosso do Sul'
	df_infoMunicipios['Area Territorial'] = 1500, 1575, 315, 72960, 7067, 25567, 3959, 28472, 1144, 1656
	df_infoMunicipios['Populacao'] = 4138, 11520, 7357, 30903, 23857, 14386, 11615, 7586, 8350, 9236, 
	df_infoMunicipios['PIB   '] = 71638000,  114350000, 44373000, 462258000, 186812000, 115786000,90226000, 31897, 39989000, 105697000
	df_infoMunicipios['IDH'] = 'ni', 0.68, 0.743, 0.745, 0.715, 0.662, 'nï', 0.654, 0.702, 0.723
	df_infoMunicipios['Densid. Demografica'] = 2.66, 7.31, 23.35, 0.42, 3.37, 0.56, 2.93, 0.26, 7.29, 5.57
	df_infoMunicipios['PIB per capita'] = df_infoMunicipios['PIB   '] / df_infoMunicipios['Populacao']

	print(df_infoMunicipios)
	
	print('\n')
	
	print('Media dos pibs: ', df_infoMunicipios['PIB   '].mean()) 
	
	print('\n')
	input('Pressione ENTER para sair')

	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))