list_Unidades= ['"',('Un','Uno'),'Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho','Nueve']; list_de_diez =['',('Diez','Once','Doce','Trece','Catorce','Quince','Dieciseis','Diecisiete','Dieciocho','Diecinueve'),('Veinte','Venti'),('Treinta','Treinta y'),('Cuarenta','Cuarenta y'),('Cincuenta','Cincuenta y'),('Sesente','Sesenta y'),('Setenta','Setenta y'),('Ochenta','Ochenta y'),('Noventa','Noventa y')];
list_de_cien = ["",('Cien','Ciento'),'Doscientos','Trecientos','Cuatrocientos','Quinientos','Seiscientos','Sieteciento','Ochocientos','Novecientos'];
list_miles = [("",""),('Mil','Mil'),('Millon','Millones'),('Billon','Billones')];

def numero_a_letras(num):
    num_entero = int(num)
    numero_letras = ""
    letras = ""
    cont = 0
    while(num_entero > 0):
        n = num_entero % 1000
        if(cont == 0):
            letras = convert_num_at_let(n, 1).strip()
        else:
            letras = convert_num_at_let(n, 0).strip()
        if(n == 0):
            numero_letras = letras + " " + numero_letras
        if( n == 1):
            if(cont > 1 and cont <= 3):
                numero_letras = list_miles[cont][0]+" "+numero_letras
            else:
                numero_letras = letras+" "+list_miles[cont][0]+ " " + numero_letras
        else:
            numero_letras = letras+" "+list_miles[cont][1]+ " " + numero_letras
        cont = cont + 1
        numero_letras = numero_letras.strip()
        num_entero = int(num_entero / 1000)
    numero_letras = numero_letras.strip()
    print(numero_letras)

def convert_num_at_let(num, val):
    txt_cien = ""
    txt_des = ""
    txt_unidades = ""
    cienAmil = int (num / 100)
    diezAcien = int((num -(cienAmil * 100))/10)
    unoAnueve = int(num - (cienAmil * 100 + diezAcien * 10))
    txt_cien  = list_de_cien[cienAmil]
    if(cienAmil == 1):
        if(diezAcien == 0 and unoAnueve == 0):
            txt_cien = txt_cien[0]
        else:
            txt_cien = txt_cien[1]
    txt_des = list_de_diez[diezAcien]
    if(diezAcien == 1):
        txt_des = txt_des[unoAnueve]
    elif(diezAcien > 1):
        if(unoAnueve != 0):
            txt_des = txt_des[1]
        else:
            txt_des = txt_des[0]
    if(diezAcien != 1):
        txt_unidades = list_Unidades[unoAnueve]
        if(unoAnueve == 1):
            txt_unidades = txt_unidades[val]
    return "%s %s %s" %(txt_cien,txt_des,txt_unidades)

## Permmite que el usuario ingresé un numero entero
## Obtiene el valor 
num = int(raw_input("Ingrese un numero entero: "))
numero_a_letras(num)
