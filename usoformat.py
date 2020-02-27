#Este codigo define 3 distintas variables con sus respectivos valores, en el caso de "fltAreaTriangulo" lo que hace la linea es multiplicar los dos datos anteriores y los divide entre dos. 

def main():
  intBase = 7
  intAltura = 5
  fltAreaTriangulo=(intBase*intAltura)/2
  txt = "Area: {2:0.2f} ( {0} por {1} entre dos )"
  print(txt.format(intBase, intAltura, fltAreaTriangulo))
#Lo que hace esta ultima linea es incrustar con la función format los 2 valores que se tienen y el valor que se calulo, de tal modo que junto a la variable "txt" se muestre la operación que se utilizo para realizar el codigo.

