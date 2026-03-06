class Capsula:

    def calculoComValordaCapsula(self):
        while True:
            print("DIGITE TODAS AS INFORMAÇÕES SEM CARACTER!")
            pesoCapsula = input("Digite o peso da capsula(ex: 98,0 mg = 98): ")
            quantidadeEmUnd = input("Digite a quantidade de unidades que deseja converter: ")
            try:
                intPesoCapsula = int(pesoCapsula)
                intQuantidadeEmUnd = int(quantidadeEmUnd)

                valorEmKg = (intPesoCapsula * intQuantidadeEmUnd)/1000
                resultado = f"{valorEmKg:,.3f}".replace(".", ",")

                linha = f"você deverá pesar: {resultado} mg, que será o mesmo que: {quantidadeEmUnd} und\n"
                print(linha)

                arqHistorico = open("historico.txt","a")
                arqHistorico.write(linha)
                arqHistorico.close()

                break
            except ValueError:

                print("ERRO!VOCÊ USOU '.' OU ','")

    def calculoSemPesoDaCapsula(self):
        while True:
            print("DIGITE TODAS AS INFORMAÇÕES SEM CARACTER!")
            pesoDaCaixa = input("Digite o peso da caixa em mg(ex: 12kg = 12000): ")
            quantidadeDecapsulasDentroDaCaixa = input("Digite a quantidade de capsulas desta Caixa: ")
            quantidadeEmUnd = input("Digite a quantidade de unidades que deseja converter: ")

            try:
                intPesoCaixa = int(pesoDaCaixa)
                intquantidadeDecapsulasDentroDaCaixa = int(quantidadeDecapsulasDentroDaCaixa)
                intquantidadeEmUnd = int(quantidadeEmUnd)

                pesoCapsula = intPesoCaixa / intquantidadeDecapsulasDentroDaCaixa
                valorEmKg = (pesoCapsula * intquantidadeEmUnd)/1000

                resultado = f"{valorEmKg:,.3f}".replace(".", ",")

                linha = f"você devera pesar: {resultado} mg que será o mesmo que: {quantidadeEmUnd} und. O peso da capsula é de: {round(pesoCapsula,3)} mg"

                print(linha)

                arqHistorico = open("historico.txt","a")
                arqHistorico.write(linha)
                arqHistorico.close()

                break

            except ValueError: 

                print("ERRO!VOCÊ USOU '.' OU ','")

    def convercaoDePesoAlcool(self):
        pesorequerido = float(input("Digite o peso que em ml que é requisitado na op ex(21.000):"))
        calculoDeConvercao = round(pesorequerido * 0.808)

        linha = f"O peso em kg de {pesorequerido} é de {calculoDeConvercao} kg"
        print(linha)

        arqHistorico = open("historico.txt","a")
        arqHistorico.write(linha)
        arqHistorico.close()

    def historico(self):
        with open("historico.txt", "r") as arquivo:
            # 1. Pega todas as linhas e remove a última se estiver vazia
            linhas = [linha.strip() for linha in arquivo if linha.strip()]
            
            if linhas:
                # 2. Pega a última linha do arquivo
                ultima_linha = linhas[-1]
                
                # 3. Divide a linha pelo ';' e pega o último elemento da lista (índice -1)
                partes = ultima_linha.split(';')
                ultimo_valor = partes[-1].strip()
                
                print(f"O último valor salvo é: {ultimo_valor}")
            else:
                print("O arquivo está vazio.")

    def devolucaoCapsulas(self):
        while True:
            print("DIGITE TODAS AS INFORMAÇÕES SEM CARACTER!")
            peso_da_capsula =  input("digite o peso da capsula: ")
            peso_a_devolver = input("digite o peso que deseja converter para und: ")

            try:
                intPesoDaCapsula= int(peso_da_capsula)
                intPesoaDevolver = int(peso_a_devolver)
                devolver = intPesoaDevolver / intPesoDaCapsula

                resultado = f"{devolver:,.3f}".replace(".", ".")

                print(f"{intPesoaDevolver}kg será {resultado} und")

                break

            except ValueError:

                 print("ERRO!VOCÊ USOU '.' OU ','")   



        




