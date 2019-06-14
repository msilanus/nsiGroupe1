def harmonique_croissant(n : int):
    """Retourne la somme des inverses entre 1 et n"""
    H = 0
    if n!=0:
        for i in range(1,n+1):
            H += 1.0/i
        return H

def harmonique_decroissant(n : int):
    """Retourne la somme des inverses entre 1 et n"""
    H = 0
    if n!=0:
        for i in range(n,0,-1):
            H += 1.0/i
        return H

print((f'n=1000000 : H = {harmonique_croissant(1000000)}'))

print((f'n=1000000 : H = {harmonique_decroissant(1000000)}'))