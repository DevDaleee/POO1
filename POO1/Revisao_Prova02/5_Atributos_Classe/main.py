class A:
    var_class = 123
    
    def __init__(self):
        self.var_class = 321
    
a1 = A()
a2 = A()

#A.var_class = "Alterado "
#É possivel alterar variaveis de classe usando instancias, mas apenas para aquela instancia
a1.var_class = 321

#print(a1.__dict__)
#print(a2.__dict__)
#print(A.__dict__)
#print('\n')
print(a1.var_class)
print(a2.var_class)
print(A.var_class)