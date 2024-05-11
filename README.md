# Projeto: Recomendador de Cursos Alura via Google Generative AI

## Objetivo do Projeto

Este projeto visa desenvolver uma ferramenta de recomendação de cursos personalizados da Alura, utilizando a API do Google Generative AI. O objetivo é auxiliar profissionais a identificar os cursos mais relevantes para seu desenvolvimento, baseado em uma análise detalhada de seus currículos.

## Problema que o Projeto Resolve

Com a vasta oferta de cursos disponíveis, identificar quais são os mais adequados para o desenvolvimento profissional de um indivíduo pode ser desafiador. Este projeto automatiza a análise de currículos e a recomendação de cursos, proporcionando sugestões personalizadas que ajudam profissionais a alcançar seus objetivos de carreira de forma mais eficaz.

## Descrição de Funcionamento

1. **Leitura e Extração de Dados do Currículo**:
   - O projeto extrai o texto de um arquivo PDF de currículo armazenado em um repositório do GitHub.
   - **Atenção:** É necessário subir seu currículo no formato PDF na pasta 'cv' no projeto do GitHub. Recomenda-se não usar espaço, acentuação ou caracteres especiais no nome do arquivo.

2. **Configuração da API Google Generative AI**:
   - A API é configurada para gerar respostas baseadas em prompts detalhados que analisam o currículo e recomendam cursos.

3. **Análise do Currículo**:
   - Um prompt específico é utilizado para analisar o currículo, extraindo informações como experiência profissional, principais áreas de atuação, soft-skills, conhecimentos técnicos e ferramentas utilizadas.

4. **Recomendação de Cursos**:
   - Baseado na análise do currículo, são recomendados cursos da Alura, focados em aprimorar habilidades e conhecimentos relevantes para o profissional.

5. **Interação com o Usuário**:
   - O usuário pode interagir com a IA para tirar dúvidas sobre a análise do currículo e as recomendações de cursos.

## Tecnologias Utilizadas

- **Python**
- **Google Generative AI API**
- **PyPDF2**: Para extração de texto de arquivos PDF.
- **Requests**: Para realizar requisições HTTP e obter arquivos PDF do GitHub.

## Orientações de Uso

1. **Subir Currículo**:
   - Coloque seu currículo em formato PDF na pasta `cv` do projeto no GitHub.
   - **Recomendações para o nome do arquivo**:
     - Não use espaços, acentuações ou caracteres especiais.
   - Informe o nome do arquivo na variável `CV_NAME` no código para garantir que o currículo correto seja analisado.

2. **Configuração da API**:
   - Configure a chave da API do Google Generative AI na variável `GOOGLE_API_KEY`.

3. **Execução do Código**:
   - O código está configurado para buscar o PDF do currículo e da lista de cursos diretamente do GitHub.
   - Após a análise do currículo, a IA gera um relatório detalhado e recomenda cursos.

4. **Interação com a IA**:
   - Utilize o prompt interativo para fazer perguntas adicionais à IA sobre a análise e recomendações.

## Informações Relevantes

- **Dependências**:
  - Certifique-se de ter as bibliotecas `google.generativeai`, `PyPDF2` e `requests` instaladas no seu ambiente Python.
- **Segurança**:
  - O projeto inclui configurações de segurança para filtrar conteúdo inadequado.

Sinta-se à vontade para explorar e personalizar as recomendações de cursos baseados nas necessidades específicas de desenvolvimento profissional. Este projeto facilita o processo de identificação de cursos relevantes, promovendo um aprendizado contínuo e direcionado.
