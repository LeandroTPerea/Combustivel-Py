a=int(input("Digite valor de a:"))
b=int(input("Digite valor de b:"))
c=int(input("Digite valor de c:"))

if (a > 0):
    if (b > 0):
        print ("Tudo ok para decolagem!")
    else:
        print ("Tanque principal vazio; voando com combustível reserva!")
else:
    if (c > 0):
        print ("Foguete não tem piloto, mas há outros foguetes disponíveis!")
