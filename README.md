# ⚡ FastAPI REST API - Modern Backend & Pydantic Validation

Este projeto demonstra a criação de uma API REST de alta performance utilizando **FastAPI**. O foco principal é a estruturação de rotas modulares, o uso de esquemas de validação de dados com **Pydantic** e a implementação de operações assíncronas no ecossistema Python.

---

# 📝 Resumo (Resume)
Neste projeto, desenvolvi uma API escalável seguindo o padrão de separação de responsabilidades. Utilizei o **APIRouter** para organizar as rotas, garantindo que o núcleo da aplicação (`main.py`) permaneça limpo. A grande vantagem explorada aqui foi a integração com o **Pydantic**, onde criei um `UsuarioSchema` para garantir que as requisições POST contenham dados válidos (ID como inteiro e nome como string), gerando automaticamente a documentação interativa da API (Swagger UI).



## 🚀 Tecnologias e Ferramentas (Tech Stack)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-05998B?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92067?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)

## 📋 Funcionalidades em Destaque
* **Roteamento Modular (APIRouter):** Organização das rotas de usuários em arquivos separados, facilitando a expansão do sistema para novos recursos.
* **Validação Automática com Pydantic:** Uso de classes que herdam de `BaseModel` para validar tipos de entrada e saída, eliminando erros de dados mal-formatados.
* **Documentação Automática:** A API gera nativamente os endpoints `/docs` (Swagger) e `/redoc`, permitindo testar as rotas instantaneamente no navegador.
* **Operações REST (GET & POST):** Implementação de listagem de recursos e criação de novos usuários com persistência em memória.
* **Tipagem Estrita (Type Hints):** Uso extensivo das dicas de tipo do Python para garantir um código mais seguro, legível e com suporte total do IntelliSense.
* **Arquitetura de Modelos vs Esquemas:** Separação clara entre a classe de domínio `Usuario` e o esquema de transferência de dados `UsuarioSchema`.



---

# 👨‍💻 Sobre mim (About Me)
Olá, meu nome é **Kaio**, tenho 22 anos. Como meu objetivo é o **Back-End com Python**, o FastAPI é uma ferramenta chave no meu portfólio. Notei que trabalhar com Pydantic é extremamente familiar após minha experiência com **TypeScript** no Front-End; ambos focam em garantir que o dado que trafega na aplicação
