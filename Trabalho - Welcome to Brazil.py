from tkinter import *

'''Cada class são telas do aplicativo. 
Ao todo são 17 telas. Todas interligadas em condições de erros e acertos.'''

class Tela_final(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Tela')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')

        self.widgets()
        root.mainloop()

    def widgets(self):
        # Texto 1
        self.titulo_txt1 = Label(self,
                                 text='Welcome\nTo\nBrazil',
                                 font=('Bookman Old Style', 72, 'bold'))
        self.titulo_txt1.place(relx=0.02, rely=0.13)

        # Texto 2
        self.titulo_txt1 = Label(self,
                                 text='Obrigado por jogar!',
                                 font=('Bookman Old Style', 26))
        self.titulo_txt1.place(relx=0.02, rely=0.02)

        self.btn_continuar = Button(
            self,
            text='Jogar\n Novamente',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_continuar)
        self.btn_continuar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

    # Metódos de invocação de uma nova janela
    def clica_continuar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p1(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p5_erro(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Você Errou')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')
        # Imagem
        self.foto = PhotoImage(file='WTB_p5E.png')
        self.img_centro = Label(self, image=self.foto)
        self.img_centro.place(relx=0.21, rely=0.25)

        self.widgets()
        root.mainloop()

    def widgets(self):
        # Título 1 da Pergunta
        self.titulo_txt1 = Label(self,
                                 text='Acordaaa menino,\nAcordaaaa menina,\nvocê errou!',
                                 font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt1.place(relx=0.22, rely=0.02)

        self.btn_continuar = Button(
            self,
            text='Ir para o fim',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_continuar)
        self.btn_continuar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

    # Metódos de invocação de uma nova janela
    def clica_continuar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_final(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p5_acerto(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Você Acertou')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')
        # Imagem
        self.foto = PhotoImage(file='WTB_p5A.png')
        self.img_centro = Label(self, image=self.foto)
        self.img_centro.place(relx=0.29, rely=0.25)

        self.widgets()
        root.mainloop()

    def widgets(self):
        # Título 1 da Pergunta
        self.titulo_txt1 = Label(self,
                                 text='Você acertou!',
                                 font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt1.place(relx=0.25, rely=0.17)

        self.btn_continuar = Button(
            self,
            text='Ir para o fim',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_continuar)
        self.btn_continuar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

    # Metódos de invocação de uma nova janela
    def clica_continuar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_final(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p5(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Pergunta')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')

        self.widgets()
        root.mainloop()

    def widgets(self):
        # Título 1 da Pergunta
        self.titulo_txt = Label(self,
                                text='O Bolsonaro gastou quantos reais\n com leite condensado?',
                                font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt.place(relx=0, rely=0.17)

        self.btn_1 = Button(
            self,
            text='R$ 15 milhões',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_1)
        self.btn_1.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

        self.btn_2 = Button(
            self,
            text='R$ 16 milhões',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_2)
        self.btn_2.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.2)

    # Metódos de invocação de uma nova janela
    def clica_1(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p5_acerto(self)  # Próxima janela para ser aberta

    def clica_2(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p5_erro(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p4_erro(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Você Errou')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')
        # Imagem
        self.foto = PhotoImage(file='WTB_p4E.png')
        self.img_centro = Label(self, image=self.foto)
        self.img_centro.place(relx=0.21, rely=0.25)

        self.widgets()
        root.mainloop()

    def widgets(self):
        # Título 1 da Pergunta
        self.titulo_txt1 = Label(self,
                                 text='Você errou!',
                                 font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt1.place(relx=0.2, rely=0.17)

        self.btn_continuar = Button(
            self,
            text='Próxima Fase',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_continuar)
        self.btn_continuar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

    # Metódos de invocação de uma nova janela
    def clica_continuar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p5(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p4_acerto(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Você Acertou')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')
        # Imagem
        self.foto = PhotoImage(file='WTB_p4A.png')
        self.img_centro = Label(self, image=self.foto)
        self.img_centro.place(relx=0.21, rely=0.25)

        self.widgets()
        root.mainloop()

    def widgets(self):
        self.btn_continuar = Button(
            self,
            text='Próxima Fase',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_continuar)
        self.btn_continuar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

        self.titulo_txt1 = Label(self,
                                 text='Você Acertou!',
                                 font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt1.place(relx=0.22, rely=0.12)


    # Metódos de invocação de uma nova janela
    def clica_continuar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p5(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p4(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Pergunta')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')

        self.widgets()
        root.mainloop()

    def widgets(self):
        # Título 1 da Pergunta
        self.titulo_txt = Label(self,
                                text='O Mister Catra\ntem quantos filhos?',
                                font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt.place(relx=0.23, rely=0.17)

        self.btn_1 = Button(
            self,
            text='32',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_1)
        self.btn_1.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

        self.btn_2 = Button(
            self,
            text='23',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_2)
        self.btn_2.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.2)

    # Metódos de invocação de uma nova janela
    def clica_1(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p4_acerto(self)  # Próxima janela para ser aberta

    def clica_2(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p4_erro(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p3_erro(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Você Errou')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')
        # Imagem
        self.foto = PhotoImage(file='WTB_p3E.png')
        self.img_centro = Label(self, image=self.foto)
        self.img_centro.place(relx=0.2, rely=0.25)

        self.widgets()
        root.mainloop()

    def widgets(self):
        # Título 1 da Pergunta
        self.titulo_txt1 = Label(self,
                                 text='Você teve Pocahs ideias e errou',
                                 font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt1.place(relx=0.05, rely=0.17)

        self.btn_continuar = Button(
            self,
            text='Próxima Fase',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_continuar)
        self.btn_continuar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

    # Metódos de invocação de uma nova janela
    def clica_continuar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p4(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p3_acerto(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Você Acertou')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')
        # Imagem
        self.foto = PhotoImage(file='WTB_p3A.png')
        self.img_centro = Label(self, image=self.foto)
        self.img_centro.place(relx=0.2, rely=0.25)

        self.widgets()
        root.mainloop()

    def widgets(self):
        #Título 1 da Pergunta
        self.titulo_txt1 = Label(self,
                                text='O Brasil tá lascado',
                                font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt1.place(relx=0.23, rely=0.17)

        self.btn_continuar = Button(
            self,
            text='Próxima Fase',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command = self.clica_continuar)
        self.btn_continuar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

#Metódos de invocação de uma nova janela
    def clica_continuar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p4(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p3(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Pergunta')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')

        self.widgets()
        root.mainloop()

    def widgets(self):
        #Título 1 da Pergunta
        self.titulo_txt = Label(self,
                                text='O que é Basculho?',
                                font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt.place(relx=0.2, rely=0.17)

        self.btn_1 = Button(
            self,
            text='Gíria\nNordestina;\nServir pra\n nada, resto.',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command= self.clica_1)
        self.btn_1.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

        self.btn_2 = Button(
            self,
            text='Ser feio,\n mal arrumado.',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command= self.clica_2)
        self.btn_2.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.2)

#Metódos de invocação de uma nova janela
    def clica_1(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p3_acerto(self)  # Próxima janela para ser aberta

    def clica_2(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p3_erro(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p2_erro(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Você Errou')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')
        # Imagem
        self.foto = PhotoImage(file='WTB_p2E.png')
        self.img_centro = Label(self, image=self.foto)
        self.img_centro.place(relx=0.2, rely=0.25)

        self.widgets()
        root.mainloop()

    def widgets(self):
        # Título 1 da Pergunta
        self.titulo_txt1 = Label(self,
                                 text='Seu histórico de atleta\n não foi suficiente.\nAliste-se as Forças Armadas!',
                                 font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt1.place(relx=0.09, rely=0.09)

        self.btn_continuar = Button(
            self,
            text='Próxima Fase',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_continuar)
        self.btn_continuar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

    # Metódos de invocação de uma nova janela
    def clica_continuar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p3(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p2_acerto(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Você Acertou')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')
        # Imagem
        self.foto = PhotoImage(file='WTB_p2A.png')
        self.img_centro = Label(self, image=self.foto)
        self.img_centro.place(relx=0.27, rely=0.25)

        self.widgets()
        root.mainloop()

    def widgets(self):
        #Título 1 da Pergunta
        self.titulo_txt1 = Label(self,
                                text='Você tá ligado na Maju',
                                font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt1.place(relx=0.17, rely=0.09)
        # Título 1 da Pergunta
        self.titulo_txt1 = Label(self,
                                 text='Jornalista Brasileira responável por quebrar\npadrões de estética para uma apresentadora.',
                                 font=('Bookman Old Style', 19))
        self.titulo_txt1.place(relx=0.05, rely=0.17)

        self.btn_continuar = Button(
            self,
            text='Próxima Fase',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command = self.clica_continuar)
        self.btn_continuar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

#Metódos de invocação de uma nova janela
    def clica_continuar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p3(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p2(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Pergunta')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')

        self.widgets()
        root.mainloop()

    def widgets(self):
        #Título 1 da Pergunta
        self.titulo_txt = Label(self,
                                text='Quem é o atual Ministro da Saúde?',
                                font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt.place(relx=0, rely=0.17)

        self.btn_queiroga = Button(
            self,
            text='Marcelo\n Queiroga',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command= self.clica_queiroga)
        self.btn_queiroga.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

        self.btn_teich = Button(
            self,
            text='Nelson Teich',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command= self.clica_teich)
        self.btn_teich.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.2)

#Metódos de invocação de uma nova janela
    def clica_queiroga(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p2_acerto(self)  # Próxima janela para ser aberta

    def clica_teich(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p2_erro(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p1_erro(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Você Errou')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')
        # Imagem
        self.foto = PhotoImage(file='WTB_p1E.png')
        self.img_centro = Label(self, image=self.foto)
        self.img_centro.place(relx=0.2, rely=0.25)

        self.widgets()
        root.mainloop()

    def widgets(self):
        # Título 1 da Pergunta
        self.titulo_txt1 = Label(self,
                                 text='Você errou e virou Jacaré',
                                 font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt1.place(relx=0.12, rely=0.17)

        self.btn_continuar = Button(
            self,
            text='Próxima Fase',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_continuar)
        self.btn_continuar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

    # Metódos de invocação de uma nova janela
    def clica_continuar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p2(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p1_acerto(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Você Acertou')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')
        # Imagem
        self.foto = PhotoImage(file='WTB_p1A.png')
        self.img_centro = Label(self, image=self.foto)
        self.img_centro.place(relx=0.2, rely=0.25)

        self.widgets()
        root.mainloop()

    def widgets(self):
        # Título 1 da Pergunta
        self.titulo_txt1 = Label(self,
                                 text='Parabéns Jovem, você acertou',
                                 font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt1.place(relx=0.10, rely=0.17)

        self.btn_continuar = Button(
            self,
            text='Próxima Fase',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_continuar)
        self.btn_continuar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

    # Metódos de invocação de uma nova janela
    def clica_continuar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p2(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_p1(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Pergunta')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')

        self.widgets()
        root.mainloop()

    def widgets(self):
        #Título 1 da Pergunta
        self.titulo_txt1 = Label(self,
                                text='Qual a Vacina mais eficaz?',
                                font=('Bookman Old Style', 26, 'bold'))
        self.titulo_txt1.place(relx=0.12, rely=0.08)

        # Título 2 da Pergunta
        self.titulo_txt2 = Label(self,
                                text='Que deveria ter sido comprada',
                                font=('Bookman Old Style', 19, 'bold'))
        self.titulo_txt2.place(relx=0.18, rely=0.17)

        # Título 3 da Pergunta
        self.titulo_txt3 = Label(self,
                                text='pelo governo brasileiro no começo da pandemia.',
                                font=('Bookman Old Style', 19, 'bold'))
        self.titulo_txt3.place(relx=0.01, rely=0.22)

        self.btn_moderna = Button(
            self,
            text='Moderna',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_moderna)
        self.btn_moderna.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

        self.btn_pfizer = Button(
            self,
            text='Pfizer',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command= self.clica_pfizer)
        self.btn_pfizer.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.2)

#Metódos de invocação de uma nova janela
    def clica_pfizer(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p1_acerto(self)  # Próxima janela para ser aberta

    def clica_moderna(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p1_erro(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

class Tela_Info(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Informações')
        self.resizable(False, False)
        self.geometry('640x630+400+20')
        # Icone
        self.iconbitmap('WTB.ico')
        self.widgets()
        root.mainloop()

    def widgets(self):
        self.btn_entrar = Button(
            self,
            text='Iniciar Jogo',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command= self.clica_entrar)
        self.btn_entrar.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.2)

        # Texto 1.1
        self.titulo_txt1 = Label(self,
                                 text='Welcome to Brazil é um aplicativo de perguntas e respostas',
                                 font=('Bookman Old Style', 16))
        self.titulo_txt1.place(relx=0.02, rely=0.17)
        # Texto 1.2
        self.titulo_txt1 = Label(self,
                                 text='relacionadas a acontecimentos da atualidade no Brasil.',
                                 font=('Bookman Old Style', 16))
        self.titulo_txt1.place(relx=0.05, rely=0.22)
        # Texto 1.3
        self.titulo_txt1 = Label(self,
                                 text='Ele funciona basicamente gerando perguntas para o usuário',
                                 font=('Bookman Old Style', 16))
        self.titulo_txt1.place(relx=0.02, rely=0.27)
        # Texto 1.4
        self.titulo_txt1 = Label(self,
                                 text='Colaboradores:\n\nGabriel Leopoldino;\nKauã Alves;\nLavínia Dias;\nRafaela Rodrigues.',
                                 font=('Bookman Old Style', 16))
        self.titulo_txt1.place(relx=0.31, rely=0.38)

        #Metódos de invocação de uma nova janela
    def clica_entrar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p1(self)  # Próxima janela para ser aberta
    def hide(self):
        self.withdraw()
    def show(self):
        self.update()
        self.deiconify()

class App:
    def __init__(self): # Metódo Construtor
        self.root = root
        self.tela()
        self.widgets()
        root.mainloop()

    def tela(self):     # Configurações da tela
        self.root.title('Welcome to Brazil')
        self.root.geometry('640x630+400+20')
        self.root.configure(bg='#009C3B')
        self.root.resizable(False,False)
        #Icone
        self.root.iconbitmap('WTB.ico')
        # Imagem
        self.foto = PhotoImage(file='WTB_Capa.png')
        self.img_centro = Label(self.root, image=self.foto)
        self.img_centro.place(relx=0.001, rely=0.05)

    def widgets(self):
        self.btn_entrar = Button(
            self.root,
            text='Iniciar Jogo',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_entrar)
        self.btn_entrar.place(relx=0.15, rely=0.77, relwidth=0.3, relheight=0.2)

        self.btn_info = Button(
            self.root,
            text='Informações',
            bg='yellow',
            font=('Bookman Old Style', 20),
            command=self.clica_info)
        self.btn_info.place(relx=0.55, rely=0.77, relwidth=0.3, relheight=0.2)

        #Metódos de invocação de uma nova janela
    def clica_info(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_Info(self)  # Próxima janela para ser aberta

    def clica_entrar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_p1(self)  # Próxima janela para ser aberta

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()

##### APP PORINCIPAL #####
root = Tk()
App()