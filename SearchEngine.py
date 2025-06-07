from exa_py import Exa

exa = Exa('your Exa API key ID')

query = input('Search here: ')
response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.google.com'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()