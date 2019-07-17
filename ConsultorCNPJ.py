# Desenvolvido por Adriel Freud!
# Contato: businessc0rp2k17@gmail.com
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
#conding: utf-8

import requests
import json
import argparse
import sys

parse = argparse.ArgumentParser(description="CNPJ for Get Informations!")
parse.add_argument("-c", "--cnpj", help="Url for get Informations! ")
args = parse.parse_args()

menu = r"""\033[1;36m
  _____                       _ _             _____  _   _ ______  ___ 
 /  __ \                     | | |           /  __ \| \ | || ___ \|_  |
 | /  \/ ___  _ __  ___ _   _| | |_ ___  _ __| /  \/|  \| || |_/ /  | |
 | |    / _ \| '_ \/ __| | | | | __/ _ \| '__| |    | . ` ||  __/   | |
 | \__/\ (_) | | | \__ \ |_| | | || (_) | |  | \__/\| |\  || |  /\__/ /
  \____/\___/|_| |_|___/\__,_|_|\__\___/|_|   \____/\_| \_/\_|  \____/ 
Powered by Adriel Freud\n"""

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}

def export_json(cnpj):
	url = 'https://www.receitaws.com.br/v1/cnpj/{0}'.format(cnpj)
	req = requests.get(url, headers=headers)
	code = req.status_code
	if code == 200:
		html = req.text
		with open('file1.json', 'w') as w:
			w.write(html.encode('utf-8'))
			w.close()

def consultar(cnpj):
	url = 'https://www.receitaws.com.br/v1/cnpj/{0}'.format(cnpj)
	req = requests.get(url, headers=headers)
	code = req.status_code
	if code == 200:
		html = req.text
		receita = json.loads(html.encode('utf-8'))
		#print("\033[31mAtividade Principal: %s"%receita['atividade_principal'][0]['text'])
		print("\033[31mNome: %s"%receita['nome'])
		print("\033[31mComplemento: %s"%receita['complemento'])
		print("\033[31mUF: %s"%receita['uf'])
		print("\033[31mTelefone: %s"%receita['telefone'])
		print("\033[31mEmail: %s"%receita['email'])
		print("\033[31m(QSA) Nome: %s"%receita['qsa'][0]['nome'])
		print("\033[31m(QSA) Nome: %s"%receita['qsa'][1]['nome'])
		print("\033[31mSituacao: %s"%receita['situacao'])
		print("\033[31mBairro: %s"%receita['bairro'])
		print("\033[31mNumero: %s"%receita['numero'])
		print("\033[31mCEP: %s"%receita['cep'])
		print("\033[31mMunicipio: %s"%receita['municipio'])
		print("\033[31mCNPJ: %s"%receita['cnpj'])
		print("\033[31mStatus: %s"%receita['status'])
	else:
		print("\033[31m[!] Error ao Requisitar o Site!\n\033[1;m")

if args.cnpj:
	print(menu)
	export_json(args.cnpj)
	consultar(args.cnpj)

else:
	print(menu)
	parse.print_help()
