import os

TOKEN = os.getenv("TOKEN_INTELITECH")
print(f"Debug: TOKEN_INTELITECH={TOKEN}")  # Apenas para verificar se está pegando o valor

if not TOKEN:
    raise ValueError("TOKEN não encontrado ou inválido.")