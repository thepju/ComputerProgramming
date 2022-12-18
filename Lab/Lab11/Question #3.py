class City:
  Country = {}
  nbCity = 0
  nbCountry = 0
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    if country not in City.Country.keys():
      City.Country[country] = []
      City.nbCountry += 1
    City.Country[country].append((city, float(temperature)))
    City.nbCity += 1
import csv
def fu(name):   
    with open(name) as file:
        reader = csv.DictReader(file)
        dic = dict()
        for row in reader : 
            if not row['country'] in dic :
                dic[row['country']] = list()
                dic[row['country']].append(float(row['temperature']))
            else :
                dic[row['country']].append(float(row['temperature']))
        for i in dic :
            print(f"{i} {sum(dic[i]) / len(dic[i]):.2f}")
name = input("Enter file name: ")
fu(name) 