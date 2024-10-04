#Faça um programa para o cálculo de uma folha de pagamento, 
#sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
#e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#alário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
#dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220
salario_b = float(input("Me diga o seu salário bruto: .2f"))
salario_fgts = salario_b*(0.11)
sindicato = salario_b*(0.03)

if (salario_b < 900):
    desconto = 0/salario_b
    
if (salario_b >= 900 and salario_b < 1500):
    desconto = salario_b - (5/100*salario_b)
    
if (salario_b >= 1500 and salario_b < 2500):
    desconto = salario_b - (10/100*salario_b)

if (salario_b >= 2500):
    desconto = salario_b - (20/100*salario_b)

desconto_t = (salario_fgts+sindicato+desconto)

salario_l = salario_b - desconto_t

print("Seu salário bruto é: ", salario_b)
print("Seu desconto do FGTS é: ", salario_fgts)
print("Seu desconto do sindicato é: ", sindicato)
print("Seu valor pago para o imposto de Renda é: ", desconto)
print("Seu salário liquido é: ", salario_l)
