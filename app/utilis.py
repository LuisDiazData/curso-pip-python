import read

data = read.read_csv('data.csv')

def get_population(data):
  dict_density = {item["Country/Territory"] :   
  float(item["World Population Percentage"]) for item in data
  }
  return dict_density
def population_by_country(data,country ):
  result = list(filter(lambda item: item["Country/Territory"]==country,data))
  return result

def population_by_continent(data, continent):
  result = list(filter(lambda item: item["Continent"]==continent,data))
  return result