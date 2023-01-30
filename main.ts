input.onLogoEvent(TouchButtonEvent.Touched, function () {
    checking(3)
})
input.onButtonPressed(Button.A, function () {
    checking(1)
})
function checking (num: number) {
    if (state == 2) {
        show(num)
        if (memory_list[current] == num) {
            score += 1
            if (current < total - 1) {
                current += 1
            } else {
                state = 1
                current = 0
                if (total < 15) {
                    total += 1
                }
            }
        } else {
            basic.clearScreen()
            basic.showIcon(IconNames.No)
            basic.showString("LOSE")
            basic.showString("SCORE")
            basic.showNumber(score)
            state = 0
        }
    }
}
input.onButtonPressed(Button.AB, function () {
    if (state == 0) {
        state = 1
        total = 3
        current = 0
    }
})
input.onButtonPressed(Button.B, function () {
    checking(2)
})
function show (num2: number) {
    if (num2 == 1) {
        basic.showString("A")
    } else if (num2 == 2) {
        basic.showString("B")
    } else if (num2 == 3) {
        basic.showIcon(IconNames.Happy)
    }
    basic.pause(500)
    basic.clearScreen()
    basic.pause(200)
}
let total = 0
let score = 0
let current = 0
let memory_list: number[] = []
let state = 0
state = 0
memory_list = [
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
]
basic.forever(function () {
    let index: number;
if (state == 0) {
        basic.showLeds(`
            # # . # #
            # # # # #
            # . # . #
            # . . . #
            # . . . #
            `)
        score = 0
    } else if (state == 1) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.showIcon(IconNames.Yes)
        basic.pause(500)
        index = 0
        while (index <= total - 1) {
            memory_list[index] = randint(1, 3)
            show(memory_list[index])
            index += 1
        }
        state = 2
    } else {
    	
    }
})
