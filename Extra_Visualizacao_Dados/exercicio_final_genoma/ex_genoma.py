
entrada = open("ex_genoma_bacteria.fasta").read()

entrada_humano = open("ex_genoma_human.fasta").read()

saida = open("bacteria.html", "w")  # saída em html
saida_humano = open("humano.html", "w")

# Vamos trabalhar com um dict:
cont = {}
cont_humano = {}

# uma letra pode ser A, T, C, G, total de 16 combinações entre elas
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0
        cont_humano[i+j] = 0
# assim gero 0 pares de cada combinação

entrada = entrada.replace("\n","")  # para tirar o erro da quebra de linha
entrada_humano = entrada_humano.replace("\n","")  # para tirar o erro da quebra de linha

for k in range(len(entrada) - 1): # k vai de 0 a 1700+-
    cont[entrada[k]+entrada[k+1]] += 1 # procura a letra atual e próx, com isso encontro um par e por isso soma a variavel dessa pos  
    cont_humano[entrada_humano[k]+entrada[k+1]] += 1

# HTML:

i = 1
for k in cont:
    transparencia = cont[k]/max(cont.values())
    transparencia_humano = cont_humano[k]/max(cont_humano.values())

    saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height: 100px;"
        + "float: left; background-color: rgba(0,0,0,"+str(transparencia)+"')>"+k+"</div>")

    saida_humano.write("<div style='width:100px; border:1px solid #111; color:#fff; height: 100px;"
        + "float: left; background-color: rgba(0,0,0,"+str(transparencia_humano)+"')>"+k+"</div>")

    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")  # força o html a fazer uma quebra de linha.
        saida_humano.write("<div style='clear:both'></div>")  # força o html a fazer uma quebra de linha.
    i += 1

saida.close()
saida_humano.close()