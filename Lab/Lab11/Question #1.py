class Country:
  nbCountry = 0
  def __init__(self, country, population, EU,coastline):
    self.country = country
    self.population = float(population)
    self.EU = EU
    self.coastline = coastline
    Country.nbCountry += 1
import csv
def fu(name):   
    with open(name) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader : 
            if row[2] == 'no' and  row[3] == 'yes': print(f"{row[0]} {row[1]}")
name = input("Enter File name: ")
fu(name) 