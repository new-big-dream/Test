"""Ce module fournit une fonction pour calculer une moyenne de valeurs"""

from rich.console import Console
from rich.markdown import Markdown


def moyenne(valeurs):
    """Retourne la moyenne des valeurs d'une liste non vide."""
    if not valeurs:
        raise ValueError("La liste de valeurs ne peut pas être vide")

    res = 0
    for x in valeurs:
        res += x
    return res / len(valeurs)


if __name__ == "__main__":
    Console().print(Markdown(moyenne.__doc__))
    print("moyenne([10, 20, 15]) :", end=" ")
    print(moyenne([10, 20, 15]))
