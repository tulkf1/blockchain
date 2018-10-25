
import json        # импортируем формат обмена данными кода Java Script         
import os          # импортируем модуль операционной системы, для работы с файлами
import hashlib     # импортируем модуль криптографии и шифрования


analisys_dir = os.curdir + '/analisys/' # задается текущий каталог

def get_hash(filename):
	 
		file = open(analisys_dir + filename, 'rb').read()

		return hashlib.md5(file).hexdigest()


def get_files():
	files = os.listdir(analisys_dir)     
	return sorted([int(i) for i in files])



def check_integrity(): 
	 
	 files = get_files() # [1, 2, 3, 4, 5, ... n], первый блок (1) является генезис блоком и не включаяет в себя хэш-скрипт

	 results = []

	 for file in files[1:]: # [2, 3, 4, 5, ... n], для каждой итерации в цикле
			f = open(analisys_dir + str(file)) # преобразование числа в строку
			h = json.load(f)['hash']

			prev_file = str(file - 1)
			actual_hash = get_hash(prev_file)

			if h == actual_hash:
				res = 'Документ цел'
			else:
				res = 'Документ поврежден'

			#print('block {} is: {}'.format(prev_file, res))	

			results.append ({'block': prev_file, 'result': res})

			return results

def write_block(agent_name, amount, principal_name, prev_hash=''):
		files = get_files()
		prev_file = files [-1]

		filename = str(prev_file + 1)
		print(filename)

		prev_hash = get_hash(str(prev_file))

		data = {'agent_name': agent_name,  # data - абстрактная структура данных, хранящая в себе параметры обработки
				'amount': amount,  
				'principal_name': principal_name,  
				'hash': prev_hash }  

		with open(analisys_dir + filename, 'w') as file :  
					json.dump(data, file, indent=4, ensure_ascii=False) 


def main():
		write_block(agent_name='jaja', amount=22, principal_name='anderzel')
		print (check_integrity())


if __name__ == '__main__':
		main() 