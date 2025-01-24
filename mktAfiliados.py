import os

TOKEN = os.getenv("TOKEN_AFILIADOS")
print(f"Debug: TOKEN_AFILIADOS={TOKEN}")  # Apenas para verificar se está pegando o valor

if not TOKEN:
    raise ValueError("TOKEN não encontrado ou inválido.")