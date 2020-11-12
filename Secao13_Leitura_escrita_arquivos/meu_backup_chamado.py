#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Neste, realiza a automatização das verificações da existência dos diretórios
Vamos então adicionar todos em um dicionário de dados
    Se possível, já realizar em um arquivo de configuração .json
Nele lemos o arquivo, trazemos ao dicionários os diretórios, fazemos as verif.:
    se tamanho > 0 e se o tempo de criação > 25 horas

No arquivo de configuração, deve conter o path do arquivo (path_to_check), 
nome do arquivo (string_file_name) e o tempo padrão de configuração (25 horas, 
por enquanto)

Fazer todas as verificações dentro de uma mesma função, se tudo ok, retorna um
print avisando que tudo ok, se com erro, retorna o erro

nome do arquivo original: monitora-bkp-equip-redes.py

upload ex: scp -r chamado_edit.py root@10.248.1.35:/opt/seven/scripts


"""

import os
import time
import json

""" parametros para verificação do backup do CISCOASABNC"""
ciscoasabnc_path_to_check = '/usr/local/scripts/bkp/ciscoasabnc'
ciscoasabnc_string_filename = 'runnung-config_'

""" parametros para verificação do backup do CISCOASADC"""
ciscoasadc_path_to_check = '/usr/local/scripts/bkp/ciscoasadc'
ciscoasadc_string_file_name = 'runnung-config_'

""" parametros para verificação do backup do FGT600EDC"""
fgt600Edc_path_to_check = '/usr/local/scripts/bkp/fgt600Edc'
fgt600Edc_string_file_name = 'conf_fgt600E_'

""" parametros para verificação do backup do SWCOREBNC"""
swcorebnc_path_to_check = '/usr/local/scripts/bkp/swcorebnc'
swcorebnc_string_file_name = 'startup-config_'

""" parametros para verificação do backup do SWCOREDC"""
swcoredc_path_to_check = '/usr/local/scripts/bkp/swcoredc'
swcoredc_string_file_name = 'startup-config_'

""" parametros para verificação do backup do SWDISTBNCA"""
swdistbncA_path_to_check = '/usr/local/scripts/bkp/swdistbncA'
swdistbncA_string_file_name = 'startup-config_'

""" parametros para verificação do backup do SWDISTBNCB"""
swdistbncB_path_to_check = '/usr/local/scripts/bkp/swdistbncB'
swdistbncB_string_file_name = 'startup-config_'


def verify_directories() -> None:
    """Função de verificação dos diretórios."""
    # Carregando do arquivo de configuração, com tempo limite e diretórios:
    with open('configuracao.json') as config:
        data = json.load(config)
    max_time = data['max_time']

    # Verificando cada um deles se obedecem aos requisitos:
    for dir in data['directories']:
        try:
            os.chdir(dir['path_name'])
            path_log_files = os.listdir(dir['path_name'])
            files = [
                f
                for f in path_log_files
                if f.startswith(dir['file_name'])
            ]
            if files:
                """ Filtra arquivo mais recente da pasta """
                newest_file = max(files, key=lambda x: os.stat(x).st_mtime)
                st = os.stat(newest_file)
                creation_time = int(time.time() - st.st_mtime)  # tempo criado

                # Verifica o tempo de arquivo mais recente na pasta:
                if creation_time > max_time * 3600:
                    print(
                        f"Arquivo mais recente de nome {newest_file}, " +
                        f"do diretorio {dir['path_name']}, " +
                        f"ultrapassou o limite de {max_time} horas."
                    )
                # Verifica se o tamanho do arquivo buscado é maior que 0:
                elif os.stat(newest_file).st_size == 0:
                    print("Erro! O arquivo mais recente possui tamanho zero.")
                else:
                    print(f"Tudo ok. Diretorio {dir['path_name']}. Tamanho " + 
                    f"do arquivo: {os.stat(newest_file).st_size} bytes. " +
                    f"Ultimo upload feito menos de {max_time} horas atras.")
            else:
                print(f"Sem arquivos no diretorio {dir['path_name']}.")
        except FileNotFoundError:
            print(f"Erro! Diretorio {dir['path_name']} nao existe!")



def new_dir() -> None:
    """Adiciona um novo diretório ao arquivo .json de configuração."""
    path_dir = input("Digite o path: ")
    name_file = input("Digite o nome do arquivo: ")
    with open('configuracao.json', 'r+') as json_file:
        data = json.load(json_file)

    with open('configuracao.json', 'w') as json_file:
        new_dir__ = {'path_name': path_dir, 'file_name': name_file}
        data['directories'].append(new_dir__)
        json.dump(data, json_file, ensure_ascii=False, indent=4)


# Permite a chamada de funcoes em especifico via linha de comando
if __name__ == '__main__':
    # Aqui apenas pra focar no meu diretório atual, depois retirar
    """este_diretorio = os.path.dirname(os.path.abspath(__file__))
    diretorio_raiz = os.path.dirname(este_diretorio)
    if diretorio_raiz not in sys.path:
        sys.path.insert(0, diretorio_raiz)
    """

    # new_dir()
    verify_directories()
