import requests
from bs4 import BeautifulSoup

# URL do arquivo .html no GitHub
url = 'https://github.com/robinsonronchi/Recomendador-Cursos-Alura/blob/main/Cursos%20online%20de%20tecnologia%2C%20design%20e%20neg%C3%B3cios%20digitais%20da%20Alura.html'

# Função para buscar cursos no HTML
def buscar_cursos(url):
    # Requisição HTTP para obter o conteúdo do arquivo .html
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

    # Parsing do conteúdo HTML com BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Busca por todos os cursos identificados pela tag <span class="card-curso__nome">
    cursos = soup.find_all('span', class_='card-curso__nome')

    # Criação da lista de cursos
    lista_cursos = [curso.get_text(strip=True) for curso in cursos]

    return lista_cursos

# Função para salvar a lista de cursos em um arquivo .txt
def salvar_cursos(cursos, arquivo_saida):
    with open(arquivo_saida, 'w') as file:
        for curso in cursos:
            file.write(f"{curso}\n")

# URL do arquivo .html no GitHub (substitua pela URL correta)
url = 'https://raw.githubusercontent.com/robinsonronchi/Recomendador-Cursos-Alura/blob/main/Cursos%20online%20de%20tecnologia%2C%20design%20e%20neg%C3%B3cios%20digitais%20da%20Alura.html'

# Busca pelos cursos
cursos = buscar_cursos(url)

# Salva a lista de cursos em um arquivo .txt
arquivo_saida = 'cursos_alura.txt'
salvar_cursos(cursos, arquivo_saida)

print(f"Lista de cursos salva em {arquivo_saida}")

