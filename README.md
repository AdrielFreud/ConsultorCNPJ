## AdrielFreud

![](https://img.shields.io/badge/ConsultarCNPJ-v1.0-blue?style=flat&logo=appveyor)
![](https://img.shields.io/badge/plataforma-win32--win64--linux64--linux32-blue?style=flat&logo=appveyor)
![](https://img.shields.io/badge/python-3.x.x-blue)

 - O Script faz a busca em uma base de dados e tras informações sobre seu CNPJ informado.
 
 ```python
 if cnpj <= 20:
    code = req.status_code
    if code == 200:
      html = req.text
      receita = json.loads(html.encode('utf-8'))
```

## AVISO
- Caso você encontrar um bug [Click-aqui](https://github.com/AdrielFreud/ConsultorCNPJ/issues/new) crie um issue para eu corrigi-lo.

## Imagem
![photo]()

## Características
  - Consulta CNPJ.
  - Very Simple and Fast.
 
 ## Download
Baixe diretamente do github com:
 - git clone https://github.com/AdrielFreud/ConsultorCNPJ.git
 - ou https://github.com/AdrielFreud/ConsultorCNPJ/archive/master.zip


## Uso
 - py ConsultorCNPJ.py [type] 0123456789

## Requerimentos
 - Python3
# Bibliotecas python necessarias:
  - pip install requests
