from PyPDF2 import PdfFileReader, PdfFileWriter

caminho1 = "Separar arquivos/1 (" #exemplo da pasta + o nome do arquivo
caminho2 = ").pdf" #final do nome do arquivo
numero = 1 #contador para o próximo numero
total = 319 #total de arquivos a separar

while numero <= total:

    print('Iniciou PDF ' + str(numero))
    caminho = caminho1 + str(numero) + caminho2 #Criando o caminho final
    pdf_file = open(caminho, 'rb')  #acessando o arquivo com o separador de PDF
    pdf_reader = PdfFileReader(pdf_file)

    numpaginas = pdf_reader.getNumPages() #total de paginas do PDF aberto

    #função para extrair pagina a pagina
    for i in range (numpaginas):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(i))
        separado = open('Separar arquivos/Separados/NewComp' + str(numero) + 'pag' + str(i+1) + '.pdf','wb') #escolhendo a nomenclatura do novo arquivo, bem como o caminho dele
        pdf_writer.write(separado) #salvando o arquivo novo
        separado.close()

    print('pdf numero ' + str(numero) + ' finalizado')
    numero = numero + 1 #indo para o próximo arquivo PDF
    pdf_file.close()
