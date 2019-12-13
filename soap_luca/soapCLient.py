from zeep import Client

client = Client(wsdl='http://www.dneonline.com/calculator.asmx?wsdl')

a = raw_input("Digite o A: ")
b = raw_input("Digite o B: ")

run = True
res = ''
while run:
    print("operacoes: sum | sub | mul | div")
    res = raw_input("Digite qual a operacao: ")
    if res == 'sum':
        print(client.service.Add(a,b))

    elif res == 'mul':
        print(client.service.Multiply(a,b))

    elif res == 'sub':
        print(client.service.Subtract(a,b))

    elif res == 'div':
        print(client.service.Divide(a,b))
