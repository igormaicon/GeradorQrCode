import qrcode

# Dados que você quer codificar no QR Code
print('O que deseja codificar em QR Code?:')
data = input()

# Perguntar ao usuário o nome do arquivo
print('Qual nome você gostaria de dar para o arquivo do QR Code? (sem extensão):')
nome_arquivo_base = input()
nome_arquivo = f"{nome_arquivo_base}.png"

# Criar o objeto QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adicionar os dados ao QR Code
qr.add_data(data)
qr.make(fit=True)

# Criar a imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salvar a imagem
img.save(nome_arquivo)

print(f"QR Code gerado com sucesso e salvo como {nome_arquivo}")