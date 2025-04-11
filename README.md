# Gerador de QR Code em Python

Este é um projeto simples em Python que permite gerar códigos QR a partir de textos ou links fornecidos pelo usuário.

## Como Usar

Para usar este gerador de QR Code, siga os passos abaixo:

1.  **Pré-requisitos:** Certifique-se de ter o Python instalado no seu computador. Você pode baixá-lo em [https://www.python.org/downloads/](https://www.python.org/downloads/).

2.  **Instalação da Biblioteca:** Abra o seu terminal ou prompt de comando e instale a biblioteca `qrcode` usando o pip:

    ```bash
    pip install qrcode
    ```

3.  **Execução do Script:** Salve o código Python do gerador de QR Code (por exemplo, como `gerador_qr.py`). Navegue até a pasta onde você salvou o arquivo no seu terminal e execute o script com o comando:

    ```bash
    python gerador_qr.py
    ```

4.  **Entrada de Dados:** O programa irá perguntar:

    ```
    O que deseja codificar em QR Code?:
    ```

    Digite o texto ou o link que você deseja transformar em QR Code e pressione Enter.

5.  **Nome do Arquivo:** Em seguida, o programa perguntará:

    ```
    Qual nome você gostaria de dar para o arquivo do QR Code? (sem extensão):
    ```

    Digite o nome desejado para o arquivo da imagem (sem a extensão `.png`) e pressione Enter.

6.  **Resultado:** O QR Code será gerado e salvo como um arquivo `.png` com o nome que você especificou na mesma pasta onde o script está sendo executado. Uma mensagem de sucesso será exibida no terminal.

## Exemplo de Uso

1.  Execute o script: `python gerador_qr.py`
2.  O programa pergunta: `O que deseja codificar em QR Code?:`
3.  Você digita: `https://github.com/igormaicon` e pressiona Enter.
4.  O programa pergunta: `Qual nome você gostaria de dar para o arquivo do QR Code? (sem extensão):`
5.  Você digita: `perfil_github` e pressiona Enter.
6.  Será gerado um arquivo chamado `perfil_github.png` com o QR Code para o seu perfil do GitHub.

## Contribuição e Feedback

Se você tiver alguma sugestão de melhoria, encontrar algum erro ou tiver alguma ideia para tornar este projeto ainda melhor, por favor, sinta-se à vontade para me avisar! Você pode:

* **Abrir uma Issue:** Se você encontrar um bug ou tiver uma sugestão específica, você pode abrir uma nova "Issue" na aba de "Issues" do repositório no GitHub.
* **Enviar um Pull Request:** Se você quiser contribuir com código, pode fazer um "fork" do repositório, fazer as suas alterações e enviar um "Pull Request" para que eu possa revisar e incorporar as suas mudanças.
* **Deixar um comentário:** Você também pode deixar um comentário na página do repositório.

Seu feedback é muito importante para o desenvolvimento deste projeto!

## Autor

Este projeto foi desenvolvido por Igor Maicon Rocha de Jesus Muniz.

## Licença

MIT License

Copyright (c) 2025 Igor Maicon Rocha de Jesus Muniz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

