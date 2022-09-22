# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:56:56 2022

@author: Usuario
"""
import random
plantas=0
bacterias=0
agua=0

A1=random.randint(1,4)
if A1==3 or A1==4:
    A1="B"
else:
    if A1==1:
        A1="P"
    else:
        if A1==2:
            A1="A"
            
A2=random.randint(1,4)
if A2==3 or A2==4:
    A2="B"
else:
    if A2==1:
        A2="P"
    else:
        if A2==2:
            A2="A"
            
A3=random.randint(1,4)
if A3==3 or A3==4:
    A3="B"
else:
    if A3==1:
        A3="P"
    else:
        if A3==2:
            A3="A"
A4=random.randint(1,4)
if A4==3 or A4==4:
    A4="B"
else:
    if A4==1:
        A4="P"
    else:
        if A4==2:
            A4="A"
            
B1=random.randint(1,4)
if B1==3 or B1==4:
    B1="B"
else:
    if B1==1:
        B1="P"
    else:
        if B1==2:
            B1="A"

B2=random.randint(1,4)
if B2==3 or B2==4:
    B2="B"
else:
    if B2==1:
        B2="P"
    else:
        if B2==2:
            B2="A"            
            
B3=random.randint(1,4)
if B3==3 or B3==4:
    B3="B"
else:
    if B3==1:
        B3="P"
    else:
        if B3==2:
            B3="A"

B4=random.randint(1,4)
if B4==3 or B4==4:
    B4="B"
else:
    if B4==1:
        B4="P"
    else:
        if B4==2:
            B4="A"
C1=random.randint(1,4)
if C1==3 or C1==4:
    C1="B"
else:
    if C1==1:
        C1="P"
    else:
        if C1==2:
            C1="A"

C2=random.randint(1,4)
if C2==3 or C2==4:
    C2="B"
else:
    if C2==1:
        C2="P"
    else:
        if C2==2:
            C2="A"
C3=random.randint(1,4)
if C3==3 or C3==4:
    C3="B"
else:
    if C3==1:
        C3="P"
    else:
        if C3==2:
            C3="A"
C4=random.randint(1,4)
if C4==3 or C4==4:
    C4="B"
else:
    if C4==1:
        C4="P"
    else:
        if C4==2:
            C4="A"
D1=random.randint(1,4)
if D1==3 or D1==4:
    D1="B"
else:
    if D1==1:
        D1="P"
    else:
        if D1==2:
            D1="A"

D2=random.randint(1,4)
if D2==3 or D2==4:
    D2="B"
else:
    if D2==1:
        D2="P"
    else:
        if D2==2:
            D2="A"
D3=random.randint(1,4)
if D3==3 or D3==4:
    D3="B"
else:
    if D3==1:
        D3="P"
    else:
        if D3==2:
            D3="A"
D4=random.randint(1,4)
if D4==3 or D4==4:
    D4="B"
else:
    if D4==1:
        D4="P"
    else:
        if D4==2:
            D4="A" 
            
print("/",A1,"/",B1,"/",C1,"/",D1,"/")
print("/",A2,"/",B2,"/",C2,"/",D2,"/")
print("/",A3,"/",B3,"/",C3,"/",D3,"/")
print("/",A4,"/",B4,"/",C4,"/",D4,"/")
print("")
                                    
if A1=="P":
    plantas=plantas+1
else:
    if A1=="A":
        agua=agua+1
    else: 
        if A1=="B":
           bacterias=bacterias+1
           
if A2=="P":
    plantas=plantas+1
else:
    if A2=="A":
        agua=agua+1
    else: 
        if A2=="B":
           bacterias=bacterias+1
           
if A3=="P":
    plantas=plantas+1
else:
    if A3=="A":
        agua=agua+1
    else: 
        if A3=="B":
           bacterias=bacterias+1

if A4=="P":
    plantas=plantas+1
else:
    if A4=="A":
        agua=agua+1
    else: 
        if A4=="B":
           bacterias=bacterias+1

if B1=="P":
    plantas=plantas+1
else:
    if B1=="A":
        agua=agua+1
    else: 
        if B1=="B":
           bacterias=bacterias+1
           
if B2=="P":
    plantas=plantas+1
else:
    if B2=="A":
        agua=agua+1
    else: 
        if B2=="B":
           bacterias=bacterias+1
           
if B3=="P":
    plantas=plantas+1
else:
    if B3=="A":
        agua=agua+1
    else: 
        if B3=="B":
           bacterias=bacterias+1           
           
if B4=="P":
    plantas=plantas+1
else:
    if B4=="A":
        agua=agua+1
    else: 
        if B4=="B":
           bacterias=bacterias+1           
           
if C1=="P":
    plantas=plantas+1
else:
    if C1=="A":
        agua=agua+1
    else: 
        if C1=="B":
           bacterias=bacterias+1 
           
if C2=="P":
    plantas=plantas+1
else:
    if C2=="A":
        agua=agua+1
    else: 
        if C2=="B":
           bacterias=bacterias+1
          
if C3=="P":
    plantas=plantas+1
else:
    if C3=="A":
        agua=agua+1
    else: 
        if C3=="B":
           bacterias=bacterias+1

if C4=="P":
    plantas=plantas+1
else:
    if C4=="A":
        agua=agua+1
    else: 
        if C4=="B":
           bacterias=bacterias+1 

if D1=="P":
    plantas=plantas+1
else:
    if D1=="A":
        agua=agua+1
    else: 
        if D1=="B":
           bacterias=bacterias+1

if D2=="P":
    plantas=plantas+1
else:
    if D2=="A":
        agua=agua+1
    else: 
        if D2=="B":
           bacterias=bacterias+1

if D3=="P":
    plantas=plantas+1
else:
    if D3=="A":
        agua=agua+1
    else: 
        if D3=="B":
           bacterias=bacterias+1

if D4=="P":
    plantas=plantas+1
else:
    if D4=="A":
        agua=agua+1
    else: 
        if D4=="B":
           bacterias=bacterias+1             
print("El total de plantas es:",plantas)
print("El total de bacterias es:",bacterias)
print("El total de agua es:",agua)

print("")

print("El porcentaje de plantas es de",(plantas*100)/16,"%")
print("El porcentaje de bacterias es de",(bacterias*100)/16,"%")
print("El porcentaje de agua es de",(agua*100)/16,"%")

print("")

if plantas>bacterias>agua:
    print("El elemento con mayor ocurrencia son las plantas")
    print("El elemento con menor ocurrencia es el agua")
else: 
    if plantas>agua>bacterias:
        print("El elemento con mayor ocurrencia son las plantas")
        print("El elemento con menor ocurrencia son las bacterias")
    else:
        if bacterias>plantas>agua:
             print("El elemento con mayor ocurrencia son las bacterias")
             print("El elemento con menor ocurrencia es el agua")
        else:
            if bacterias>agua>plantas:
                print("El elemento con mayor ocurrencia son las bacterias")
                print("El elemento con menor ocurrencia son las plantas")
            else:
                if agua>bacterias>plantas:
                    print("El elemento con mayor ocurrencia es el agua")
                    print("El elemento con menor ocurrencia son las plantas")
                else:
                    if agua>plantas>bacterias:
                        print("El elemento con mayor ocurrencia es el agua")
                        print("El elemento con menor ocurrencia son las plantas")
                    else:
                           if agua>plantas==bacterias:
                              print("El elemento con mayor ocurrencia es el agua y existe un empate entre los elementos plantas y bacterias")
                           else: 
                               if agua<plantas==bacterias:
                                  print("El elemento con menor ocurrencia es el agua y existe un empate entre los elementos plantas y bacterias")
                               else:
                                   if plantas>bacterias==agua:
                                       print("El elemento con mayor ocurrencia son las plantas y existe un empate entre los elementos agua y bacterias")
                                   else:
                                       if plantas<bacterias==agua:
                                           print("El elemento con menor ocurrencia son las plantas y existe un empate entre los elementos agua y bacterias")
                                       else:
                                           if bacterias>agua==plantas:
                                               print("El elemento con mayor ocurrencia son las bacterias y existe un empate entre los elementos agua y plantas")
                                           else:
                                               if bacterias<agua==plantas:
                                                   print("El elemento con menor ocurrencia son las bacterias y existe un empate entre los elementos agua y plantas")
                                               else:
                                                   if bacterias==agua and plantas:
                                                       print("Existe un empate entre todos los elementos")
                                                     
print("")                                                       
if A1=="B" and A2=="B" and A3=="B" and B1=="B" and B3=="B" and C1=="B" and C2=="B" and C3=="B" and B2=="P":
   print("Existe una relacion planta bajo ataque")
else:
    if A1=="P" and A2=="P" and A3=="P" and B1=="P" and B3=="P" and C1=="P" and C2=="P" and C3=="P" and B2=="A":
        print("Existe una relacion Agua-Riesgo-Escasez")
    else:
        if B2=="B" and B3=="B" and B1=="B" and C3=="B" and C1=="B" and D1=="B" and D2=="B" and D3=="B" and C2=="P":
           print("Existe una relacion planta bajo ataque")
        else:
            if B2=="P" and B3=="P" and B1=="P" and C3=="P" and C1=="P" and D1=="P" and D2=="P" and D3=="P" and C2=="A":
                print("Existe una relacion Agua-Riesgo-Escasez")
            else:
                if A2=="B" and B2=="B" and A3=="B" and B4=="B" and A4=="B" and C2=="B" and C3=="B" and C4=="B" and B2=="P":
                    print("Existe una relacion planta bajo ataque")
                else:
                    if A2=="P" and B2=="P" and A3=="P" and B4=="P" and A4=="P" and C2=="P" and C3=="P" and C4=="P" and B2=="A":
                        print("Existe una relacion Agua-Riesgo-Escasez")
                    else:
                        if B2=="B" and B3=="B" and B4=="B" and C2=="B" and C4=="B" and D2=="B" and D3=="B" and D4=="B" and B2=="P":
                            print("Existe una relacion planta bajo ataque")
                        else:
                            if B2=="P" and B3=="P" and B4=="P" and C2=="P" and C4=="P" and D2=="P" and D3=="P" and D4=="P" and B2=="A":
                                print("Existe una relacion Agua-Riesgo-Escasez")
                            