print("euromillions simulator")
import random


print_wins = False

# start with 1 grand
starting_money = 100000

wins_2_0 = 0
wins_2_1 = 0
wins_1_2 = 0
wins_3_0 = 0
wins_3_1 = 0
wins_2_2 = 0
wins_4_0 = 0
wins_3_2 = 0
wins_4_1 = 0
wins_4_2 = 0
wins_5_0 = 0
wins_5_1 = 0
wins_5_2 = 0

bounds_2_0 = [170, 340]
bounds_2_1 = [300, 850]
bounds_1_2 = [430, 860]
bounds_3_0 = [680, 1275]
bounds_3_1 = [850, 4250]
bounds_2_2 = [690, 2150]
bounds_4_0 = [2125, 8500]
bounds_3_2 = [2150, 8600]
bounds_4_1 = [4250, 34000]
bounds_4_2 = [8500, 425000]
bounds_5_0 = [85000, 4250000]
bounds_5_1 = [8500000, 102000000]
bounds_5_2 = [1445000000, 20400000000]

runs = 0

max_money = [0, 0]
total_winnings = 0


def p_win(text):
    if print_wins:
        print(text)

def cscr():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


while True:
    try:

        if max_money[0] < starting_money:
            max_money = [starting_money, runs]

        starting_money -= 250
        runs += 1

        balls = []
        stars = []

        ball_selection = [1,  2,  3,  4,  5,  6,  7,  8,  9,  10,
                          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                          21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                          31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                          41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        star_selection = [1,  2,  3,  4,  5,  6,  7,  8,  9,  10,
                          11, 12]

        while len(balls) < 5:
            ball = random.randint(1, len(ball_selection))
            balls.append(ball_selection.pop(ball-1))
            
        while len(stars) < 2:
            star = random.randint(1, len(star_selection))
            stars.append(star_selection.pop(star-1))

        ball_selection = [1,  2,  3,  4,  5,  6,  7,  8,  9,  10,
                          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                          21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                          31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                          41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        star_selection = [1,  2,  3,  4,  5,  6,  7,  8,  9,  10,
                          11, 12]
        
        draw_balls = []
        draw_stars = []

        while len(draw_balls) < 5:
            ball = random.randint(1, len(ball_selection))
            draw_balls.append(ball_selection.pop(ball-1))

        while len(draw_stars) < 2:
            star = random.randint(1, len(star_selection))
            draw_stars.append(star_selection.pop(star-1))

        balls_matched = 0
        stars_matched = 0

        for ball in balls:
            if ball in draw_balls:
                balls_matched += 1
        
        for star in stars:
            if star in draw_stars:
                stars_matched += 1

        if balls_matched == 2 and stars_matched == 0:
            wins_2_0 += 1
            win = bounds_2_0[1]
            # win = random.randint(bounds_2_0[0], bounds_2_0[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 2_0 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 2 and stars_matched == 1:
            wins_2_1 += 1
            win = bounds_2_1[1]
            # win = random.randint(bounds_2_1[0], bounds_2_1[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 2_1 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 1 and stars_matched == 2:
            wins_1_2 += 1
            win = bounds_1_2[1]
            # win = random.randint(bounds_1_2[0], bounds_1_2[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 1_2 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 3 and stars_matched == 0:
            wins_3_0 += 1
            win = bounds_3_0[1]
            # win = random.randint(bounds_3_0[0], bounds_3_0[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 3_0 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 3 and stars_matched == 1:
            wins_3_1 += 1
            win = bounds_3_1[1]
            # win = random.randint(bounds_3_1[0], bounds_3_1[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 3_1 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 2 and stars_matched == 2:
            wins_2_2 += 1
            win = bounds_2_2[1]
            # win = random.randint(bounds_2_2[0], bounds_2_2[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 2_2 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 4 and stars_matched == 0:
            wins_4_0 += 1
            win = bounds_4_0[1]
            # win = random.randint(bounds_4_0[0], bounds_4_0[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 4_0 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 3 and stars_matched == 2:
            wins_3_2 += 1
            win = bounds_3_2[1]
            # win = random.randint(bounds_3_2[0], bounds_3_2[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 3_2 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 4 and stars_matched == 1:
            wins_4_1 += 1
            win = bounds_4_1[1]
            # win = random.randint(bounds_4_1[0], bounds_4_1[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 4_1 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 4 and stars_matched == 2:
            wins_4_2 += 1
            win = bounds_4_2[1]
            # win = random.randint(bounds_4_2[0], bounds_4_2[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 4_2 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 5 and stars_matched == 0:
            wins_5_0 += 1
            win = bounds_5_0[1]
            # win = random.randint(bounds_5_0[0], bounds_5_0[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 5_0 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 5 and stars_matched == 1:
            wins_5_1 += 1
            win = bounds_5_1[1]
            # win = random.randint(bounds_5_1[0], bounds_5_1[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 5_1 - added "+str(win))
            starting_money += win
            total_winnings += win
        elif balls_matched == 5 and stars_matched == 2:
            wins_5_2 += 1
            win = bounds_5_2[1]
            # win = random.randint(bounds_5_2[0], bounds_5_2[1])
            p_win("draw: "+str(runs)+" - year"+str(runs//104)+" - WIN 5_2 - added "+str(win))
            starting_money += win
            total_winnings += win
        # elif random.randint(1,1000) == 823:
        #     wins_5_2 += 1
        #     win = bounds_5_2[1]
        #     # win = random.randint(bounds_5_2[0], bounds_5_2[1])
        #     print("draw:",runs,"- year",runs//104,"- WIN 5_2 - added", win)
        #     starting_money += win
        #     total_winnings += win
        # else:
            # print("draw:",runs,"- year",runs//104,"- no win")


        if runs % 20800 == 0:
            cscr()

            print("total runs: ", runs)
            print("total years: ", runs // 104)
            print("total money spent: ", runs * 250)
            print("final money: ", starting_money)

            print()

            print("max money: ", max_money[0], " on year ", max_money[1]//104)
            print("total winnings: ", total_winnings)
            print("total paid: ", runs * 250)

            print()

            print("total wins 2_0: ", wins_2_0)
            print("total wins 2_1: ", wins_2_1)
            print("total wins 1_2: ", wins_1_2)
            print("total wins 3_0: ", wins_3_0)
            print("total wins 3_1: ", wins_3_1)
            print("total wins 2_2: ", wins_2_2)
            print("total wins 4_0: ", wins_4_0)
            print("total wins 3_2: ", wins_3_2)
            print("total wins 4_1: ", wins_4_1)
            print("total wins 4_2: ", wins_4_2)
            print("total wins 5_0: ", wins_5_0)
            print("total wins 5_1: ", wins_5_1)
            print("total wins 5_2: ", wins_5_2)


    except:
        break

print("total runs: ", runs)
print("total years: ", runs // 104)
print("total money spent: ", runs * 250)
print("final money: ", starting_money)

print()

print("max money: ", max_money[0], " on year ", max_money[1]//104)
print("total winnings: ", total_winnings)
print("total paid: ", runs * 250)

print()

print("total wins 2_0: ", wins_2_0)
print("total wins 2_1: ", wins_2_1)
print("total wins 1_2: ", wins_1_2)
print("total wins 3_0: ", wins_3_0)
print("total wins 3_1: ", wins_3_1)
print("total wins 2_2: ", wins_2_2)
print("total wins 4_0: ", wins_4_0)
print("total wins 3_2: ", wins_3_2)
print("total wins 4_1: ", wins_4_1)
print("total wins 4_2: ", wins_4_2)
print("total wins 5_0: ", wins_5_0)
print("total wins 5_1: ", wins_5_1)
print("total wins 5_2: ", wins_5_2)

