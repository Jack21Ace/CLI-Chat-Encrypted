# Creación de la variable que nos da los 28 caracteres de la A a la Z incluyendo un espacio " " y un "."
st:list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','.']
# Creación del reflector estatico
rf = ['A', 'X', 'B', 'C', 'D', 'E', 'F', 'G', 'D', 'I', 'J', 'K', 'G', 'M', 'K', 'M', 'I', 'E', 'B', 'X', 'F', 'T', 'C', 'V', 'V', 'J', 'A', 'T']
# Reflector derecho
r_der = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', ' ', 'N', '.', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
# Reflector medio
r_med = ['.', 'A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', ' ', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
# Reflector Izquierdo
r_izq = ['E', 'K', 'M', 'F', 'L', 'G', ' ', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', '.', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']


rotor_izq = []
rotor_med = []
rotor_der = []

for i in zip(st, r_izq):
    rotor_izq.append([i[0], i[1]])
    
for i in zip(st, r_med):
    rotor_med.append([i[0], i[1]])
    
for i in zip(st, r_der):
    rotor_der.append([i[0], i[1]])

def avanzar_rotor(rotor, paso):
    cuenta = 0
    while cuenta < paso:
        rotor.append(rotor.pop(0))
        cuenta += 1
    return rotor

def conf_rotores(clave_inicial):
    while clave_inicial.upper()[0] != rotor_izq[0][0]:
        rotor_izq.append(rotor_izq.pop(0))

    while clave_inicial.upper()[1] != rotor_med[0][0]:
        rotor_med.append(rotor_med.pop(0))

    while clave_inicial.upper()[2] != rotor_der[0][0]:
        rotor_der.append(rotor_der.pop(0))

def senal_ida(rotor, indice, verbose=False):
    letra_entrada = rotor[indice][1]
    indice_salida = 0
    for pares in rotor:
        if pares[0] != letra_entrada:
            indice_salida += 1
        else:
            break
    return letra_entrada, indice_salida

def senal_vuelta(rotor, indice, verbose=False):
    letra_entrada = rotor[indice][0]
    indice_salida = 0
    for pares in rotor:
        if pares[1] != letra_entrada:
            indice_salida += 1
        else:
            break
    return letra_entrada, indice_salida

def indice_reflector(disco, indice, verbose=False):
    letra_entrada = disco[indice]
    if indice == (len(disco) - 1):
        for i in range(len(disco)):
            if disco[i] == letra_entrada:
                return letra_entrada, i
    else:
        for j in range(indice + 1, len(disco)):
            if disco[j] == letra_entrada:
                return letra_entrada, j
            else:
                for k in range(indice):
                    if disco[k] == letra_entrada:
                        return letra_entrada, k

def enigma(mensaje, clave):

    conf_rotores(clave)

    mensaje_final = []
    for i in mensaje.upper():
        avanzar_rotor(rotor_der, 1)
        if rotor_der[-1][0] == 'V':
            avanzar_rotor(rotor_med, 1)
            if rotor_med[-1][0] == 'Q':
                avanzar_rotor(rotor_izq, 1)

        indice_entrada = st.index(i)

        primer_paso = senal_ida(rotor_der, indice_entrada)
        segundo_paso = senal_ida(rotor_med, primer_paso[1])
        tercer_paso = senal_ida(rotor_izq, segundo_paso[1])
        rebote = indice_reflector(rf, tercer_paso[1])
        cuarto_paso = senal_vuelta(rotor_izq, rebote[1])
        quinto_paso = senal_vuelta(rotor_med, cuarto_paso[1])
        sexto_paso = senal_vuelta(rotor_der, quinto_paso[1])
        mensaje_final.append(st[sexto_paso[1]])

    mensaje_str = ''.join(mensaje_final)
    return mensaje_str

obj = enigma("ZMRKCSYTTWMJB", "DJH")
print(obj)
