import pandas as pd
from pandas_datareader import data
from IPython.display import display


def VerificaMes(x, y):
    if x in y:
        return 1
    else:
        print("\nDesculpe, tente novamente.")


def AlteraValor(x, z):
    tabela.loc[x, MesSelecionado] = z
    tabela.to_excel("Finanças22.xlsx")


def AlteraValorFixo(x, z):
    tabela2.loc[x, MesSelecionado] = z
    tabela2.to_excel("Finanças22fixo.xlsx")


def AlteraNomeFixo(x, z):
    tabela2.loc[x, 'Nome'] = z
    tabela2.to_excel("Finanças22fixo.xlsx")


def MudarNovamente():
    MudarAlgo_N = input("\nDeseja fazer mais alguma alteração [s/n]? ")
    if MudarAlgo_N.lower() == "s":
        return 1
    elif MudarAlgo_N.lower() == "n":
        print("\nOK! Até mais.\n")
        return 0
    else:
        print("\nPor favor, digite 's' para sim e 'n' para não, apenas. \n")


def MudarValor(x, y, z, k):

    j = 1
    while (j != 0):
        pergunta = input(
            "\nAtualmente {} do mes de {} é de R$ {} . Deseja altera-lo [s/n]? ".format(x, y, z))
        if pergunta.lower() == 's':
            valor = float(input("\nPara qual valor deseja altera-lo? "))
            AlteraValor(k, valor)
            j = 0
        elif pergunta.lower() == 'n':
            print("\nOK!")
            j = 0
        else:
            print("\nPor favor, digite 's' para sim e 'n' para não, apenas. \n")
            j = 1


def VoltaMenu():
    l = 1
    while (l != 0):
        Menu = input("\nDeseja retornar para o menu [s/n]? ")
        if Menu.lower() == "s":
            l = 0
            p = 1
        elif Menu.lower() == "n":
            exit("\nOK! até mais!\n")
            l = 0
            p = 0
        else:
            print("\nPor favor, digite 's' para sim e 'n' para não, apenas. \n")
            l = 1


def RegTag():
    i = 0
    Registro_tag = 1
    while (Registro_tag != 0):
        if (tabela2['Nome'][i] == nada):
            Nome_fixo = input(
                "\nDigite um nome para a tag: ")
            AlteraNomeFixo(i, Nome_fixo)
            Preço_fixo = float(input("\nDigite o valor: "))
            AlteraValorFixo(i, Preço_fixo)
            break
        elif (tabela2['Nome'][i] != nada):
            i = i + 1
            Registro_tag = 1


tabela = pd.read_excel("Finanças22.xlsx", usecols=[1,
                                                   2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
tabela2 = pd.read_excel("Finanças22fixo.xlsx", index_col="n")
nada = "-"
zero = 0
tabela['titulos'].fillna(nada, inplace=True)
tabela.fillna(zero, inplace=True)
tabela2["Nome"].fillna(nada, inplace=True)
tabela2.fillna(zero, inplace=True)


meses = ["nothing", "janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

print('\nOi, bem vindo! Vamos começar...')

p = 1
while (p != 0):
    print("\n1 - Ver meus dados atuais\n2 - Alterar dados\n3 - Ver gastos fixos apenas\n4 - Alterar gastos fixos\n5 - Sair\n")
    op = int(input("O que deseja fazer? "))

    match op:
        case 1:
            print('Estes são seus dados atuais:\n')
            display(tabela)
            VoltaMenu()
        case 2:
            k = 1
            while (k != 0):

                print('\n')
                for i in range(1, 13):
                    m = "{} - " + meses[i]
                    print(m.format(i))

                mes = int(input("\nQual mês você deseja acessar? "))

                MesSelecionado = meses[mes]

                Verifica_mes = VerificaMes(MesSelecionado, meses)

                if Verifica_mes == 1:
                    fixo = tabela2[MesSelecionado][10]
                    if (tabela[MesSelecionado][0] == zero):
                        entrada = float(
                            input("\nDigite o valor que entrou esse mês: "))
                        AlteraValor(0, entrada)
                    else:
                        entrada = tabela[MesSelecionado][0]
                        MudarValor("a entrada", MesSelecionado, entrada, 0)
                        entrada = tabela[MesSelecionado][0]
                    if (tabela[MesSelecionado][2] == zero and tabela2[MesSelecionado][10] == zero):
                        print(
                            "\nSeus dados de gastos fixos estão vazios, por favor preencha os dados na tabela de gastos fixos")
                        fixo = tabela[MesSelecionado][2]
                    else:
                        fixo = tabela2[MesSelecionado][10]
                        AlteraValor(2, fixo)
                    if (tabela[MesSelecionado][4] == zero):
                        investe = float(input(
                            "\nDigite a porcentagem que você deseja invesir esse mês (recomenda-se 15%): "))
                        investir = entrada*(investe/100)
                        AlteraValor(4, investir)
                    else:
                        investir = tabela[MesSelecionado][4]
                        MudarValor("o valor investido",
                                   MesSelecionado, investir, 4)
                        investir = tabela[MesSelecionado][4]
                    if (tabela[MesSelecionado][7] == zero):
                        GastoVariavel = float(
                            input("\nDigite os gastos desse mês até agora: "))
                        AlteraValor(7, GastoVariavel)
                    else:
                        Variavel = input(
                            "\nVocê obteve algum gasto a mais [s/n]? ")
                        j = 1
                        while (j != 0):
                            if Variavel.lower() == 's':
                                GastoVariavel = tabela[MesSelecionado][7]
                                GastoVariavelNovo = float(
                                    input("\nDigite quanto você gastou: "))
                                GastoVariavel = GastoVariavel + GastoVariavelNovo
                                AlteraValor(7, GastoVariavel)
                                j = 0
                            elif Variavel.lower() == 'n':
                                GastoVariavel = tabela[MesSelecionado][7]
                                print("\nOK!")
                                j = 0
                            else:
                                print(
                                    "\nPor favor, digite 's' para sim e 'n' para não, apenas. \n")
                                j = 1
                    PD_Gastar = entrada - (fixo+investir+GastoVariavel)
                    AlteraValor(10, PD_Gastar)
                    print("\nPronto! Seus dados foram alterados.\n")
                    print("Seu saldo disponível para gasto é de: R$ {}\n".format(
                        tabela.loc[10, MesSelecionado]))
                    VerTabela = input(
                        "\nDeseja ver a tabela com seus dados atualizados [s/n]? ")
                    j = 1
                    while (j != 0):
                        if VerTabela.lower() == "s":
                            print('\n')
                            display(tabela)
                            k = MudarNovamente()
                            j = 0
                        elif VerTabela.lower() == "n":
                            k = MudarNovamente()
                            j = 0
                        else:
                            print(
                                "\nPor favor, digite 's' para sim e 'n' para não, apenas. \n")
                            j = 1
        case 3:
            display(tabela2)
            VoltaMenu()
        case 4:
            print('\n')
            for i in range(1, 13):
                m = "{} - " + meses[i]
                print(m.format(i))

            mes = int(input("\nQual mês você deseja acessar? "))

            MesSelecionado = meses[mes]

            Verifica_mes = VerificaMes(MesSelecionado, meses)

            if Verifica_mes == 1:
                Cadastro = 1
                while (Cadastro != 0):
                    tag_reg = input(
                        "\nDeseja cadastrar alguma tag fixa [s/n]? ")
                    if tag_reg.lower() == "s":
                        RegTag()
                        Cadastro2 = 1
                        while (Cadastro2 != 0):
                            outra_tag = input(
                                "\nDeseja cadastrar outra tag fixa [s/n]? ")
                            if outra_tag.lower() == "s":
                                RegTag()
                            elif outra_tag.lower() == "n":
                                break
                            else:
                                print(
                                    "\nPor favor, digite 's' para sim e 'n' para não, apenas. \n")
                                Cadastro2 = 1
                        break
                    elif tag_reg.lower() == "n":
                        break
                    else:
                        print(
                            "\nPor favor, digite 's' para sim e 'n' para não, apenas. \n")
                        Cadastro = 1
                TotalFixo = tabela2[MesSelecionado].sum()
                AlteraValorFixo(10, TotalFixo)
                AlteraValor(2, TotalFixo)
                PD_Gastar = PD_Gastar - TotalFixo
                AlteraValor(10, PD_Gastar)
            VoltaMenu()
        case 5:
            exit("\nAté mais!\n")
        case _:
            print("\nTente uma opção válida!\n")
