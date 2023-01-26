print('***********************')
print('长尸🝗⼕ти长и 廾ㄖ人и长и')
print('***********************')

# battl_field = [[' ' for row in range(3)] for col in range(3)]
battl_field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def new_game(battl_field):
    print('—' * 15)
    for row in battl_field:
        for col in row:
            print('|', col, '|', end='')
        print()
        print('—' * 15)


def validation(next_step):
    valid = False
    for row, x in enumerate(battl_field):
        for col, y in enumerate(x):
            if step == y:
                battl_field[row][col] = next_step
                valid = True
                return next_step

def input_num(next_step):
    global step
    flag = False
    count_iq = 0
    while not flag:
        step = input(f'Ходят {next_step}  введите цифру от 1 до 9:  ')
        if count_iq > 2:
            print('Ты что тупой??? 🧐')
            count_iq = 0
        if not step.isdigit():
            print('Ошибка! Это не цифра. Введите цифру от 1 до 9')
            count_iq += 1
            continue
        else:
            step = int(step)
        if step < 1 or step > 9:
            print('Ошибка! Введите цифру от 1 до 9')
            count_iq += 1
            continue
        if validation(next_step):
            flag = True
            return next_step
        else:
            print('░З░А░Н░Я░Т░О░!░')
            count_iq +=1
            continue
        break


def check_win(battl_field):
    f = battl_field
    for row in range(3):
        # горизонталь
        if f[row][0] == f[row][1] == f[row][2]:
            return f[row][0]
            break
        # вертикаль
        elif f[0][row] == f[1][row] == f[2][row]:
            return f[0][row]
            break
        # диагональ
        elif f[0][0] == f[1][1] == f[2][2]:
            return f[0][0]
            break
        elif f[0][2] == f[1][1] == f[2][0]:
            return f[1][1]
            break
    return False

def select_step_xo(battl_field):
    count = 0
    global new_battl_field
    while True:
        new_game(battl_field)
        if count % 2 == 0:
            input_num('✖')
        else:
            input_num('ⵔ')
        count += 1
        if count == 9:
            print('Ничья.')
            break
        if check_win(battl_field):
            print(f"Победили:  {check_win(battl_field)}  🏆")
            break
    new_game(battl_field)


select_step_xo(battl_field)

