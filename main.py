def on_logo_touched():
    checking(3)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_button_pressed_a():
    checking(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def checking(num: number):
    global score, current, state, total
    if state == 2:
        show(num)
        if memory_list[current] == num:
            score += 1
            if current < total - 1:
                current += 1
            else:
                state = 1
                current = 0
                if total < 15:
                    total += 1
        else:
            basic.clear_screen()
            basic.show_string("LOSE")
            basic.show_string("SCORE")
            basic.show_number(score)
            state = 0

def on_button_pressed_ab():
    global state, total, current
    if state == 0:
        state = 1
        total = 3
        current = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    checking(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def show(num2: number):
    if num2 == 1:
        basic.show_string("A")
    elif num2 == 2:
        basic.show_string("B")
    elif num2 == 3:
        basic.show_icon(IconNames.HAPPY)
    basic.pause(500)
    basic.clear_screen()
    basic.pause(200)
total = 0
score = 0
current = 0
memory_list: List[number] = []
state = 0
state = 0
memory_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def on_forever():
    global score, state
    if state == 0:
        basic.show_leds("""
            # # . # #
                        # # # # #
                        # . # . #
                        # . . . #
                        # . . . #
        """)
        score = 0
    elif state == 1:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
        basic.pause(500)
        index = 0
        while index <= total - 1:
            memory_list[index] = randint(1, 3)
            show(memory_list[index])
            index += 1
        state = 2
    else:
        pass
basic.forever(on_forever)
