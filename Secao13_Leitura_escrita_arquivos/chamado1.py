import os
import time
import sys

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

def check_fortigate_bkp_file():
    change_to_path = os.chdir(fortigate_path_to_check)
    path_log_files = os.listdir(fortigate_path_to_check)
    files = [f for f in path_log_files if f.startswith(fortigate_string_filename)]
    if files:
        """ Filtra arquivo mais recente da pasta """
        newest_file = max(files, key=lambda x: os.stat(x).st_mtime)
        st=os.stat(newest_file)
        creation_time=int(time.time()-st.st_mtime)

        """ 90000 = 25 horas """
        if creation_time > 90000:
            print("Arquivo mais recente '{}/{}' foi criado {} segundos atrás".format(fortigate_path_to_check, newest_file, creation_time))
        else:
            print("OK")

    else:
        print("Nenhum arquivo de log com nome '{}*' encontrado no diretório '{}'".format(fortigate_string_filename, fortigate_path_to_check))

def check_fortigate_bkp_file_size():
    change_to_path = os.chdir(fortigate_path_to_check) # Entra no diretorio de logs
    directory_dumps_list = os.listdir(fortigate_path_to_check)

    files = [f for f in directory_dumps_list if f.startswith(fortigate_string_filename)]
    if files:
        newest_file = max(files, key=lambda x: os.stat(x).st_mtime) # filtra o arquivo mais recente
        if os.stat(newest_file).st_size == 0: # verifica se o arquivo esta vazio
            """ Verifica se o tamanho do arquivo eh 0 """
            print("0")
        else:
            """ Mostra o tamanho do arquivo """
            print(os.stat(newest_file).st_size)
    else:
        print("99999999") #Arquivo nao encontrado


def check_ciscoasa_bkp_file():
    change_to_path = os.chdir(ciscoasa_path_to_check)
    path_log_files = os.listdir(ciscoasa_path_to_check)
    files = [f for f in path_log_files if f.startswith(ciscoasa_string_file_name)]
    if files:
        """ Filtra arquivo mais recente da pasta """
        newest_file = max(files, key=lambda x: os.stat(x).st_mtime)
        st=os.stat(newest_file)
        creation_time=int(time.time()-st.st_mtime)

        """ 90000 = 25 horas """
        if creation_time > 90000:
            #trigger: O arquivo mais recente do diretório tem mais de 24h em {HOST.NAME}
            print("Arquivo mais recente '{}/{}' foi criado {} segundos atrás".format(ciscoasa_path_to_check, newest_file, creation_time))
        else:
            print("OK")

    else:
        print("Nenhum arquivo de log com nome '{}*' encontrado no diretório '{}'".format(ciscoasa_string_file_name, ciscoasa_path_to_check))


def check_ciscoasa_bkp_file_size():
    change_to_path = os.chdir(ciscoasa_path_to_check) # Entra no diretorio de logs
    directory_dumps_list = os.listdir(ciscoasa_path_to_check)

    files = [f for f in directory_dumps_list if f.startswith(ciscoasa_string_file_name)]
    if files:
        newest_file = max(files, key=lambda x: os.stat(x).st_mtime) # filtra o arquivo mais recente
        if os.stat(newest_file).st_size == 0: # verifica se o arquivo esta vazio
            """ Verifica se o tamanho do arquivo eh 0 """
            print("0")
        else:
            """ Mostra o tamanho do arquivo """
            print(os.stat(newest_file).st_size)
    else:
        print("99999999") #Arquivo nao encontrado

def check_swcore_bkp_file():
    change_to_path = os.chdir(swcore_path_to_check)
    path_log_files = os.listdir(swcore_path_to_check)
    files = [f for f in path_log_files if f.startswith(swcore_string_file_name)]
    if files:
        """ Filtra arquivo mais recente da pasta """
        newest_file = max(files, key=lambda x: os.stat(x).st_mtime)
        st=os.stat(newest_file)
        creation_time=int(time.time()-st.st_mtime)

        """ 90000 = 25 horas """
        if creation_time > 90000:
            #trigger: O arquivo mais recente do diretório tem mais de 24h em {HOST.NAME}
            print("Arquivo mais recente '{}/{}' foi criado {} segundos atrás".format(swcore_path_to_check, newest_file, creation_time))
        else:
            print("OK")

    else:
        print("Nenhum arquivo de log com nome '{}*' encontrado no diretório '{}'".format(swcore_string_file_name, swcore_path_to_check))

def check_swcore_bkp_file_size():
    change_to_path = os.chdir(swcore_path_to_check) # Entra no diretorio de logs
    directory_dumps_list = os.listdir(swcore_path_to_check)

    files = [f for f in directory_dumps_list if f.startswith(swcore_string_file_name)]
    if files:
        newest_file = max(files, key=lambda x: os.stat(x).st_mtime) # filtra o arquivo mais recente
        if os.stat(newest_file).st_size == 0: # verifica se o arquivo esta vazio
            """ Verifica se o tamanho do arquivo eh 0 """
            print("0")
        else:
            """ Mostra o tamanho do arquivo """
            print(os.stat(newest_file).st_size)
    else:
        print("99999999") #Arquivo nao encontrado

# Permite a chamada de funcoes em especifico via linha de comando
if __name__ == '__main__':
    globals()[sys.argv[1]]()