"""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""

def analyze_input_data(sequence):
    for el in sequence:
        if el != "P1" and el != "P2":
            return False
    return True

def get_next_score(current_score):
    if current_score == "Love":
        return "15"
    elif current_score == "15":
        return "30"
    elif current_score == "30":
        return "40"
    elif current_score == "40":
        return "Advantage"
    else:
        return "Win"

def update_scores(p1_score, p2_score):
    if p2_score != "Advantage": 
        p1_score = get_next_score(p1_score)
    else:
        p2_score = "40"

    return p1_score, p2_score

def print_game_status(p1_score, p2_score):
    if p1_score == "Advantage":
        print("Advantage P1")
    elif p2_score == "Advantage":
        print("Advantage P2")
    elif p1_score == "40" and p2_score == "40":
        print("Deuce")
    elif p1_score == "Win":
        print("Winner is P1")
        return True
    elif p2_score == "Win":
        print("Winner is P2")
        return True
    else:
        print(f"{p1_score} - {p2_score}")
    
    return False

def main():
    match = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

    if analyze_input_data(match):
        p1_score = "Love"
        p2_score = "Love"
        for score in match:
            if score == "P1":
                p1_score, p2_score = update_scores(p1_score, p2_score)
            else:
                p2_score, p1_score = update_scores(p2_score, p1_score)
                
            if print_game_status(p1_score, p2_score):
                break
    
    else:
        print("ERROR: Input sequence has got an invalid element! It must only contain 'P1' or 'P2'")


if __name__ == '__main__':
    main()