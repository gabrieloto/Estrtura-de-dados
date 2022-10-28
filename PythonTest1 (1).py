class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
               
class Fila_super:
    def __init__(self):
        self.head = None
    
    def enqueue(self, client):
        if self.tail.next is None:
            self.head = client 

    def push(self, cliente):
        new_node = Node(cliente)
        if self.head == None:
            self.head = new_node
            return
        aux = self.head
        while aux.next != None:
            aux = aux.next
        aux.next = new_node    

    def printNome(self):
        print()
        aux = self.head
        contador = 0
        while aux != None:
            contador += 1
            print(contador, "º cliente: ",aux.data[0], sep="")
            aux = aux.next

    def pagar(self):
        aux = self.head
        if aux != None:
            self.head = self.head.next
            print("\nO cliente", aux.data[0], "comprou", aux.data[1], "produtos, e irá pagar", aux.data[2], "R$\n")
            del aux

fila_super = Fila_super()
compra = 0
produt = 0
option = 4

print("___BEM VINDO AO SUPER MERCADO___")
while (option!= 3) :
    print("0 - comprar 1 kg de arroz.")
    print("1 - comprar 1 kg de feijao.")
    print("2 - comprar 1kg de carne.")
    print("3 - finalizar compras.")
    option = int(input("oque vc vai escolher?"))
    if option == 3:
        option = 4
        murrinha = int(input("só vai comprar isso?\n 0 para sim\n 5 para não\n"))
        if murrinha == 0:
            name = input("obrigado por comprar, qual o seu nome?:")
            fila_super.push([name, produt, compra])
            print("então",name,"você comprou",produt,"produtos e sua",compra,"R$.agora pode se encaminhar para pagar.\n")
            while(murrinha < 3 or murrinha > 4):
                print("0 - atender um cliente")
                print("1 - imprimir lista de clientes")
                print("2 - voltar para o Menu do cliente")
                print("3 - para encerrar o dia")
                murrinha = int(input("oque vc vai escolher?"))
                if murrinha == 0:
                    fila_super.pagar()
                elif murrinha == 1:
                    fila_super.printNome()
                elif murrinha == 2:
                    murrinha = 4
                elif murrinha == 3:
                    option = 3
                
    elif option == 0:
        produt = produt +1
        compra = float(compra + 4.50)
    elif option == 1:
        produt = produt +1
        compra = float(compra + 9.69)
    elif option == 2:
        produt = produt +1
        compra = float(compra + 37.54)
    else:
        print("selecione de novo pfv, deu erro.\n")