from bs4 import BeautifulSoup
import requests

# Obtener el código HTML de la página
url = 'https://www.example.com'
response = requests.get(url)
html = response.text

# Crear un objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Buscar todas las etiquetas de estilo que contengan valores de color
colors = set()
for tag in soup.find_all(style=True):
    style = tag['style']
    for color in re.findall(r'(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}|rgb\(\d{1,3},\s?\d{1,3},\s?\d{1,3}\))', style):
        colors.add(color)

# Imprimir los colores encontrados
print(colors)
