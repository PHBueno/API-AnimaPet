# API-AnimaPet

## Como executar o Projeto
O projeto foi desenvolvido em Python, utilizando o framework FastAPI para a criação de uma API REST simples.

- Verifique se o python 3.9 está instalado
- Crie um ambiente virtual (`python3.9 -m venv venv`);
- Execute o ambiente virtual (Linux: `source venv/bin/activate`, Windows: (`.\venv\Scripts\activate`))
- Realize as instalações das dependências (`pip install -r requirements.txt`);
- Após instalar as dependências execute o UviCorn :) (`uvicorn main:app --reload`);

## TESTES
Para a criação dos testes, foi utilizada a biblioteca [Behave](https://behave.readthedocs.io/en/stable/).
Os arquivos de testes estão no diretório `features`.

- Para rodar os testes NO LINUX execute (`behave`) no terminal:
    - Para executar as Features separadamente, execute: `behave -i features/<feature_name>`
- Para rodar os testes NO WINDOWS rode o comando (`Run behave`) no terminal:
    - Para executar as Features separadamente, executa: `Run behave -i features/<feature_name>`