import utilis
import charts
data = utilis.data
print("Welcome, please select your country for generate the Graphics")
tipo_graficto = int(input("1 Para graficar la poblacion por pais ò 2 Para una grafica de pie por continente\n"))
if tipo_graficto == 1:
  country = input("Type Country ==>")
  result = utilis.population_by_country(data, country.     
  capitalize())
  values = list(result[0].values())
  values_years = values[5:14]
  years = ["2022",   
  "2020","2015","2010","2000","1990","1980","1970"]
  year_values = dict(zip(years, values_years))
  for key, value in year_values.items():
    year_values[key] = int(value)
  charts.generate_bar_char(country,year_values.keys(),   
  year_values.values())
elif tipo_graficto == 2:
  continents = []
  for i in range(len(data)):
    continents.append(data[i]["Continent"])
  continents = list(set(continents))
  options = [x for x in range(len(continents))]
  options_continents = dict(zip(options, continents))
  for key, value in options_continents.items():
    print(key, value )
  option_user = int(input("Selecciona el Continente\n"))
  continent = options_continents[option_user]
  data_continent = utilis.population_by_continent(data,      continent)
  density = utilis.get_population(data_continent)
  labels = list(density.keys())
  values = list(density.values())
  charts.generate_pie_bar(continent ,labels, values)