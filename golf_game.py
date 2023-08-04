import random

#Clubs setup
driver_distances = list(range(230, 280, 5))
low_distances = list(range(185, 215, 5))
mid_distances = list(range(130, 185, 5))
high_distances = list(range(90, 135, 5))
gap_wedge_distances = list(range(50, 85, 5))
lob_wedge_distances = list(range(10, 50, 5))
putt_outcomes = [1,2,3]


#Define functions for hitting clubs
def hit_driver():
    club_distance = random.choice(driver_distances)
    return club_distance

def hit_low_iron():
    club_distance = random.choice(low_distances)
    return club_distance

def hit_mid_iron():
    club_distance = random.choice(mid_distances)
    return club_distance

def hit_high_iron():
    club_distance = random.choice(high_distances)
    return club_distance

def hit_gap_wedge():
    club_distance = random.choice(gap_wedge_distances)
    return club_distance

def hit_lob_wedge():
    club_distance = random.choice(lob_wedge_distances)
    return club_distance

def finish_hole():
    finish = random.choice(putt_outcomes)
    return finish


#Hole/Course Setup
full_hole_range = list(range(130,520,5))
par3_range = list(range(130,255,5))
par4_range = list(range(255,445,5))
par5_range = list(range(445,520,5))
par3_4_range = par3_range + par4_range
par3_5_range = par3_range + par5_range
par4_5_range = par4_range + par5_range

par3_count = 0
par4_count = 0
par5_count = 0


#Scorecard setup
total_strokes = 0
total_to_par = 0


#Intro prompt
print()
print("Welcome to Dan's Golf Course! Are you ready to play?")
print()

initial_answer = input("yes/no: ")

if initial_answer == "no":
    print()
    print("Come back when you are ready to play.")
    print()
    exit()
else:
    print()
    print("Great lets go!")
    print()
    print()


club_message = "Here are your club choices: Driver, Low Iron, Mid Iron, High Iron, Gap Wedge, Lob Wedge"

print(club_message)
print()
print()
print()


#Main game

#Setting up loop for each hole 1-9
for x in range(1, 10):
    
    #Set up hole count restrictions on par
    if par3_count < 2 and par4_count < 5 and par5_count < 2:
        hole_length = random.choice(full_hole_range)
    if par3_count >= 2 and par4_count < 5 and par5_count < 2:
        hole_length = random.choice(par4_5_range)
    if par3_count >= 2 and par4_count < 5 and par5_count >= 2:
        hole_length = random.choice(par4_range)
    if par3_count < 2 and par4_count < 5 and par5_count >= 2:
        hole_length = random.choice(par3_4_range)
    if par3_count < 2 and par4_count >= 5 and par5_count >= 2:
        hole_length = random.choice(par3_range)
    if par3_count >= 2 and par4_count >= 5 and par5_count < 2:
        hole_length = random.choice(par5_range)
    if par3_count < 2 and par4_count >= 5 and par5_count < 2:
        hole_length = random.choice(par3_5_range)    

        

    #Set up par for the hole
    if hole_length <= 250:
        par = 3
        par3_count += 1
    elif hole_length > 250 and hole_length <= 440:
        par = 4
        par4_count += 1
    elif hole_length > 440:
        par = 5
        par5_count += 1

    #Set initial parameters before starting a hole
    distance_remaining = hole_length
    hole_shots = 0  
    
    

    #Show player the hole information
    print("Hole #" + str(x) + " is a " + str(hole_length) + "-yard Par " + str(par) + "." )
    print()


    #Start loop to be able to choose clubs while at least 20 yards away
    while distance_remaining >= 20:
        club = input("What club would you like to use? ")
        if club == "Driver" or club == "driver":
            shot_distance = hit_driver()
            print()
            print("You hit your Driver " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif club == "Low Iron" or club == "low iron" or club == "Low iron" or club == "low Iron" or club == "low" or club == "Low":
            shot_distance = hit_low_iron()
            print()
            print("You hit your Low Iron " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif club == "Mid Iron" or club == "mid iron" or club == "Mid iron" or club == "mid Iron" or club == "mid" or club == "Mid":
            shot_distance = hit_mid_iron()
            print()
            print("You hit your Mid Iron " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif club == "High Iron" or club == "high iron" or club == "High iron" or club == "high Iron" or club == "high" or club == "High":
            shot_distance = hit_high_iron()
            print()
            print("You hit your High Iron " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif club == "Gap Wedge" or club == "gap wedge" or club == "Gap wedge" or club == "gap Wedge" or club == "gap" or club == "Gap":
            shot_distance = hit_gap_wedge()
            print()
            print("You hit your Gap Wedge " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif club == "Lob Wedge" or club == "lob wedge" or club == "Lob wedge" or club == "lob Wedge" or club == "lob" or club == "Lob":
            shot_distance = hit_lob_wedge()
            print()
            print("You hit your Lob Wedge " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
    

    #Finish the hole by putting
    if distance_remaining < 20:
        if distance_remaining == 0:
            putts = 0
        else:
            putts = finish_hole()
        hole_strokes = hole_shots + putts     
        hole_to_par = hole_strokes - par
        total_strokes += hole_strokes
        total_to_par += hole_to_par

        #Show player hole/round scoring info
        if putts == 0:
            print("You're in the hole! You're in for " + str(hole_strokes) + " strokes.")
        else:
            print("You're on the green! After " + str(putts) + " putt(s), you're in for " + str(hole_strokes) + " strokes.")
        if hole_to_par > 0:
            print("Your score for the hole is +" + str(hole_to_par) + " to par.")
        elif hole_to_par == 0:
            print("Your score for the hole is even to par.")
        else:    
            print("Your score for the hole is " + str(hole_to_par) + " to par.")
        print()
        print("You've hit a total of " + str(total_strokes) + " strokes so far.") 
        if total_to_par > 0:
            print("Your score for the round is +" + str(total_to_par) + " to par.")
        elif total_to_par == 0:
            print("Your score for the round is even to par.")    
        else:    
            print("Your score for the round is " + str(total_to_par) + " to par.")       
        print()
        print()
        print()  


#Final score messages & exit prompt      
print("Congratulations on finishing your 9-hole round!")
print("Your stroke total is " + str(total_strokes) + ".")
if total_to_par > 0:
    print("Your score for the day is +" + str(total_to_par) + " to par.")
elif total_to_par == 0:
    print("Your score for the day is even to par.")    
else:
    print("Your score for the day is " + str(total_to_par) + " to par.")
print()
print()
print("THANKS FOR PLAYING! PLEASE SEND ME ANY FEEDBACK.")
print()
print()

leave = input("type 'exit' to exit ")
if leave == "exit":
    exit()