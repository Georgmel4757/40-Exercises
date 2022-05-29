def main():
    ex1 = ["Rook", "A8", "H8"]
    ex2 = ["Bishop", "A7", "G1"]
    ex3 = ["Queen", "C4", "D6"]

    res_1 = canMove(*ex1)
    res_2 = canMove(*ex2)
    res_3 = canMove(*ex3)

    print(res_1)
    print(res_2)
    print(res_3)


def canMove(chessman, last_pos, new_pos):
    chessmen = ["king", "queen", "rook", "bishop", "knight", "pawn"]

    x_range = range(1, 9)
    y_range = range(1, 9)

    x_pos = {"A": 1, "B": 2, "C": 3,
            "D": 4, "E": 5, "F": 6,
            "G": 7, "H": 8} 

    sign_last = x_pos[last_pos[0]]
    sign_new = x_pos[new_pos[0]]
    num_last = int(last_pos[1])
    num_new = int(new_pos[1])

    chessman = chessman.strip().lower()

    if chessman not in chessmen:
        return None
    if sign_last not in x_range or sign_new not in x_range:
        return False
    if num_last not in y_range or num_new not in y_range:
        return False

    if chessman == "king":
        if (sign_new in range(sign_last-1, sign_new+2) and 
                num_new in range(num_last-1, num_new+2)):
            return True
        return False

    elif chessman == "queen":
        if (sign_new == sign_last or num_new == num_last or
                num_new - num_last == sign_new - sign_last or
                num_new - num_last == -(sign_new - sign_last)):
            return True
        return False
    
    elif chessman == "rook":
        if sign_new == sign_last or num_new == num_last:
            return True
        return False
    
    elif chessman == "bishop":
        if (num_new - num_last == sign_new - sign_last or
                num_new - num_last == -(sign_new - sign_last)):
            return True
        return False
    
    elif chessman == "knight":
        if (abs(num_new - num_last) == 2 and abs(sign_new - sign_last) == 1 or 
                abs(num_new - num_last) == 1 and abs(sign_new - sign_last) == 2):
            return True
        return False

    elif chessman == "pawn":
        if sign_last == sign_new and (abs(num_new - num_last) in [1, 2]):
            return True
        return False
    
    return None
    

if __name__ == "__main__":
    main()
