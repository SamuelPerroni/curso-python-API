from abc import ABC, abstractclassmethod

class ItemCardapio(ABC):
    def __init__(self, nome: str, preco: float) -> None:
        self._nome = nome
        self._preco = preco
        
    @abstractclassmethod
    def aplicar_desconto(self):
        ...