N1,N2,N3,N4 = input().split(" ")

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

mediaPeso = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
print("Media: {:.1f}".format(mediaPeso))

if(mediaPeso >= 7.0):
    print("Aluno aprovado.")
elif(mediaPeso < 5.0):
    print("Aluno reprovado.")
elif(mediaPeso >= 5.0 and mediaPeso <= 6.9):
    print("Aluno em exame.")
    N4 = float(input())
    print("Nota do exame:",N4)
    mediaFinal = (N4 + mediaPeso)/2
    if(mediaFinal >= 5.0):
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(mediaFinal))
    elif(mediaFinal <= 4.9):
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(mediaFinal))