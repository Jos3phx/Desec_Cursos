#!/usr/bin/python2

################################################################
#                                                              #
# PROGRAMA SIMPLES EM PYTHON2 PARA QUEBRA SENHAS HASH COM SALT #
#                                                              #
################################################################

import crypt

print '''

	Hcrack em Python2 v0.1 - Beta

Programa para efetuar ataques de forca-bruta em HASHES MD5, SHA-256 E SHA-512 com SALT.

Segue referencia: https://man7.org/linux/man-pages/man3/crypt.3.html

Obs: Tarefa do curso Novo Pentest Profissional - Desec Security

'''
### 1 PARTE: ARMAZENA AS INFORMACOES DA HASH E SALT
hashc = raw_input("\nDigite a hash completa:  ")
salt = raw_input("\nInforme o SALT:  ")

#### ESTRUTURA PARA ABRIR O ARQUIVO DE SENHAS E SALVAR EM UMA LISTA
lista = []
with open('wl2.txt') as senhas:
    lista = senhas.read().splitlines()

### 2 PARTE: CRIAR UMA HASH COM SALT FORNECIDO E SALVAR (LISTA EXTERNA OPCIONAL)
resultado = []
for senha in lista:
    hashid = crypt.crypt(senha, salt)
    resultado.append("{}:{}".format(senha, hashid))  # ADICIONA O FORMATO "SENHA:HASH" A LISTA

# ESTRUTURA PARA SALVAR EM UM ARQUIVO EXTERNO
#with open('hashID.txt', 'w') as f:
#    for item in resultado:
#        f.write(item + '\n')

# 3 PARTE: PROCURAR A HASHc NO ARQUIVO E EXIBIR A SENHA CORRESPONDENTE
hash_encontrada = False
for item in resultado:
    partes = item.split(":")
# ESTRUTURA PARA VERIFICAR SE HA LINHAS MALFORMADAS
    if len(partes) == 2:
        senha, hash_gerado = partes
        if hash_gerado == hashc:
            print "\nSenha encontrada:", senha
            hash_encontrada = True
            break

if not hash_encontrada:
    print "\nSenha nao encontrada!"
