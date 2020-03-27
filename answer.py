# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:12:03 2020

@author: Juan Rojas
"""
carga = 0
#Capacidad de carga del Antonov An-225 es de 250000kg, 250000*15%=237500
while carga < 237500 :
    kg= int(input("Ingrese peso del paquete"))
    km= int(input("ingrese distancia del paquete"))
    if kg > 10:
        tdv = int(input("digite 1 si es intercontinental"))
        if tdv == 1:
            ml = km/1,6
            p = kg*4500 + ml*8000
            if kg>400 and km>8000:
                pti= p*10/100
                print("el precio es",pti)
            else:
                pti = p
                print("el precio es",pti)
        else:
            p = kg*4500+km*4000
            if kg>100:
                pti= p*15/100
                print("el precio es",pti)
            else:
                pti=p
                print("el precio es",pti)
                
    else:
        print("el paquete no pesa mas de 10kg")
             
              
        
            
                
    
         
         
             
        
              
        

    
    



