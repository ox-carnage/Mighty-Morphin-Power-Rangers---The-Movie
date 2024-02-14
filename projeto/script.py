import sys
import re

def organizar_hexadecimal(entrada):
    # Encontrar todas as ocorrências de padrões hexadecimais no formato ($XX)
    padrao_hex = re.compile(r'\(\$[0-9A-Fa-f]+\)')
    valores_hex = padrao_hex.findall(entrada)

    # Organizar os valores hexadecimais
    valores_hex_organizados = sorted(valores_hex)

    # Substituir os valores hexadecimais no texto original com a formatação desejada
    for valor in valores_hex_organizados:
        valor_formatado = f'db {valor[2:-1]}'  # Remover os caracteres $() e adicionar db
        entrada = entrada.replace(valor, valor_formatado)

    return entrada

def salvar_em_arquivo(saida, conteudo):
    with open(saida, 'w') as arquivo_saida:
        arquivo_saida.write(conteudo)

if len(sys.argv) != 5:
    print("Uso correto: python script.py o ARQUIVO s SAIDA_DO_ARQUIVO.TXT")
    sys.exit(1)

comando, modo, arquivo_entrada, modo_saida, arquivo_saida = sys.argv

if modo != 'o' or modo_saida != 's':
    print("Modos não reconhecidos. Use 'o' para organizar e 's' para salvar.")
    sys.exit(1)

try:
    with open(arquivo_entrada, 'r') as arquivo_entrada:
        conteudo_entrada = arquivo_entrada.read()
except FileNotFoundError:
    print(f"O arquivo {arquivo_entrada} não foi encontrado.")
    sys.exit(1)

conteudo_organizado = organizar_hexadecimal(conteudo_entrada)

salvar_em_arquivo(arquivo_saida, conteudo_organizado)

print(f"Conteúdo com hexadecimais organizados e salvo em {arquivo_saida}.")
