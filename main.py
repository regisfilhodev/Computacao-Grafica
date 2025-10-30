import matplotlib.pyplot as plt
from skimage import io, color
from skimage.feature import daisy

caminho_imagem = 'imagem.jpeg'

imagem = io.imread(caminho_imagem)
imagem_gray = color.rgb2gray(imagem)

descs, descs_img = daisy(imagem_gray, step=180, radius=58, rings=2, histograms=6, visualize=True)

print(f"Formato dos descritores: {descs.shape}")

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(imagem_gray, cmap='gray')
ax[0].set_title('Imagem Original')
ax[1].imshow(descs_img)
ax[1].set_title('Descritores DAISY')
for a in ax:
    a.axis('off')
plt.tight_layout()
plt.show()
