def busca_pais(paises, pais):
    """
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    """
    
    try:
        return paises[pais]
    except KeyError:
        return None

paises = {'Argentina':3}
print(busca_pais(paises,'Argentina'))
print(busca_pais(paises,'Colombia'))