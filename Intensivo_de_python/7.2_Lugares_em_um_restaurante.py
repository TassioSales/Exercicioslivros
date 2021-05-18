mesaUser = str(input("Ola Voce precisa de uma mesa para quantas pessoa ?"))

if mesaUser.isnumeric() and mesaUser >= 8:
    mesaUser = int(mesaUser)
else:
    print("ERRO, a quantida informado não e adequada")

if mesaUser >= 8:
    print('''Não temos mesas suficentes para essas quantidade de pessoas teria como agurar alguns minutos ate termos mesas suficentes para acomodarmos vcs..''')
else:
  print("Sua mesa ja esta pronta. Por favor queira se acomodar")
    