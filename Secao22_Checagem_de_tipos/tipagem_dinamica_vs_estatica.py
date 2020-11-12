"""

Tipagem dinâmica vs estática

O python tem tipagem dinâmica, ou seja, você não precisa definir o tipo da var
    Diferentemente de C ou Java
    Tipo de declaração implicita (inferência de tipos)

Os tipos do Python em dada variável se adaptam ao contexto, podem ser hora int
hora str, isso porque a alocação da memória é feita de forma completamente au-
tomática
    Porém há de se ter cuidado entre operações entre tipos diferentes
        Como int e str, o que não é possível. Mas só gera erro na execução!

Na tipagem dinâmica precisamos definir o tipo de forma clara e ela ocorre até
o final da execução, não é possível trocar os tipos
    Caso não estjea claro ou tenha problema, em tempo e compilação ele dá erro
"""