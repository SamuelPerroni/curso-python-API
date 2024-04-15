from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str, tipo: str, tamanho: str) -> None:
        super().__init__(nome, preco)
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho
    def __str__(self) -> str:
        return self._nome    
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)