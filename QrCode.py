import qrcode
import tkinter as tk

class App():
     def __init__(self, toplevel):
         toplevel.geometry("500x200")
#         #URL
         self.frame1 = tk.Frame(toplevel)
         self.frame1.pack(fill="both",padx=20,pady=20)
       
#         # Nome arquivo
         self.frame2 = tk.Frame(toplevel)
         self.frame2.pack(fill="both",padx=20,pady=20)
        
         #botao
         self.frame3 = tk.Frame(toplevel)
         self.frame3.pack(fill="both", padx=10, pady=5)

         self.label = tk.Label(self.frame1, text="Digite sua URL: ")
         self.label.pack(side="left")
         self.endereco = tk.Entry(self.frame1,width=80)
         self.endereco.pack(side="right")

         self.label2 = tk.Label(self.frame2, text="Nome do arquivo: ")
         self.label2.pack(side="left")
         self.nome = tk.Entry(self.frame2,width=80)
         self.nome.pack(side="right")

         self.buttton= tk.Button(self.frame3, text= "Gerar",
         command=self.gerar)
         self.buttton.pack(side="bottom")
        
         self.label3 = tk.Label(self.frame3,text="")
         self.label3.pack(side="bottom")

     def gerar(self):
         endereco= self.endereco.get()
         nome= self.nome.get()

         if endereco != nome:
             imagem= qrcode.make(f'{endereco}')
             imagem.save(f'{nome}.jpg')       
             self.label3['text']=" Qr.code gerado"
        
         else:

             self.label3['text']= " Qr.code não gerado"

raiz = tk.Tk()
app = App(raiz)
raiz.mainloop()
