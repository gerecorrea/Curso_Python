"""
Métodos mágicos.

São todos os métodos que utilizam dunder (__)

Um exemplo simples é o dunder init -> __init__


"""
from __future__ import annotations

class Livro:

    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self) -> None:
        """Sobreescrevendo um método da classe Object."""
        return f"{self.titulo} escrito por {self.autor}."

    def __str__(self) -> str:
        """Método similar ao __repr__, se refere a saída visual ao usuário."""
        """O __str__ tem preferencia em relação ao __repr__, por isso a saída
        será a dele."""
        return self.titulo

    def __len__(self) -> int:
        """Puxa o método len() para a página e printa o num de pag."""
        return self.paginas

    def __del__(self) -> None:
        print('Um objeto do tipo Livro foi deletado da memória.')

    def __add__(self, outro: Livro):
        return f"{self} - {outro}"

    # São diversos os outros métodos que podemos modificar aqui dentro da clas-
    # se para adaptar ao contexto da nossa classe.


if __name__ == "__main__":
    livro1 = Livro('IA com Python', 'Trevis Trevoso', 144)
    livro2 = Livro('IA com C++', 'Trevis Trevoso Filho', 324)
    print(livro1)  # Retorna o tipo do objeto e o endereço de memória somente
    # Esse print acima é do método __repr__ da classe Obejct, como foi sobrees-
    # crito, então teremos uma nova saída, de acordo com o método sobreescrito
    
    print(len(livro1))
    print(livro1 + livro2)
    del livro1  # Deleta o objeto, igual visto anteriormente para outros obj.
    # É possível sobreescrever o método para modificá-lo, ainda
    # print(livro1)
    
    # Como tenho 2 objetos criados, aparece o del duas vezes, porque ao finali-
    #zar o código, o Python deleta automaticamente da memória
