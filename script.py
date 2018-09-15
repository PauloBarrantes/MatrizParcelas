

matrizInicial = [
[842,844,808,822,979,954,965,906,898,856],
[803,841,870,970,943,914,916,836,858,926],
[773,782,860,822,932,971,765,875,853,936],
[912,887,815,937,844,661,841,844,809,778],
[874,792,803,793,818,799,767,855,792,858],
[908,875,899,788,867,790,831,757,751,774],
[875,907,921,963,875,880,898,802,874,928],
[891,928,871,875,865,777,738,796,855,901],
[823,784,754,873,764,775,752,753,720,798],
[785,794,764,822,714,748,724,717,736,724]
]

from tkinter.filedialog import askopenfilename

import openpyxl
#filename = askopenfilename()
#print(filename)

#doc = openpyxl.load_workbook('/Users/paulobarrantes/Proyectos/MatrizParcelas/Test1.xlsx')
#archivo
#doc = openpyxl.load_workbook('address.xls')
def calcularMatrices(largo, ancho):

    nFilas = 10
    nColumnas = 10
    '''
    matrizInicial = [
        [2,2,3,4,5,6],
        [5,62,3,2,8,6],
        [4,6,3,1,8,4],
        [9,1,4,0,2,5],
        [1,3,4,1,3,10],
        [0,1,1,84,2,5]
    ]'''
    matrizNueva = []
    l = largo
    a = ancho
    columna = 0
    filas = 0
    for i in range(0, nFilas,largo):
        print("Resultado", int(nFilas/largo))
        for j in range(0, nColumnas,ancho):

            value = 0
            for a in range(i,i+largo,1):
                for b  in range(columna, columna + ancho, 1):
                    value = value + matrizInicial[a][b]

            print (value)
            if columna == 0:
                matrizNueva.append([value])
            else:
                matrizNueva[filas].append(value)
            columna = columna + ancho
        filas = filas+1
        columna = 0
    print(matrizNueva)
    for x in range(0,5):
        for y in range(0,10):
            print(matrizNueva[x][y],' - ' ,end='')
        print()
calcularMatrices(2,1)
