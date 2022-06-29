class Figure:
    dic_letter = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    dic_letrev = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    list_num = [1, 2, 3, 4, 5, 6, 7, 8]
    list_turn = []
    current_field = None
    error = None
    figur_name = None


class King:
    @staticmethod
    def turn(current_fild):
        first = current_fild[0]
        sec = int(current_fild[1:])
        list1 = []
        if sec in Figure.list_num and first in Figure.dic_letter:
            for i in range(Figure.dic_letter[first] - 1, Figure.dic_letter[first] + 2):
                if i in Figure.dic_letter.values():
                    for j in range(sec - 1, sec + 2):
                        if j in Figure.list_num:
                            ans = Figure.dic_letrev[i] + str(j)
                            if ans == current_fild.upper():
                                continue
                            else:
                                list1.append(ans)
                                continue
        else:
            Figure.error = "Field does not exist."

        Figure.list_turn = list1
        Figure.current_field = current_fild.upper()
        Figure.figur_name = 'king'


class Queen:
    @staticmethod
    def turn(current_fild):
        first = current_fild[0]
        sec = int(current_fild[1:])
        list1 = []
        if sec in Figure.list_num and first in Figure.dic_letter:
            for i in range(1, 9):
                for j in range(1, 9):
                    if abs(Figure.dic_letter[first] - i) == abs(sec - j) or i == Figure.dic_letter[first] or j == sec:
                        ans = Figure.dic_letrev[i] + str(j)
                        if ans == current_fild.upper():
                            continue
                        else:
                            list1.append(ans)
                            continue
        else:
            Figure.error = "Field does not exist."

        Figure.list_turn = list1
        Figure.current_field = current_fild.upper()
        Figure.figur_name = 'queen'


class Rook:
    @staticmethod
    def turn(current_fild):
        first = current_fild[0]
        sec = int(current_fild[1:])
        list1 = []
        if sec in Figure.list_num and first in Figure.dic_letter:
            for i in range(1, 9):
                for j in range(1, 9):
                    if i == Figure.dic_letter[first] or j == sec:
                        ans = Figure.dic_letrev[i] + str(j)
                        if ans == current_fild.upper():
                            continue
                        else:
                            list1.append(ans)
                            continue
        else:
            Figure.error = "Field does not exist."
        Figure.list_turn = list1
        Figure.current_field = current_fild.upper()
        Figure.figur_name = 'rook'


class Bishops:
    @staticmethod
    def turn(current_fild):
        first = current_fild[0]
        sec = int(current_fild[1:])
        list1 = []
        if sec in Figure.list_num and first in Figure.dic_letter:
            for i in range(1, 9):
                for j in range(1, 9):
                    if abs(Figure.dic_letter[first] - i) == abs(sec - j):
                        ans = Figure.dic_letrev[i] + str(j)
                        if ans == current_fild.upper():
                            continue
                        else:
                            list1.append(ans)
                            continue
        else:
            Figure.error = "Field does not exist."
        Figure.list_turn = list1
        Figure.current_field = current_fild.upper()
        Figure.figur_name = 'bishops'


class Knights:
    @staticmethod
    def turn(current_fild):
        first = current_fild[0]
        sec = int(current_fild[1:])
        num_f = Figure.dic_letter[first]
        list1 = []
        if sec in Figure.list_num and first in Figure.dic_letter:
            for i in range(1, 9):
                for j in range(1, 9):
                    if (i == num_f + 1 or i == num_f - 1) and (j == sec - 2 or j == sec + 2):
                        ans = Figure.dic_letrev[i] + str(j)
                    elif (j == sec + 1 or j == sec - 1) and (i == num_f - 2 or i == num_f + 2):
                        ans = Figure.dic_letrev[i] + str(j)
                    else:
                        continue
                    if ans == current_fild.upper():
                        continue
                    else:
                        list1.append(ans)
                        continue
        else:
            Figure.error = "Field does not exist."
        Figure.list_turn = list1
        Figure.current_field = current_fild.upper()
        Figure.figur_name = 'knights'


class Pawns:
    @staticmethod
    def turn(current_fild):
        first = current_fild[0]
        sec = int(current_fild[1:])
        list1 = []
        if sec in Figure.list_num and first in Figure.dic_letter:
            if sec < 8:
                list1.append(first.upper() + str(sec + 1))
        else:
            Figure.error = "Field does not exist."
        Figure.list_turn = list1
        Figure.current_field = current_fild.upper()
        Figure.figur_name = 'pawns'
