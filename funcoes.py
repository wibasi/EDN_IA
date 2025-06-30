def calcular_volume_comprimento(comprimento, largura, altura):
    
    
    #Calcula o volume de um objeto retangular dado seu comprimento, largura e altura.
    
    #Args:
     #   comprimento (float): O comprimento do objeto.
      #  largura (float): A largura do objeto.
       # altura (float): A altura do objeto.
    
    #Returns:
        #float: O volume do objeto.
    return comprimento * largura * altura

volume = calcular_volume_comprimento(10,20,5)
print(volume)
