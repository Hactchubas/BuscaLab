# 🔍 BuscaLab

 Projeto baseado em outro projeto que fiz parte: Projeto Integrado 1 (https://github.com/Hactchubas/techplan-projeto-integrado1) do curso de Sistemas e Mídias Digitais diurno na Universidade Federal do Ceará

 Afim de expandir meus conhecimentos de desenvolvimento FullStack, dessa vez usando o framework Django, resolvi refazer o projet com essa tecnologia, aproveitando das ferramentas e estrutura que o framework me proporciona para construir um aplicação confiável, escalável e de qualidade.

 
## 📃 Descrição
 
Projeto Integrado 1 é um projeto da equipe TechPlan (da qual faço parte) juntamente com o suporte técnico do curso de Sistemas e Mídias Digitais. O intuito do projeto é criar um site, onde seja possível visualizar e modificar o inventário de hardware e software dos laboratórios do bloco, por exemplo visualizar e modificar número de máquinas em cada laboratório, modelo de máquinas, potência das máquinas presente nos laboratórios, softwares disponíveis em cada laboratório e etc.

Além disso o site também contará com um Help Desk para que os usuários possam reportar quaisquer problemas que ocorrerem com os laboratórios.
Com foco em dois tipos principais de usuário:
- Usuário comum: usa a aplicação para buscar informações do inventário e faz reportes sobre porblemas que encontrou. Para este usuário, como o principal modo de utilização é o celular seguimos com uma metodologia de mobile first.
- Usuário suporte: usa a aplicação para além de buscar informações poder adicionar, excluir e editá-las, além de poder visualizar todos os reportes feitos por usuários comuns. Como seu principla método de utilização é o desktop, a página para esse usuário foi pensada nesse perfil de utilização.


 <br>

 ![](https://img.shields.io/badge/HTML5-122E40?style=for-the-badge&logo=html5&logoColor=white)
 ![](https://img.shields.io/badge/CSS3-122E40?style=for-the-badge&logo=css3&logoColor=white)
 ![](https://img.shields.io/badge/JavaScript-122E40?style=for-the-badge&logo=javascript&logoColor=white)
 ![](https://img.shields.io/badge/Python-122E40?style=for-the-badge&logo=python&logoColor=white)
 
 ![](https://img.shields.io/badge/-Django-122E40?style=for-the-badge&logo=django&logoColor=white)&nbsp;
 ![](https://img.shields.io/badge/-SQLite-122E40?style=for-the-badge&logo=sqlite&logoColor=white)&nbsp;
 
 ![Visual Studio Code](https://img.shields.io/badge/-Visual%20Studio%20Code-122E40?style=for-the-badge&logo=visual-studio-code&logoColor=007ACC&labelColor=122E40&logoColor=white)&nbsp;
 ![GitHub](https://img.shields.io/badge/-GitHub-122E40?style=for-the-badge&logo=github&labelColor=122E40&logoColor=white)&nbsp;
 

 ## ⚙ CONFIGURAÇÕES
Recomendado rodar e instalar as dependências do projeto em um ambiente virtual:
- Basta no terminal dentro da pasta do projeto rodar o comando: ```python -m venv nome_do_ambiente```

Primeiro, quem utilizar o código, precisa ter esses elementos instalados:

- `PYTHON 3`: Instalar o Python 3 na sua máquina.(Pode ser a extensão do VS Code ou pelo link: https://www.python.org/downloads/)
- `DJANGO`: Dentro do VS Code, instalar a biblioteca Django no terminal com o seguinte código: ```pip install django```
- `SQLite3`: Baixe o arquivo .zip na página https://www.sqlite.org/download.html e extraia os arquivos para dentro da pasta Scripts no ambiente virtual do seu projeto.


<a id="ancora5"></a>
## 🛠️ COMO RODAR?

Para rodar o código, precisa ter todas as configurações ajustadas.
 - 1- Inicie o servidor com: ```python manage.py runserver```
 - 2- Espere o servidor iniciar e com a tecla Alt presionado clique no IP do server
 - 3- Adicione "/BuscaLab" ao final da url para acessar o aplicativo do projeto.
