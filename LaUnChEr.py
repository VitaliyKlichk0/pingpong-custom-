from customtkinter import*


class ConnectWindow(CTk):
    def __init__ (self):
        super().__init__()
        self.geometry ('700x600')
        self.configure (fg_color='#121212')
        self.title ('Agario')
        self.resizable (False, False)
        main_font = ('Helvetica', 15, 'bold')
        self.name = None
        self.host = None
        self.port = None

        CTkLabel (self, text='Ping-Pong',font=("impact",100,'bold'), text_color="#14e252").pack(pady=20)
        
        self.Name = CTkEntry (self,
        placeholder_text='Ваш нік: ',

        height=47,
        font=main_font, 
        corner_radius=25, 
        fg_color="#161616",
        border_color="#666666",
        text_color="#666666",
        placeholder_text_color="#929292"
        )
        self.Name.pack(fill='x', padx=60, pady=20)
        

        self.Host = CTkEntry (self,
        placeholder_text='🌐IP-адреса:',
        height= 47,
        font=main_font,
        corner_radius=25,
        fg_color="#161616",
        border_color="#666666",
        text_color="#666666",
        placeholder_text_color="#929292"
        )
        self.Host.pack(fill='x',padx=60, pady=20)


        self.Port = CTkEntry (self,
        placeholder_text='🔌Порт:',
        height= 47,
        font=main_font,
        corner_radius=25,
        fg_color="#161616",
        border_color="#666666",
        text_color="#666666",
        placeholder_text_color="#929292"
        )
        self.Port.pack(fill='x',padx = 60,pady=20)


        self.sign_up_button = CTkButton(self,
        text='GO',
        height = 55,
        font=main_font,
        corner_radius=25,
        text_color="#FFFFFF",
        fg_color="#20e673",
        hover_color="#16b357",
        command=self.open_game
        )
        self._status_label = None
        self.sign_up_button.pack(fill='x', padx=240, pady=20)

        
    def open_game(self):
       self.name = self.Name.get()
       self.host = self.Host.get()
       self.port = self.Port.get()
       self.destroy()
