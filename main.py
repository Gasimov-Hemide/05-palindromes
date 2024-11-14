"""
Verifie si un mot est un palindrome : 
    -ispalindrome(p)
    -main()
"""

#### Fonction secondaire

def ispalindrome(p):

    """
    Vérifie si un mot est un palindrome
    args : 
        -p : un mot dont on veut voir s'il est un palindrome 
    returns : 
        -True : le mot est bien un palindrome
        -False : le mot n'est pas un palindrome
    """

    a = p.lower().translate(str.maketrans('éèêëàâäîïôöùûüç','eeeeaaaiioouuuc',' -.,?!;:/\''))
    b = a[::-1]

    palindrome = True
    l=len(a)
    for i in range(l):
        if a[i-1] != b[i-1]:
            palindrome = False
            break
    return palindrome

#### Fonction principale

def main():

    """
    Fait des appels de test en utilisant le module ispalindrome
    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
