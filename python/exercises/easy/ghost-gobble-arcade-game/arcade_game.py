"""Funciones para implementar las reglas del clásico juego de arcade Pac-Man."""


def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    
    if power_pellet_active == True and touching_ghost == True:
        return True
    else:
        return False
    


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    
    if touching_power_pellet == True or touching_dot == True:
        return True
    else:
        return False
    
def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
   
    if power_pellet_active == True and touching_ghost == True:
        return False
    elif power_pellet_active == False and touching_ghost == True:
        return True
    else:
        return False


def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:

    if lose(power_pellet_active, touching_ghost) == False and has_eaten_all_dots == True:
        return True
    else:
        return False

def is_invincible(power_pellet_active, has_eaten_all_dots):
    if power_pellet_active == True or has_eaten_all_dots == True:
        return True
    else:
        return False