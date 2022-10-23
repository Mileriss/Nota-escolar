import os

#Local onde o usuário vai selecionar a máteria para calcular a média escolar
print("\n -CALCULADORA DE NOTAS ESCOLARES- \n")

selecionarMateria = input('Digite o NUMERO correpondente a materia que deseja visualizar as notas' 
                            + '\n1 - PORTUGUES' + '\n2 - MATEMATICA' + '\n3 - CIENCIAS' 
                            + '\n4 - GEOGRAFIA' + '\n5 - ED.FISICA' + '\n6 - HISTORIA'
                            + '\nDigite aqui: ')

materia = selecionarMateria

if (selecionarMateria == '1'): materia = 'Portugues'
if (selecionarMateria == '2'): materia = 'Matematica'
if (selecionarMateria == '3'): materia = 'Ciencias'
if (selecionarMateria == '4'): materia = 'Geografia'
if (selecionarMateria == '5'): materia = 'Ed.Fisica'
if (selecionarMateria == '6'): materia = 'Historia'

print(f'\nVoce selecionou: {materia}!\n')

os.system('pause'), os.system('cls')


#Função que vai realizar a soma entre a nota 1 e nota 2 e retornar a média do valor total
def ResultadoMedia():
    nota1 = 0
    print(f"Digite abaixo a primeira nota (Entre 0 - 10)")
    nota1 = float(input("Digite aqui: "))
    while (nota1 > 10): print("Nao sao permitidos valores maiores que 10!"); return 0

    nota2 = 0
    print(f"\nDigite abaixo a segunda nota (Entre 0 - 10)")
    nota2 = float(input("Digite aqui: "))
    while (nota2 > 10): print("Nao sao permitidos valores maiores que 10!"); return 0

    resultado = (nota1 + nota2)/2
    print(f"\nA sua media eh: {resultado} \n")

#Estrutura para verificar se a média final vai aprovar, reprovar ou deixar o aluno em recuperação
    if (resultado == 10):
        print("Voce tirou a nota maxima! \n")
    elif (resultado < 10 and resultado > 6):
        print(f"Voce passou em {materia} \n")
    elif (resultado < 6 and resultado > 4.5):
        print(f"Voce ficou de recuperacao em {materia} \n")
    else:
        print(f"Voce foi reprovado em {materia}")

ResultadoMedia()