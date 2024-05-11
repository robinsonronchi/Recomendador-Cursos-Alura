import re

def extract_courses_from_html(html_content):
    # Regex para encontrar todos os cursos
    pattern = re.compile(r'card-curso__nome">(.*?)</span>')
    courses = pattern.findall(html_content)
    return courses

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_courses_to_txt(courses, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for course in courses:
            file.write(course + '\n')

def main():
    input_file = 'cursos-alura.html'  # Substitua pelo caminho do seu arquivo .html
    output_file = 'courses_list.txt'

    # Lê o conteúdo do arquivo HTML
    html_content = read_html_file(input_file)

    # Extrai os nomes dos cursos
    courses = extract_courses_from_html(html_content)

    # Escreve os nomes dos cursos em um arquivo .txt
    write_courses_to_txt(courses, output_file)
    print(f"Lista de cursos salva em {output_file}")

if __name__ == "__main__":
    main()