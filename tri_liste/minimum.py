l = [10, 20, 34, 1, 2, 5, 7, 56, 80]

def mini(l: list, d: int, f: int) -> int:
    """l est votre liste, d défini le début (a logiquement mettre a 0) \nf défini la fin de la liste (a logiquement mettre a taille de la liste -1)"""
    if d == f: return [l[d]]
    else:
        m = (d+f)//2
        x = mini(l,d,m)
        y = mini(l,m+1,f)
        return x if x < y else y

def maxi(l: list, d: int, f: int) -> int:
    """l est votre liste, d défini le début (a logiquement mettre a 0) \nf défini la fin de la liste (a logiquement mettre a taille de la liste -1)"""
    if d == f: return [l[d]]
    else:
        m = (d+f)//2
        x = mini(l,d,m)
        y = mini(l,m+1,f)
        return x if x > y else y
