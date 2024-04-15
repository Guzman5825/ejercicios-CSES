dna=input()
repMasAlta=0
repLetraActual=0
letraAnterior=dna[0]

for letra in dna:    
    if letraAnterior==letra:
        repLetraActual+=1
    else:
        if repLetraActual>repMasAlta:
            repMasAlta=repLetraActual
        letraAnterior=letra
        repLetraActual=1

if repLetraActual>repMasAlta:
    repMasAlta=repLetraActual

print(repMasAlta)

        
        

