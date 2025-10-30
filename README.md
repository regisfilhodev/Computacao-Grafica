# Extração de Features com o Descritor DAISY 🌀

Este projeto demonstra como extrair descritores locais de uma imagem utilizando o método **DAISY** da biblioteca `scikit-image`. O objetivo é entender e visualizar como o algoritmo representa características visuais da imagem em forma de vetores de descritores.

---

## Bibliotecas Utilizadas

O código utiliza as seguintes bibliotecas:

- `matplotlib.pyplot` → Para exibir imagens e visualizações.
- `skimage.io` → Para leitura de imagens.
- `skimage.color` → Para conversão da imagem para tons de cinza.
- `skimage.feature.daisy` → Para extração dos descritores DAISY.

---

## Como Executar

1. Instale as dependências:

```bash
pip install scikit-image matplotlib
````

2. Coloque uma imagem chamada `imagem.jpeg` no mesmo diretório do main.
3. Execute o projeto com Python:

```bash
python main.py
```

Se tudo estiver correto, será exibida uma janela mostrando a imagem original à esquerda e a visualização dos descritores DAISY à direita.