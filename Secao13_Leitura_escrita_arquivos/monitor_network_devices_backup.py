"""Verificação de diretórios e seus arquivos em tamanho e tmepo de criação."""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import json


def verify_directories() -> None:
    """Função de verificação dos diretórios."""
    # Carregando do arquivo de configuração, com tempo limite e diretórios:
    with open('monitor_network_devices_backup.json') as config:
        data = json.load(config)
    max_time = data['max_time']

    erro = False

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
                    erro = True
                    print(
                        f"Arquivo mais recente de nome {newest_file}, " +
                        f"do diretorio {dir['path_name']}, " +
                        f"ultrapassou o limite de {max_time} horas."
                    )

                # Verifica se o tamanho do arquivo buscado é maior que 0:
                elif os.stat(newest_file).st_size == 0:
                    print("Erro! O arquivo mais recente possui tamanho zero.")
                    erro = True
            else:
                print(f"Sem arquivos no diretorio {dir['path_name']}.")
                erro = True
        except FileNotFoundError:
            print(f"Erro! Diretorio {dir['path_name']} nao existe!")
            erro = True
    if not erro:
        print("<<OK>>")


def add_new_dir() -> None:
    """Adiciona um novo diretório ao arquivo .json de configuração."""
    path_dir = input("Digite o path: ")
    name_file = input("Digite o nome do arquivo: ")
    with open('monitor_network_devices_backup.json', 'r+') as json_file:
        data = json.load(json_file)

    with open('monitor_network_devices_backup.json', 'w') as json_file:
        new_dir__ = {'path_name': path_dir, 'file_name': name_file}
        data['directories'].append(new_dir__)
        json.dump(data, json_file, ensure_ascii=False, indent=4)


# Permite a chamada de funcoes em especifico via linha de comando
if __name__ == '__main__':
    verify_directories()
