letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}

# print(letter_to_points)

letter_to_points.update({" " : 0})

def score_word(word) :
  point_total = 0
  for letter in word :
    if letter not in letter_to_points :
      point_total += 0
    else :
      letter_value = letter_to_points[letter]
      point_total += letter_value
  return point_total

brownie_points = score_word("BROWNIE")

print(brownie_points)

player_to_words = {"player1" : ["BLUE", "TENNIS", "EXIT"], "wordNerd" : ["EARTH", "EYES", "MACHINE"], "LexiCon" : ["ERASER", "BELLY", "HUSKY"], "ProfReader" : ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

def update_point_totals() :
  for player, words in player_to_words.items() :
    player_points = 0
    for word in words :
      player_points += score_word(word)
    player_to_points.update({player : player_points})
  print(player_to_points)
  
update_point_totals()



def play_word(player, word) :
  if player not in player_to_words :
    return "This player is not in this game"
  else :
    player_to_words[player].append(word.upper())
    update_point_totals()


play_word("player1", "zeus")
# print(player_to_words)

def check_winner() :
  winner = ""
  max_point = player_to_points["player1"]
  for points in player_to_points.values() :
    if points > max_point :
      max_point = points
  for player, points in player_to_points.items() :
    if max_point == points :
      winner = player

  print("The winner is {winner}".format(winner = winner))

check_winner()

play_word("wordNerd", "BANKAI")
check_winner()
