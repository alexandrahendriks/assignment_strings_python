# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Players who scored
score_one = 'Ruud Gullit'
score_two = "Marco van Basten"

# Times of the scores
goal_0 = 32
goal_1 = 54

scorers = f"{score_one} {goal_0}, {score_two} {goal_1}"
#print(scorers)

report = f"{score_one} scored in the {goal_0}nd minute\n{score_two} scored in the {goal_1}th minute"
#print(report)

# Choosen player's first and last name
player = "Ronald Koeman"
space = player.find(' ')
first_name = player[:space]

last = player[space + 1:]
print(last)
last_name_len = len(last)
#print(last_name_len)

name_short = f"{player[0]}. {last}"
#print(name_short)

# Chant
chant = ((first_name + "! ") * len(first_name)).rstrip()
#print(chant)

good_chant = chant[-1] != " "
#print(good_chant)


