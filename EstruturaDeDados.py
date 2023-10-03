#Imports
from collections import deque

#================================================#

#Ordenação por Seleção:
def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoporSelecao([5, 3, 6, 2, 10]))

#================================================#

#Recursão:
def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_caixa():
            print("Achei a Chave!")

#================================================#

#Pilha:
def sauda(nome):
    print ("Olá, " + nome + "!")
    sauda2(nome)
    print("Preparando para dizer tchau...")
    tchau()

def sauda2(nome):
    print("Como vai " + nome + "?")

def tchau():
    print("ok, tchau!")

sauda("Luiz")

#================================================#

#Pilha Recursiva:
def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)
      
print(fat(3))

#================================================#

#Quicksort:
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array [1:] if i <= pivo]
        maiores = [i for i in array [1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10, 5, 2, 3]))

#================================================#

#Mergesort:
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    #Divide a lista em duas metades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    #Recursivamente ordena as metades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    #Combina (funde) as metades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    #Adiciona os elementos restantes, se houver
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

print(merge_sort([10, 5, 2, 3]))

#================================================#

#Tabelas Hash (Dicionário em python)
voted = {}

def verifica_eleitor(nome):
    if voted.get(nome):
        print("Mande embora!")
    else:
        voted[nome] = True
        print("Deixe votar")

verifica_eleitor("Myrthes")
verifica_eleitor("Luiz")
verifica_eleitor("Luiz")

#================================================#

#Grafos:

#Busca em largura:
grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

def pesquisa(nome):
  fila_de_pesquisa = deque()
  fila_de_pesquisa += grafo[nome]
  verificadas = []

  while fila_de_pesquisa:
    pessoa = fila_de_pesquisa.popleft()
    if not pessoa in verificadas:
      if pessoa_e_vendedor(pessoa):
        print(pessoa + " é um vendedor de manga!")
        return True
      else:
        fila_de_pesquisa += grafo[pessoa]
        verificadas.append(pessoa)
  return False

def pessoa_e_vendedor(nome):
  return nome[-1] == "m"

pesquisa("voce")

#================================================#

#Busca em largura:
def busca_em_largura(grafo, inicio):
  visitados = set()
  fila = deque([inicio])
  visitados.add(inicio)

  while fila:
    vertice = fila.popleft()
    print(vertice, end=" ")
    for vizinho in grafo[vertice]:
      if vizinho not in visitados:
        fila.append(vizinho)
        visitados.add(vizinho)

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

busca_em_largura(grafo, 'A')

#================================================#

#Dijkstra:
#Grafo com custos nas arestas
grafo1 = {
    "0": {"1": 1, "2": 3, "5": 6},
    "1": {"2": 1},
    "2": {"3": 1},
    "3": {"4": 1},
    "4": {"5": 1},
    "5": {}
}

#a = 0 b =1 c= 2 d=3

grafo = {
    "0": {"1": 1, "2": 4},
    "1": {"2": 2, "3": 5},
    "2": {"3": 1},
    "3": {},
}

#Vértice inicial
inicio = "0"

#Inicialização das estruturas de dados
infinito = float("inf")
custos = {vertice: infinito for vertice in grafo}
custos[inicio] = 0

pais = {vertice: None for vertice in grafo}

processados = []

#Função para encontrar o vértice com o custo mais baixo
def ache_no_custo_mais_baixo(custos, processados):
    custo_mais_baixo = infinito
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos, processados)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos:
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos, processados)

#Imprimir os resultados
for vertice in custos:
    print(f"Menor custo para chegar ao vértice {vertice}: {custos[vertice]}")

#Encontrar e imprimir o caminho mínimo do vértice "0" ao vértice "5"
caminho_minimo = []
vertice_atual = "3"  # Vértice de destino
while vertice_atual is not None:
    caminho_minimo.insert(0, vertice_atual)
    vertice_atual = pais[vertice_atual]

print("Caminho mínimo:", caminho_minimo)

#================================================#

#Bellman-Ford:
class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def adiciona_aresta(self, u, v, w):
        self.grafo.append([u, v, w])

    def imprime_distancias(self, dist):
        print("Vertice \t Distancia do Vertice Inicial")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

    def bellman_ford(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.grafo:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.grafo:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("O grafo contem um ciclo de peso negativo")
                return

        self.imprime_distancias(dist)


g = Grafo(5)
g.adiciona_aresta(0, 1, -1)
g.adiciona_aresta(0, 2, 4)
g.adiciona_aresta(1, 2, 3)
g.adiciona_aresta(1, 3, 2)
g.adiciona_aresta(1, 4, 2)
g.adiciona_aresta(3, 2, 5)
g.adiciona_aresta(3, 1, 1)
g.adiciona_aresta(4, 3, -3)

g.bellman_ford(0)

#================================================#

#Floyd-Warshall:
INF = float("inf")

def floyd_warshall(graph):
    V = len(graph)
    dist = [[INF] * V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

result = floyd_warshall(graph)
for row in result:
    print(row)

#================================================#

#Algoritmo guloso:
def selecionar_atividades(atividades):
    #Supõe que as atividades estão ordenadas pelo tempo de término
    atividades.sort(key=lambda x: x[1])
    
    selecionadas = [atividades[0]]
    hora_final = atividades[0][1]
    
    for atividade in atividades[1:]:
        inicio, fim = atividade
        if inicio >= hora_final:
            selecionadas.append(atividade)
            hora_final = fim
    
    return selecionadas

#Exemplo de uso
atividades = [(1, 3), (2, 5), (3, 8), (5, 9), (8, 10)]
atividades_selecionadas = selecionar_atividades(atividades)
print("Atividades selecionadas:", atividades_selecionadas)

#================================================#

#Programação dinamica:
def problema_mochila(capacidade, pesos, valores, n):
    #Inicializa uma tabela para armazenar os resultados intermediários
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    #Preenche a tabela usando a abordagem bottom-up
    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]

#Exemplo de uso
capacidade_mochila = 10
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
numero_itens = len(pesos)

resultado = problema_mochila(capacidade_mochila, pesos, valores, numero_itens)
print("Maior valor possível na mochila:", resultado) 
