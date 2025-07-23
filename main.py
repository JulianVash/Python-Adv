'''
import this


from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())



import pkg
print(pkg.URL)
print(pkg.mod_1.func_1())

'''

import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  '''

if __name__ == '__main__':
  run()