import os
import json
import pandas as pd
import multiprocessing as mp

def scan(folder_path: str, file_name: str):
	# main myth scanner
	output = os.popen("cd %s && docker run -v $(pwd):/temp qspprotocol/mythril-usolc -xo json /temp/%s" % (folder_path, file_name), "r")
	# turn result into string
	result = output.read()
	# remove the containers
	
	return result

def loop(folder_path: str, save_path):
	result_list = []
	contracts = os.listdir(folder_path)
	total_number = len(contracts)
	error = 0
	index = 0

	for contract in contracts:
		try:
			result = scan(folder_path, contract)
			name = save_path + contract[:-3] + "json"
			with open(name, 'w') as f:
				f.write(result)
			print(f"{index}/{total_number} file scanned.")
			
		except:
			print("Error occured.")
			error += 1

		
		index += 1
		
		if index % 10 == 0:
			os.system("docker rm $(docker ps -aq)")
		# if index >=3:
		# 	break

	# df = pd.DataFrame(result_list)
	# df.to_csv('./eth_game.csv')
	print("============================================")
	print(f"{index} scanned, {error} failed.")
	return 0 

def print_hello(content):
	print(content)

if __name__ == '__main__':
	loop('contract/eth/highrisk', 'contract/eth/highrisk_result/')
	