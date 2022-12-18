mc = input("What's the result of Manchester city's match? ")
lv = input("What's the result of Liverpool's match? ")
if mc == 'won' and lv == 'won' :
  mc_Goals = int(input("What is the margin that Manchester city won by? "))
  lv_Goals = int(input("What is the margin that Liverpool won by? "))
  if mc_Goals > lv_Goals :
    print("Manchester city is the champion of Premier League.")
  elif lv_Goals > mc_Goals : 
    print("Liverpool is the champion of Premier League.")
  else : 
    po = input("Which team won the play-off match?(Manchester city/Liverpool) ")
    if po == 'Manchester city' : 
      print("Manchester city is the champion of Premier League.")
    else : 
      print("Liverpool is the champion of Premier League.")
elif mc == 'won' and lv == 'lost' : 
  print("Manchester city is the champion of Premier League.")
else :
  print("Liverpool is the champion of Premier League.")


