t = int(input())

for _ in range(t):
    n, a, q = map(int, input().split())
    notificaciones = input()

    suscriptores_en_linea = a

    for notificacion in notificaciones:
        if notificacion == '+':
            suscriptores_en_linea += 1
        else:
            suscriptores_en_linea = max(0, suscriptores_en_linea - 1)

    if suscriptores_en_linea == n:
        print("SI")
    else:
        if suscriptores_en_linea >= a or suscriptores_en_linea > 0:
            print("QUIZAS")
        else:
            print("NO")

