import pandas as pd
import numpy as np
import requests


def load_df(file_path:str):
    df = pd.read_csv(file_path)
    return df[['id', 'name', 'platform', 'cate', 'publish_date', 'contract']]

def get_contract(contract_addr):
    api_key = '39M8BBF53U6M7N2YS92M163RP3RCZF6GUK'
    r = requests.get('https://api.etherscan.io/api?module=contract&action=getsourcecode&address=' + contract_addr +'&apikey=' + api_key)
    r = eval(r.text)
    result = r['result'][0]['SourceCode']
    return result

def run(df, save_path):
    error_count = 0
    total = df.shape[0]
    for index, row in df.iterrows():
        contract_count = 0
        for addr in eval(row.contract):

            try:
                contract = get_contract(addr)
            except:
                print(f"Failed connecting to server at contract index {row['name']}-{contract_count}")
                error_count += 1
                continue

            name = save_path + row['name'] + '-' + str(contract_count) + '.sol'
            name = name.replace(" ", "_")
            with open(name, 'w') as f:
                f.write(contract)

            contract_count += 1
            print("File saved: " + name)
        print(f"{index}/{total} DApp saved: {row['name']}")
        print("======================================")
    print(f"{error_count} files failed.")
if __name__ == '__main__':
    df = load_df('./contract_addr/eth/eth_highrisk.csv')
    run(df, './contract/eth/highrisk/')

# 544/545 game saved: CryptoSpinners
# ======================================
# 38 files failed.