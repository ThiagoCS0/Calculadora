txRes=""

def calculadora (v1,v2,op):
  if(op==1):
    txRes="Soma, "+str(v1)+"+"+str(v2)+", é "+str(v1+v2)
  elif(op==2):
    txRes="Subtração, "+str(v1)+"-"+str(v2)+", é "+str(v1-v2)
  elif(op==3):
    txRes="Multiplicação, "+str(v1)+"*"+str(v2)+", é "+str(v1*v2)
  elif(op==4):
    txRes="Divisão, "+str(v1)+"/"+str(v2)+", é "+str(v1/v2)
  print("\nResultado da",txRes)

v1=int(input("Valor 1:"))
v2=int(input("Valor 2:"))
print("Escolha a operação:\n\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão")
op=int(input("Operação:"))
calculadora (v1,v2,op)