import re

'''
TODO:
    Usar with no open file.
    Ordernar por qtd de repetições em ordem decrescente.
'''

"""
No lugar do bubble sort, poderia ter sido utilizado
import operator
sorted(wc.iteritems(), reverse=True, key=operator.itemgetter(1))
"""

def pw(x):
    """
    Função para limpar a palavra,
    removendo pontuação e
    convertentendo em lowercase.
    
    Ex.: teStE,.- => teste
    """
    w = re.search(r'\w+', x)
    if w != None:
        x = w.group(0)
    return x.lower()

def main():
    try:
        f = open('input.txt', 'rU')
        wc = {}

        """
        Realiza a contagem de ocorrências de cada palavra
        e as adiciona em um dicionário (wc).
        """
        for line in f:
            words = line.split()
            for w in words:
                x = pw(w)
                if x in wc.keys():
                    wc[x] += 1
                else:
                    wc[x] = 1
        
        f.close()

        """
        Converte o dicionário em uma lista
        para viabilizar ordenação por valores.
        """
        lista = []
        for w in wc:
            lista.append((w, wc[w]))

        """
        Aplica um bubble sort na lista ordenando
        por número de ocorrências de palavras em
        ordem decrescente.
        """
        change = True
        aux = []
        while change:
            change = False
            for i in range(len(lista)-2):
                if lista[i][1] < lista[i+1][1]:
                    aux = lista[i+1]
                    lista[i+1] = lista[i]
                    lista[i] = aux
                    change = True

        """
        Imprime as palavras com maior número de ocorrências
        """
        for x in range(20):
            if len(lista) > x:
                print ("{:10}: {:5}".format(lista[x][0], lista[x][1]))
        
    except:
        print("Erro!")

main()
