def ordena_string(palavra):
    pala_list = list(palavra)

    for i in range(0, len(pala_list)):
        for j in range(0, len(pala_list)):
            if (ord(pala_list[j]) > ord(pala_list[i])):
                aux = pala_list[j]
                pala_list[j] = pala_list[i]
                pala_list[i] = aux
    return ''.join(pala_list)

palav = 'picos'
print(f'Palavra original: {palav}\nPalavra ordenada: {ordena_string(palav)}')