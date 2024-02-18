import os

#obtém a variável de ambiente
env_var = os.getenv("MY_VARIABLE", "Valor padrão caso a variável não esteja definida")

#exibe o valor da variável de ambiente
print("Valor da variável de ambiente MY_VARIABLE:", env_var)
