import os
import ctypes

ATRIBUTO_OCULTAR = 0x02

def ocultar(nome_arquivo):
    """
    Ocultador de arquivos multiplataforma
    """
    # Para sistemas *nix adicione um prefixo '.'
    prefixo = '.' if os.name != 'nt' else ''
    nome_arquivo_oculto = prefixo + nome_arquivo
    cmd = "mv {} {}".format(nome_arquivo,nome_arquivo_oculto)
    os.system(cmd)
    
    # Para Windows define o atributo do arquivo
    if os.name == 'nt':
        ret = ctypes.windll.kernel32.SetFileAttributesW(file_name,
                                                        ATRIBUTO_OCULTAR)
        if not ret: # There was an error.
            raise ctypes.WinError()

nome_arq = "oculta.txt"
ocultar(nome_arq)