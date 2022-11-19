l = [23, 12, 4, 56, 35, 57, 3, 11, 6]

def occurence(l: list, d: int, f: int, r: int) -> int:
    """l est votre liste, d défini le début (a logiquement mettre a 0) \nf défini la fin de la liste (a logiquement mettre a taille de la liste -1) \nr est ce que vous chercher chiffre/nombre"""
    if d == f: return d if l[d] == r else -1
    else:
        m = (d+f)//2
        x = occ(l,d,m,r)
        y = occ(l,m+1,f,r)
        if x != -1 and y != -1: return min(x,y)
        elif x != -1 or y != -1: return max(x,y)
        else: return -1
