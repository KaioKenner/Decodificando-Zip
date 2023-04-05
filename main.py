import zipfile

zip_file = "teste.zip"
senha_correta = "-"
with zipfile.ZipFile(zip_file, 'r') as zip_ref:

    for x in range(0, 10):
        for w in range(0, 10):
            for j in range(0, 10):
                for k in range(0, 10):

                    senha_atual = str(x) + str(w) + str(j) + str(k)


                    try:
                        zip_ref.extractall(pwd=senha_atual.encode())
                        print(f"A senha correta é: {senha_atual}")
                        break
                    except:

                        continue