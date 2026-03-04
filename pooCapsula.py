class Capsula:

    def calculoComValordaCapsula(self):
        while True:
            print("DIGITE TODAS AS INFORMAÇÕES SEM CARACTER!")
            pesoCapsula = input("Digite o peso da capsula: ")
            quantidadeEmUnd = input("Digite a quantidade de unidades que deseja converter: ")
            try:
                intPesoCapsula = int(pesoCapsula)
                intQuantidadeEmUnd = int(quantidadeEmUnd)
                valorEmKg = (intPesoCapsula * intQuantidadeEmUnd)/1000

                resultado = f"{valorEmKg:,.3f}".replace(".", ",")
                print("\nvocê devera pesar: ",resultado, "mg", "\nque será o mesmo que: ", quantidadeEmUnd, "und")

                break
            except ValueError:

                print("ERRO!")

    def calculoSemPesoDaCapsula(self):
        while True:
            print("DIGITE TODAS AS INFORMAÇÕES SEM CARACTER!")
            pesoDaCaixa = input("Digite o peso da caixa em mg: ")
            quantidadeDecapsulasDentroDaCaixa = input("Digite a quantidade de capsulas desta Caixa: ")
            quantidadeEmUnd = input("Digite a quantidade de unidades que deseja converter: ")

            try:
                intPesoCaixa = int(pesoDaCaixa)
                intquantidadeDecapsulasDentroDaCaixa = int(quantidadeDecapsulasDentroDaCaixa)
                intquantidadeEmUnd = int(quantidadeEmUnd)

                pesoCapsula = intPesoCaixa / intquantidadeDecapsulasDentroDaCaixa
                valorEmKg = (pesoCapsula * intquantidadeEmUnd)/1000

                resultado = f"{valorEmKg:,.3f}".replace(".", ",")

                print("O peso da capsula é de: ", pesoCapsula, "mg")
                print("\nvocê devera pesar: ",resultado, "mg", "\nque será o mesmo que: ", quantidadeEmUnd, "und")

                break

            except ValueError: 

                print("ERRO!")