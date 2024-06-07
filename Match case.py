def gofootball():
    goals=int(input("Enter the number of goals: "))
    match goals:
        case 1:
            print("You scored a goal.")
        case 2:
            print("You scored a brace.")
        case 3:
            print("You scored a hat-trick.")
        case 4:
            print("You scored a poker.")
        case 5:
            print("You scored a haul.")



gofootball()

