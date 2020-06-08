# Do Procedural ao Orientado à Objetos

Este pacote contém o código final e inicial do exercício do curso.

Pratique seguindo o seu processo de implementação a partir do código inicial.

Abaixo listo mais sugestões de melhorias que você pode exercitar.

## Gráfo de Chamadas

Para gerar o grafo de chamadas como mostrado na aula, instale pacote:
 
```pip install pycallgraph2```

Então faça os ajustes necessários no script `callgraph.py` e execute:

```python callgraph.py image.png```

Fique livre para incrementar os filtros e configurações do grafo e compartilhe sua melhoria com os colegas. 

## Sugestões de melhorias
- Conclua a refatoração da classe GameOfLive.
- Transforme a lógica de GUI em uma classe App.
- Melhore o desenho da GUI usando bitmaps em vez de desenhar cada retângulo.
- Melhore o Board eliminando a lógica de visitar todos os vizinhos para cada célula. Isso pode ser feito com uma tabela de lookup que mantém atualizado o cálculo de vizinhos para cada célula na hora que a célula resnasce.
- Melhore o Board tornando sua representação mais eficiente com um array de bits.
- Adapte a função `region` para trabalhar mais próxima do `Coord`.

## Exemplo de "Procedural com Classes" vs "Orientado à Objetos"

- Procedural com Classes

```python
apples = [20, 4, 5, 10, 15]

class Sorted:
    def __init__(self, items):
        self.data = items

    def sort(self):
        self.data.sort()

    def get(self, index):
        return self.data[index]


def consumer1(cesta):
    """Pega a maçã mais pessada."""
    s = Sorted(cesta)
    s.sort()
    return s.get(-1)

print(consumer1(apples))
```

- Orientado à Objetos

```python
apples = [20, 4, 5, 10, 15]


class Balança:
    def __init__(self, items):
        self.data = items

    def mais_pesado(self):
        return max(self.data)


def consumer2(cesta):
    """Pega a maçã mais pessada."""
    s = Balança(cesta)
    return s.mais_pesado()


print(consumer2(apples))
```
