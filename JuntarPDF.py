import PyPDF2
import os

# Instânciando o merge
merger = PyPDF2.PdfMerger()

# Listando os arquivos selecionados
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
# print(lista_arquivos)

# Percorrendo os arquivos da pasta
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

# Gerando o PDF final
merger.write("PDF Final.pdf")
print("Junção finalizada!")