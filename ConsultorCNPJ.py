import requests
import json
import argparse

parse = argparse.ArgumentParser(description="CPNJ for Get Informations!")
parse.add_argument("-c", "--cnpj", help="Url for get Informations! ")
args = parse.parse_args()

menu = """\033[1;36m
  _____                       _ _             _____  _   _ ______  ___ 
 /  __ \                     | | |           /  __ \| \ | || ___ \|_  |
 | /  \/ ___  _ __  ___ _   _| | |_ ___  _ __| /  \/|  \| || |_/ /  | |
 | |    / _ \| '_ \/ __| | | | | __/ _ \| '__| |    | . ` ||  __/   | |
 | \__/\ (_) | | | \__ \ |_| | | || (_) | |  | \__/\| |\  || |  /\__/ /
  \____/\___/|_| |_|___/\__,_|_|\__\___/|_|   \____/\_| \_/\_|  \____/ 

Powered by Adriel Freud\n\n\n033[1;m"""

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}

def consultar(cnpj):
	url = 'https://www.receitaws.com.br/v1/cnpj/{0}'.format(cnpj)
	req = requests.get(url, headers=headers)
	code = req.status_code
	if code == 200:
		html = req.text
		receita = json.loads(html)
		print("\033[31mAtividade Principal: %s\033[1;m"%receita['atividade_principal'][0]['text'])
		print("\033[31mNome: %s\033[1;m"%receita['nome'])
		print("\033[31mComplemento: %s\033[1;m"%receita['complemento'])
		print("\033[31mUF: %s\033[1;m"%receita['uf'])
		print("\033[31mTelefone: %s\033[1;m"%receita['telefone'])
		print("\033[31mEmail: %s\033[1;m"%receita['email'])
		print("\033[31m(QSA) Nome: %s\033[1;m"%receita['qsa'][0]['nome'])
		print("\033[31m(QSA) Nome: %s\033[1;m"%receita['qsa'][1]['nome'])
		print("\033[31mSituacao: %s\033[1;m"%receita['situacao'])
		print("\033[31mBairro: %s\033[1;m"%receita['bairro'])
		print("\033[31mNumero: %s\033[1;m"%receita['numero'])
		print("\033[31mCEP: %s\033[1;m"%receita['cep'])
		print("\033[31mMunicipio: %s\033[1;m"%receita['municipio'])
		print("\033[31mCNPJ: %s\033[1;m"%receita['cnpj'])
		print("\033[31mStatus: %s\033[1;m"%receita['status'])
	else:
		print("\033[31m[!] Error ao Requisitar o Site!\n\033[1;m")

if args.cnpj:
	print(menu)
	consultar(args.cnpj)
else:
	print(menu)
	parse.print_help()
