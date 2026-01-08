medida = float(input("Digite uma medida em metros: "))
print( "A medida de ", medida, "metros corresponde a:" )

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 100010

print( km, "quilômetros" )
print( hm, "hectômetros" )
print( dam, "decâmetros" )
print( dm, "decímetros" )
print( cm, "centímetros" )
print( mm, "milímetros" )


