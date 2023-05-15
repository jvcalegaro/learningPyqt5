import math

##############################  variáveis   ##############################
y = float(input('Insira o comprimento da flecha (em m): '))
p = float(input('Insira a massa específica (em Kg/m): '))
X = float(input('Insira o comprimento do vão (em m): '))
##############################  constantes  ##############################
g = 9.81
##############################  calculáveis ##############################
u = (p*g)/1000
x = X/2
##############################  cálculos    ##############################

# função da questão
def f(t0):
    return ((t0/u)*(math.cosh((u*x)/t0)-1)-y)

# fórmula da bisseção
def bissecao():
    a = 1 
    b = 100 
    e = 0.0001 
    opcao = input('\nPara inserir um intevalo [a,b] e um erro para a bissecao, tecle "1": \nCaso não tenha esses valores, tecle "0": ')
    if(opcao == 1):
        a = int(input('Insira o inicio do intervalo da bisseção (a): '))
        b = int(input('Insira o fim do intervalo da bisseção (b): '))
        e = float(input('Insira valor do erro da bisseção: '))
    if f(a)*f(b) < 0:
        while(math.fabs(b-a)/2 > e):
            xi = (a+b)/2
            if f(xi) == 0:
                return xi
            else:
                if f(a)*f(xi) < 0:
                    b = xi
                else:
                    a = xi
        return xi
    else:
        print('Não há raiz neste intervalo')
        
###########   T   ###########
def tracao_maxima(t0):
    return (t0 + (u * y))

###########   s   ###########
def comprimento_cabo_metade(t0): 
    return (t0/u*(math.sinh((u/t0)*x)))

###########   S   ###########
def comprimento_cabo(t0): 
    return 2*comprimento_cabo_metade(t0)

t0 = bissecao()
print(f'\n\n\nValor do peso unitario(u): {u}')
print(f'Flecha: {y}\nVao: {X}\nGravidade: {g}\nMassa especifica: {p}')

print(f'\n\nForca de tracao inicial(t0): {t0}N')
print(f'Forca de tracao maxima(T): {tracao_maxima(t0)}N')
print(f'Comprimento total do cabo(S): {comprimento_cabo(t0)}m\n\n\n')   

'''
y = comprimento da Flecha           (em m)
X = comprimento do Vão              (em m)
x = metade do comprimento do Vão    (em m)
S = comprimento do cabo             (em m)
s = metade do comprimento do cabo   (em m)
u = peso unitário                   (em KN/m)
p = massa específica em             (em Kg/m)
g = gravidade                       (em m/s²)
T0 = tração inicial                 (em N)
T = tração máxima                   (em N)
'''