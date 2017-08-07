#ネルシフラン -- My name in japanese.XD
#Nelcifran
import sys
class avlnode(object): # nó na arvoré avl
    
    def __init__(self,key):
        
        self.key = key
        self.left = None
        self.right = None
        
    def __str__(self):
        
        return str(self.key)
    
    def __repr__(self):
        
        return str(self.key)

class avltree(object):
    
    def __init__(self):
        
        self.node = None # raiz da arvoré
        self.height = -1 # altura da arvoré
        self.balance = 0 # fator de balanceamaneto
        
    def insert(self,key):
        
        #criando nó
        n = avlnode(key)
        # iniciando a arvoré
        if not self.node:
            self.node = n
            self.node.left = avltree()
            self.node.right = avltree()
        # inserindo  a key na subarvoré esquerda
        elif key<self.node.key:
            self.node.left.insert(key)
          #inserindo a key na subarvoré direita
        elif key > self.node.key:
            self.node.right.insert(key)

        #rebalanciando a arvore se necessário
        self.rebalance()
        
    def rebalance(self):# rebalanceamento da arvoré.Após  inserir ou deletar um nó
        # checando se é necessário rebalancear a arvoré
        self.update_heights(recursive = False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            #subarvoré esquerda é maior que subarvoré direita
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()
                    
                self.rotate_right()
                self.update_heights()
                self.update_balances()
            #subarvoré esquerda é maior que subarvoré esquerda
            if self.balance< -1:

                if self.node.right.balance > 0:

                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()

                self.rotate_left()
                self.update_heights()
                self.update_balances()
                
    def update_heights(self, recursive = True):
        # atualizando o tamanho da arvoré
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()
            self.height = 1 + max(self.node.left.height,self.node.right.height)
        else:
            self.height = -1

    def update_balances(self,recursive = True):
        # calculando o fator de balanceamento da arvoré
        #balanço = tamanho da subarvoré esquerda - tamanho da subarvoré direita
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()
            self.balance = self.node.left.height - self.node.right.height      
        else:
            self.balance = 0

    def rotate_right(self):
        # rotação á direita
         new_root = self.node.left.node
         new_left_sub = new_root.right.node
         old_root = self.node

         self.node = new_root
         old_root.left.node = new_left_sub
         new_root.right.node = old_root

    def rotate_left(self):
        #rotação á esquerda
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def delete(self,key):
        #deletando  key da arvoré
        if self.node != None:
            if self.node.key == key:
                # a chave é encontrada em um nó folha,apenas tiro esse cara
                if not self.node.left.node and not self.node.right.node:
                    self.node = None
                    
                elif not self.node.left.node:
                    self.node = self.node.right.node
                    
                elif not self.node.right.node:
                    self.node = self.node.left.node
                    
                else:
                    
                    successor = self.node.right.node
                    
                    while successor and successor.left.node:
                        successor = successor.left.node
                        
                    if successor:
                        
                        self.node.key = successor.key
                        self.node.right.delete(successor.key)
                        
            elif key < self.node.key:
                self.node.left.delete(key)

            elif key > self.node.key:
                self.node.right.delete(key)
            # rabalanceando
            self.rebalance()
        
    def inorder_traverse(self):
            #subarvoré esquerda - raiz - subarvoré direita
        result = []
        
        if not self.node:
            return result

        result.extend(self.node.left.inorder_traverse())
        result.append(self.node.key)
        result.extend(self.node.right.inorder_traverse())
        return result
    
    def display(self,node = None,level = 0):
        
        if not node:
            node = self.node
            
        if node.right.node:
            
            self.display(node.right.node,level+1)
            print(('\t'* level),(' /'))
            
        print(('\t'*level),node)
        
        if node.left.node:
            print(('\t'*level),(' \\'))
            self.display(node.left.node, level +1)


def Incluir(dicion):
    Palavra = str(input("Digite a palavra:"))
    dicion.append(Palavra)
    for key in dicion:
        tree.insert(key)

def Excluir(dicion):
    word = str(input("Digite a palavra a ser excluida:\n"))
    for key in [word]:
        tree.delete(key)
        #tree.inorder_traverse()
    else:
        print("Palavra não está no dicionário\n")
    
        
def Impressão():
    
    print(tree.inorder_traverse())
    print("\n")
    tree.display()

if __name__ == "__main__":
    
    dicion  = []
    tree = avltree()
    while True:
        print("\n")
        print("1 - Inserir Palavra\n2 - retirar palavra\n3 - Impressão em in order\n4 - Sair\n\n")
        
        escolha = ''
        while not isinstance(escolha,int):
            escolha = input("Escolha:\n")
            try:
                escolha = int(escolha)
            except ValueError:
                print("Digite um numero!!")
        if escolha == 1:
            
            Incluir(dicion)
           
        elif escolha == 2:
            
            Excluir(dicion)
            
        elif escolha == 3:
            
            Impressão()
            
        elif escolha == 4:
            print("Bye...Bye!!\n")
            sys.exit(0)
        else:
            print("Escolha incorreta\n")
#---------------------------------------------------------------     
'''tree = avltree()
dicion = [1,2,3,4,5,6,7,8,9,10,15]

for key in dicion:
    tree.insert(key)
print(tree.inorder_traverse())
print("Deletando \n")
for key in [1,9,7,15]:
    #print("Entrei\n\n")
    #if key == 'alicate':
        #x = dicion.index('alicate')
        #del dicion[x]
    tree.delete(key)
print(tree.inorder_traverse())
tree.display()
'''
