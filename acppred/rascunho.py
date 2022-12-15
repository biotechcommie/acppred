class Model:
    algorithm = 'random_forest'

model_1 = Model()
model_1.algorithm = 'neural network'

model_2 = Model()

print(model_1.algorithm)
print(model_2.algorithm)

# cod abaixo não funciona pois falta método construtor
# model_1 = Model('tentativa sem init')
# model_2 = Model(algorithm='tentativa sem init de novo')

# print(model_1.algorithm)
# print(model_2.algorithm)

# o self é como o THIS do Java, o algorithm da linha def é a variável que a função recebe como parametro de entrada
  # def __init__(self, algorithm):
  #     self.algorithm = algorithm
  #   def fit (self):
   #     print('Modelo não treinado ainda')

# duas formas de enviar o valor da variável, pra função do objeto - de maneira sequencial ou 
# alocando diretamente o valor em uma variavel específica
# model_1 = Model('neural  network')
# model_2 = Model(algorithm='random forest')

# print(model_1.algorithm)
# print(model_2.algorithm)
# model_1.fit()