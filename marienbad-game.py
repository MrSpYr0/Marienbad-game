#######################################################
########             module         ###################
#######################################################
import random as rd
import copy as cp
#######################################################
########          operations          #################
#######################################################

""" cette partie du code a pour but de définir les fonctions d'opérations necessaire pour notre programme"""

def somme(l):                           #fais la somme des termes d'une listee
    s = 0
    for i in range(len(l)):
        s += l[i]
    return s

def decomposition(l,z):                 #decompose un chiffre (entre 0 et z) en liste contistuer de 0 et 1
    d = [0]*z
    for loop in range(-1,-l-1,-1):
        d[loop] = 1
    return d

def addition(l1,l2):                    #additionne deux listes termes par termes
    l3 = [0]*len(l2)
    for loop in range (len(l2)):
        l3[loop] = l1[loop] + l2[loop]
    return l3
    
def soustraction(l1,l2):                #soustrait deux listes termes par termes
    l3 = [0]*len(l2)
    for loop in range (len(l2)):
        l3[loop] = l1[loop] - l2[loop]
    return l3    
    
def minimal(l_c):                       #cherche le couple tel que le deuxieme membres du couples 
    mini = l_c[0][1]                    #soit le minimal de la liste de couple
    couple = l_c[0]
    for i in range(len(l_c)):
        if mini >= l_c[i][1]:
            mini = l_c[i] [1]
            couple = l_c[i]
    return couple
                         
def maximal(l_c):                       #cherche le couple tel que le deuxieme membres du couples                 
    maxi = l_c[0][1]                    #soit le maximal de la liste de couple
    couple = l_c[0]
    for i in range(len(l_c)):
        if maxi <= l_c[i][1]:
            maxi = l_c[i] [1]
            couple = l_c[i]
    return couple
######################################################
########           organisation        ################
#######################################################
    
"""cette partie a pour but de creer les fonctions qui vont nous permettre de organiser 
les listes de telle façon a pouvoir faire nos calculs """
    
def reorganisation_bin(l,z):           #rabat le chiffre binaire a droite
    s = l[::-1] + [0]*(z-len(l))
    s2 = s[::-1]
    return s2

def reorganisation (l,z):              #rabat les 1 vers la droite
    s = somme(l)
    b = decomposition(s,z)
    return b
    
#######################################################
########          conversion          #################
#######################################################
    
    """cette partie a pour but de créer les fonctions de conversion en binaire ou en decimal d'une liste et d'une matrice
    cela permet d'utiliser notre méthodes systèmatique"""
    
def bin1(n):                            #converti un nombre en binaire 
    q = -1 
    res = '' 
    while q != 0: 
        q = n // 2 
        r = n % 2 
        res = str(r) + res 
        n = q 
    return res                          #il est renvoyer sous forme de chaine de caractere )

def conversion_dec(l):                  #convertie un nombre binaire(forme liste) en un nombre decimal
    s = 0
    n = len(l)
    for i in range (n):
        s += l[i]*(2**(n-1-i))
    return s

def conversion_ligne(l):                #compte le nombre d'element de la liste 
    s = somme(l)                        #puis converti ce nombre en binaire
    conv = bin1(s)
    ligneconv = list(conv)
    for i in range (len(ligneconv)):
        ligneconv[i] = int(ligneconv[i])
    return ligneconv

    
def conversion_plateau(mat):
    z = len(mat[0])                     #converti tout les plateau en une liste de nombre binaire 
    conv = [[0]*z]*len(mat)  
    for i in range (len(mat)):
        conv[i] = conversion_ligne(mat[i])
        conv[i] = reorganisation_bin(conv[i],z)
    return conv


    
#######################################################
########          sommme plateau           ############
#######################################################
    
    """ cette partie va faire la somme des colones du plateaux ainsi que la Nim-addition définie dans les spéc"""

def somme_plateau(mat):                 # fais la somme totale du plateau (colone par colone)
    n = len(mat)
    z = len(mat[0])
    som = [0]*z
    for i in range (n):
        som = addition(som,mat[i])
    return som


def nim_somme(mat):                     #renvoi la Nim-Somme du plateau
    mat_bin = conversion_plateau(mat)
    som = somme_plateau(mat_bin)
    for loop in range (len(som)):
        if som[loop] % 2 == 0:
            som[loop] = 0
        else:
            som[loop] = 1
    return som
    

#######################################################
########           recherche          #################
#######################################################

"""cette partie va nous permettre de regarder l'état du plateau pendant ce tour"""

def recherche_de_1(l):                     #renvoi la position du 1 qui a l'indice le plus eleve de la liste
    for loop in range (-1,-len(l),-1):
        if l[loop] == 1:
            return len(l) + loop
    return -1
    
def recherche_ligne(mat,nb,k):
    indice = []                            #recherche la ligne la moins grosse (k=1) ou la plus grosse (k!=1)
    for loop in range(len(mat)):           #contenant un certain nombre d'element
        if somme(mat[loop]) >= nb:
            i = somme(mat[loop])
            indice.append([loop,i])
            if k==1:
                solution = minimal(indice)
            else:
                solution = maximal(indice)
    if len(indice)!=0:
        return solution [0]             
    return len(mat)
    
    
def ligne_la_plus_grosse(mat):              #recherche la ligne avec le plus d'element 
    indice = []
    for loop in range(len(mat)):
        i = somme(mat[loop])
        indice.append([loop,i])
    return maximal(indice)[0]


def liste_indice_ligne(mat):                #renvoi la liste des indices des lignes non vide
    indice = []
    for i in range(len(mat)):
        if recherche_de_1(mat[i]) != -1:
            indice.append(i)
    return indice

def compter_ligne_non_vide(mat):            #compte le nombre de ligne non vide du plateau
    s = 0
    for i in range (len(mat)):
        if recherche_de_1(mat[i]) != -1:
            s += 1
    return s

def autre_ligne(plateau,ligne):             #renvoi la liste des lignes non vides mais differentes de la ligne voulu
        liste_indice = liste_indice_ligne(plateau)
        b=[]
        s=0
        compteur=0
        for i in range(len(liste_indice)):
            indice=liste_indice[i]
            compteur+=somme(plateau[indice])
            if indice!=ligne:
                b.append(indice)
                s+=somme(plateau[indice])
        if s==len(b):
            return True
        else:
            return False

#######################################################
########           tours              ################# 
#######################################################

def tour_joueur(plateau):
     n = len(plateau)
     z = len(plateau[0])
     k = 0
     while k == 0:
         print('quelle ligne ?') 
         l1 = int(input())
         if l1 <= n :                #verifie que la ligne existe
             l = l1 - 1
             print('combien de baton ?')
             b = int(input())
             s = somme(plateau[l])
             if b <= s:              #verifie qu'il reste assez de baton
                 k = 1
                 plateau[l] = soustraction(plateau[l],decomposition(b,z))
                 plateau[l] = reorganisation(plateau[l],z)
                 for i in range (n):
                     print(plateau[i])
             else:
                 k = 0
         else:
             k = 0
     return plateau
     
def tour_PC_alea(plateau):
    z = len(plateau[0])
    n = len(plateau)
    k = 0
    while k ==0 :
        l = rd.randint(0,n-1)
        b = rd.randint(1,z)
        s = somme(plateau[l])
        if b <= s :          #verifie qu'il y a assez de baton sur la ligne
            k = 1
            plateau[l] = soustraction(plateau[l],decomposition(b,z))
            plateau[l] = reorganisation(plateau[l],z)
        else :
             k = 0
    return plateau
    
def tour_PC(plateau):
    n = len(plateau)
    z = len(plateau[0])
    Nimber = nim_somme(plateau)
    nbr_a_enlever = conversion_dec(Nimber)
    ligne = recherche_ligne(plateau,nbr_a_enlever,1)
    k=1
    while nbr_a_enlever != 0 or k<=2:
        copy_plateau =cp.deepcopy( plateau)
        ligne = recherche_ligne(plateau,nbr_a_enlever,k)
        Nimber = nim_somme(plateau)
        nbr_a_enlever = conversion_dec(Nimber)
        maxi=ligne_la_plus_grosse(plateau)
        if  ligne == n:
            if compter_ligne_non_vide(plateau)==2:
                if autre_ligne(plateau,maxi) == True:
                    plateau[maxi]=[0]*z
                    return plateau
            maxi=ligne_la_plus_grosse(plateau)
            i = 0
            j = n-1
            copyplateau = somme(plateau[j])
            while nbr_a_enlever != 0 and j > 0:
                if i == z-1 and nbr_a_enlever!= 0:
                    plateau[j] = decomposition(copyplateau,z)
                    j -= 1
                    copyplateau = somme(plateau[j])
                    i = 0            
                plateau[j][i] = 0
                Nimber = nim_somme(plateau)
                nbr_a_enlever= conversion_dec(Nimber)
                i += 1
            return plateau
        else:
            if compter_ligne_non_vide(plateau)==1  and  autre_ligne(plateau,ligne) == True: #cas ou il ne reste qu'une ligne 
                if somme(plateau[ligne])!=1:                                                #avec un nombre d'element different de 1
                    a = decomposition(nbr_a_enlever-1,z)
                    plateau[ligne] = soustraction(plateau[ligne],a)
                    plateau[ligne] = reorganisation(plateau[ligne],z)
                    return plateau
                else:
                    a = decomposition(nbr_a_enlever,z)
                    plateau[ligne] = soustraction(plateau[ligne],a)
                    plateau[ligne] = reorganisation(plateau[ligne],z)
                    return plateau
            if compter_ligne_non_vide(plateau)==2 and autre_ligne(plateau,ligne) == True: #cas ou il reste 2 lignes et l'autre a 1 element
                plateau[maxi]=[0]*z
                return plateau
            elif compter_ligne_non_vide(plateau)%2!=0  and autre_ligne(plateau,ligne) == True : #cas ou il reste un nombre impaire de lignes
                if somme(plateau[ligne])!=1:                                                    #et il ne reste que 1 seul element sur les autres lignes
                    a = decomposition(nbr_a_enlever-1,z)
                    plateau[ligne] = soustraction(plateau[ligne],a)
                    plateau[ligne] = reorganisation(plateau[ligne],z)
                    return plateau
                else:
                    a = decomposition(nbr_a_enlever,z)
                    plateau[ligne] = soustraction(plateau[ligne],a)
                    plateau[ligne] = reorganisation(plateau[ligne],z)
                    return plateau
            elif compter_ligne_non_vide(plateau)%2==0 and autre_ligne(plateau,ligne) == True: #cas ou il reste un nombre paire de lignes
                if somme(plateau[ligne])!=1:                                                    #et il ne reste que 1 seul element sur les autres lignes
                    a = decomposition(nbr_a_enlever+1,z)
                    plateau[ligne] = soustraction(plateau[ligne],a)
                    plateau[ligne] = reorganisation(plateau[ligne],z)
                    return plateau
                else:
                    a = decomposition(nbr_a_enlever,z)
                    plateau[ligne] = soustraction(plateau[ligne],a)
                    plateau[ligne] = reorganisation(plateau[ligne],z)
                    return plateau
            elif compter_ligne_non_vide(plateau) != 1  and autre_ligne(plateau,ligne) == False:      
                a = decomposition(nbr_a_enlever,z)
                plateau[ligne] = soustraction(plateau[ligne],a)
                plateau[ligne] = reorganisation(plateau[ligne],z) 

            else:
                a = decomposition(nbr_a_enlever,z)
                plateau[ligne] = soustraction(plateau[ligne],a)
                plateau[ligne] = reorganisation(plateau[ligne],z)
        Nimber = nim_somme(plateau)
        nbr_a_enlever = conversion_dec(Nimber)
        k+=1
        if nbr_a_enlever !=  0:
            plateau=cp.deepcopy(copy_plateau)
    return plateau


def tours(plateau,k,f):
    n=len(plateau)
    Fours=0
    while compter_ligne_non_vide(plateau) != 0:
        if k % 2 != 0:
            plateau = tour_joueur(plateau)
            k += 1
        else:
            print('PC joue ...')
            if f==1:
                plateau = tour_PC_alea(plateau)
                for i in range (n):
                    print(plateau[i])
                k+=1
            elif f==2:
                Nimber = nim_somme(plateau)
                som = conversion_dec(Nimber)
                if som == 0:                            #impossibilite d'utiliser la methode systematique
                    plateau = tour_PC_alea(plateau)
                else:
                    if Fours % 2 != 0:
                        plateau = tour_PC(plateau)
                    else :
                        plateau = tour_PC_alea(plateau)	
                for i in range (n):
                    print(plateau[i])
                Fours+=1
                k+=1
            else :
                Nimber = nim_somme(plateau)
                som = conversion_dec(Nimber)
                if som == 0:                            #impossibilite d'utiliser la methode systematique
                    plateau = tour_PC_alea(plateau)
                else:
                    plateau = tour_PC(plateau)
                for i in range (n):
                    print(plateau[i])
                k += 1
    if k % 2 != 0:
        resultat='vous avez gagne bravo !!  '
    else:
        resultat='le PC a gagne, dommage !'
    return resultat

def creation_plat(l):
    nbrmax = 2*(l-1)+1
    u = 1
    plateau = [[0]*nbrmax]*l
    for i in range (l):
        plateau[i] = decomposition(u,nbrmax)
        u = u + 2
    return plateau
    
   
def partie():
    while True:
        print('quel niveaau de difficulte souhaitez-vous ?\n')
        print('1 - Facile \n')
        print('2- moyen\n')
        print('3- complique\n')
        f=int(input())
        print('avec combien de lignes voulez-vous jouer ?')
        n = int(input())
        plateau = creation_plat(n)
        print('qui commence ? ')
        print('1-Joueur commence ')
        print('2- PC commence ')
        h = int(input())
        for i in range (n):
            print(plateau[i])
        if h == 1:
            resultat = tours(plateau,1,f)
        elif h == 2:
            resultat = tours(plateau,0,f)
        else:
            return ('ERREUR')
        print(resultat)
        print('voulez-vous refaire une partie ?')
        print('si oui tapez 1, sinon tapez 2')
        k = int(input())
        if k == 2:
            return 'au revoir'


#######################################################
########          variable           ##################
#######################################################
print(partie())