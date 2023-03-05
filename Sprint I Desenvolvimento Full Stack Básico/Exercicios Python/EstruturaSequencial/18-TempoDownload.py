"""
    Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))

velocidade_link = float(input("Digite a velocidade do link contratado em Mbps: "))


tempo_download_min = (tamanho_arquivo / velocidade_link) / 60


print(f'Tempo estimado para download: {tempo_download_min} minutos')


