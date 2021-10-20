import requests
import tkinter as tk
#API PARA CONSULTAR O CLIMA
#api.openweathermap.org/data/2.5/weather?q={city name}&appid=89ad8ce4ebae22808286cec213ed99a5
#COVID = https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/sp 

class Tela:

    def __init__(self, master):


        cab = tk.PhotoImage(file="cab.png")
        img = tk.Label(janela, image=cab)
        img.cab = cab
        img.config(bg="#F2F2F2")
        img.place(x=40, y=1)

        
        self.cidade = tk.Label(janela, text="Código UF:")
        self.cidade["font"] = ("Lucida", "17")
        self.cidade.config(bg="#F2F2F2", foreground="black")
        self.cidade.place(x=50, y=85)
        
        self.cidadeE = tk.Entry(janela)
        self.cidadeE["font"] = ("Lucida", "17")
        self.cidadeE.config(foreground="darkblue")
        self.cidadeE.place(x=175, y=89, height=25, width=100)

        self.bt = tk.Button(janela, text="Consultar")
        self.bt.place(x=360, y=85, width=100)
        self.bt["font"] = ("Arial", "13")
        self.bt.config(bg="brown", foreground="white")
        self.bt.bind("<Button-1>", self.consultar)

        self.bt2 = tk.Button(janela, text="Limpar")
        self.bt2.place(x=285, y=85, width=70)
        self.bt2["font"] = ("Arial", "13")
        self.bt2.config(bg="black", foreground="white")
        self.bt2.bind("<Button-1>", self.limpar)

    def consultar(self, event):

        cd = self.cidadeE.get()

        
        
        r = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{}'.format(cd))
        teste = r.json()
        
        r2=('Mortes atualmente: {}'.format(teste['deaths']))
        r3=('Quantidade de casos: {}'.format(teste['cases']))
        r4=('Suspeitas: {}'.format(teste['suspects']))
        r5=('Data da atualização: {}'.format(teste['datetime']))

        
        self.lb = tk.Label(janela, text=r2)
        self.lb.config(foreground="red")
        self.lb["font"] = ("Arial", "17")
        self.lb.config(bg="#DCDCDC")
        self.lb.place(x=40, y=155)

        self.lb2 = tk.Label(janela, text=r3)
        self.lb2.config(foreground="#B22222")
        self.lb2["font"] = ("Arial", "17")
        self.lb2.config(bg="#DCDCDC")
        self.lb2.place(x=40, y=195)

        self.lb3 = tk.Label(janela, text=r4)
        self.lb3.config(foreground="maroon")
        self.lb3["font"] = ("Arial", "17")
        self.lb3.config(bg="#DCDCDC")
        self.lb3.place(x=40, y=235)

        self.lb4 = tk.Label(janela, text=r5)
        self.lb4.config(foreground="black")
        self.lb4["font"] = ("Arial", "15")
        self.lb4.place(x=5, y=355)

    def limpar(self, event):

        self.cidadeE.delete(0, "end")
        
        self.lb2 = tk.Label(janela, text="")

       

        

janela = tk.Tk()
Tela(janela)
janela.config(bg="#F2F2F2")
janela.resizable(width=False,height=False)
janela.geometry("470x400")
janela.title('DADOS COVID-19')
janela.mainloop()





