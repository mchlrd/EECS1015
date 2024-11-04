def draw_grid():
    horizontal_line = '+ - - - - + - - - - + - - - - +'
    vertical_line = "|         |         |         |"

    print(horizontal_line)

    def main_grid():
        for _ in range(5):
            print(vertical_line)
        print(horizontal_line)

    main_grid()
    main_grid()
    main_grid()
draw_grid()