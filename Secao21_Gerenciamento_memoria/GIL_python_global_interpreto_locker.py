"""

É o conhecido como mutex/lock da computação (comum em C)

O GIL transforma o código python que permita somente uma thread em execução

Não é comum seu uso em programas de single thread
    Mas caso sejam multithread, seu uso é essencial (assim como qlqr mutex, por
    conta do acesso a memória compartilahda entre as threads [concorrência])

O sys.getrefcount(a) retorna a quantidade de referencias realizadas a var a

"""