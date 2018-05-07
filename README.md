# Filmow to Letterboxd

## Gera um csv compatível com o import do Letterboxd com os filmes marcados como já vistos na conta do Filmow do usuário informado.

1. Faça download do código em Clone or download > Download ZIP

2. Instale Python 3 (A opção "Add Python 3.6 to PATH" deve ficar selecionada)
    - https://www.python.org/downloads/

3. Abra o Prompt de Comando
    - Win+R > digite cmd > OK

No cmd faça:

4. Instale Requests usando `pip install requests`

5. Instale Pandas usando `pip install pandas`

6. Instale BeautifulSoup usando `pip install beautifulsoup4`

7. Rode o script usando `python <caminho-para-o-arquivo>script.py` 
    -  Mude o `caminho-para-o-arquivo` para onde você fez o download do arquivo `script.py`.
    Exemplo: `C:\Users\Larissa\Desktop\filmowreader\script.py`
    
8. Ao rodar o código, você terá que informar o seu nome de usuário no filmow, então é só esperar terminar a execução do código! 
    (Talvez demore um pouquinho! Quer dizer que você viu muitos filmes :D)

9. Quando terminar será gerado o arquivo `./filmes.csv`, que é o seu diretório atual.

10. Agora é só importar o seu csv no https://letterboxd.com/. Para isso vá em Settings > IMPORT & EXPORT > IMPORT YOUR DATA