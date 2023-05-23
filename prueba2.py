dcto_auxiliar=0.15
dcto_admin=0.10
dcto_docente=0.5
valor_CarillasP=250.000
valor_Impl_dent=475.000
valor_brackets=800.000
print("----------------------------------------------------")
print("--> Tratamiento(s) Carillas porcelana $250.000")
print("--> Tratamiento(s) Implantes dentales $475.000")
print("--> Tratamiento(s) Ortodoncia brackets $800.000")
print("----------------------------------------------------")
while True:
    try:
        valor_CarillasP=int(input("Cuantas tratamientos de carillas de porcelana desea: "))
        if valor_CarillasP<0:
            raise ValueError()
        break 
    except ValueError:
        while True:   
         print("ingrese una opción valida")
         while True:
            try:
               valor_Impl_dent=int(input("Cuantos tratamientos de implantes dentales desea: "))
               if valor_Impl_dent<0:
                  raise ValueError()
               break
            except ValueError:
               print("Ingrese una opcion valida")
               while True:
                  try: 
                     valor_brackets=int(input("Cuantos tratamientos de brackets desea"))
                     if valor_brackets<0:
                        raise ValueError()
                     break
                  except ValueError:
                     print("Ingrese una opcion valida")
                     subtotal=valor_CarillasP+valor_Impl_dent+valor_brackets
                     if dcto_auxiliar==1:#Auxiliar
                        descuento=dcto_auxiliar*subtotal

                  