# Filmow to Letterboxd

## Gera um csv compatível com o import do Letterboxd com os filmes marcados como já vistos na conta do Filmow do usuário informado.

### (Instruções para windows)

1. Crie uma pasta para colocar o código, faça download do projeto em "Clone or download > Download ZIP", o coloque nessa pasta e extraia o arquivo. Ou clone o projeto com:
```
git clone https://github.com/larissamoreira/filmow_to_letterboxd.git
```

2. Instale Python 3 (A opção "Add Python 3.6 to PATH" deve ficar selecionada)
    - https://www.python.org/downloads/

3. Abra o Prompt de Comando
    - Win+R > digite cmd > OK

No terminal, entre na pasta onde está o projeto, com `cd <caminho-para-pasta>`. Agora é necessário instalar as dependências para o código funcionar, crie um ambiente virtual para que tudo ocorra dentro dele:

```
python -m venv ambiente
```
Ambiente criado, agora o ative com:
```
ambiente\Scripts\activate
```

Por fim, instale as dependências:
```
pip install -r requirements.txt
```

4. Hora de rodar o código, para isso entre na pasta do projeto com
```
cd filmow_to_letterboxd-master
```
e faça: 
```
python script.py
```
    
5. Ao rodar o código, você terá que informar o seu nome de usuário no filmow, então é só esperar terminar a execução do código! 
    (Talvez demore um pouquinho! Quer dizer que você viu muitos filmes :D)

6. Quando terminar será gerado o arquivo `./filmes.csv`, que é o seu diretório atual.

7. Agora é só importar o seu csv no https://letterboxd.com/. Para isso vá em Settings > IMPORT & EXPORT > IMPORT YOUR DATA