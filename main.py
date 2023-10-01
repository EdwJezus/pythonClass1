print ('Atividade 1')
print ('')

salario = int(input('Qual o salario? '))
if salario <= 280:
  porce = (salario * 0.2)
  print ('O percentual de aumento aplicado: 20%')
elif salario >= 280.01 and salario <= 700:
  porce = (salario * 0.15)
  print ('O percentual de aumento aplicado: 15%')
elif salario >= 700.01 and salario <= 1500:
  porce = (salario * 0.1)
  print ('O percentual de aumento aplicado: 10%')
elif salario >= 1500.01:
  porce = (salario * 0.05)
  print ('O percentual de aumento aplicado: 5%')

aumento = (salario + porce)
print ('O Salario antes do reajuste: ','R$' ,salario)
print ('O Valor do aumento: ' ,'R$' , porce)
print ('O Novo salario, após o reajuste:','R$' ,aumento)
print ('')

##############

print ('Atividade 2')
print ('')
dia = int(input('Qual o número? '))
if dia == 1:
  print ('Domingo')
elif dia == 2:
  print ('Segunda-feira')
elif dia == 3:
  print ('Terça-feira')
elif dia == 4:
  print ('Quarta-feira')
elif dia == 5:
  print ('Quinta-feira')
elif dia == 6:
  print ('Sexta-feira')
elif dia == 7:
  print ('Sabádo')
else:
  print ('Valor Invalido')
print ('')

###########################

print ('Atividade 3')
print ('')
freq = int(input('Frequência: '))
if freq >= 0 and freq <= 100:
  if freq <= 75:
    print ('Reprovado(a) por falta de frequência.')
  else:
    g1 = float(input('G1: '))
    if g1 >= 0 and g1 <= 10:
      print ('Ok.')
    g2 = float(input('G2: '))
    if g2 >= 0 and g2 <= 10:
      print ('Ok.')
    g = (g1 + g2)
    gtotal = (g//2)
    if gtotal >= 6:
      print ('Aprovado(a) com média:' , gtotal)
    elif max(g1 , g2) < 2:
      print ('Reprovado(a) por insuficiência de nota.')
#######Substituição
    elif gtotal < 6 and g1 < g2:
      print ('Precisa substituir G1 e deve tirar <nota necessária>')
    elif gtotal < 6 and g2 < g1:
      print ('Precisa substituir G2 e deve tirar <nota necessária>')
    elif gtotal < 6 and g1 == g2:
      print ('O(a) aluno(a) pode escolher o grau a substituir e deve tirar <nota necessária>.')
    else:
      print ('Reprovado(a).')
