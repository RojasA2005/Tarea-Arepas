aceite = float(input("¿Cuántas cucharadas de aceite?"))
aceite = round(aceite * 0.0634, 2)
sal = float(input("¿Cuántas cucharadas de sal?"))
sal = round(sal * 0.0634, 2)
agua = int(input("¿Cuántas cucharadas de agua?"))
harina = int(input("¿Cuántas cucharadas de harina?"))

bowl = sal + agua + harina
budare = bowl + aceite

cantidad_arepas = int(budare / 2)

print("Hiciste {} arepas!".format(cantidad_arepas))