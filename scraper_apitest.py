import requests

contract_addr = '0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413'
api_key = '39M8BBF53U6M7N2YS92M163RP3RCZF6GUK'

r = requests.get('https://api.etherscan.io/api?module=contract&action=getsourcecode&address=' + contract_addr +'&apikey=' + api_key)
r = eval(r.text)
result = r['result'][0]['SourceCode']
print(result)

with open('temp.sol', 'w') as f:
    f.write(result)
