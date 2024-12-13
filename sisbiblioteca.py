class Livro:
    def __init__(self, titulo:str, autor:str, isbn:str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.quantidade = 1
        #nao estao privados, podem ser acessos pela classe e por fora

    def adicionar_exemplar(self, quantidade: int) -> None:
        self.quantidade += quantidade


    def remover_livro(self, quantidade: int) -> None:
        self.quantidade -= quantidade #é considerado um procedimento porque não tem "return"

    def __str__(self) -> str: #o __str__ é um método definido que já retorna tudo como str
        return self.titulo, self.autor, self.isbn, self.quantidade
        # é um método que funciona como função

class Usuario:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        livros_emprestados = []

    def emprestar_livro(self, livro: Livro):
        livro = Livro()
        self.livros_emprestrados.append(livro)
        livro.remover_livro(1) 

        
        
        

        


