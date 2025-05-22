import base64

def criptografar_base64(texto):
    texto_bytes = texto.encode('utf-8')
    texto_base64 = base64.b64encode(texto_bytes)
    return texto_base64.decode('utf-8')

def descriptografar_base64(criptografado):
    bytes_base64 = criptografado.encode('utf-8')
    texto_original = base64.b64decode(bytes_base64)
    return texto_original.decode('utf-8')

def validar_senha(senha):
    if(senha == "senhaFoda"):
        return True
    else:
        return False
