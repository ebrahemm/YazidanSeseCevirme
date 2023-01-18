
# Gerekli kütüphaneler
from gtts import gTTS
import os
import tkinter as tk

root = tk.Tk()
root.title("Yazıdan sese çevirme uygulaması")

root.geometry("400x400+500+100")

# EVENT LISTENER için fonksiyonumuz
def create_mp3(lang="tr"):

    print(lan.get())
    if lan.get() != None:
        lang = str(lan.get())
    s = gTTS(text.get(0.0, tk.END), lang=lang)
    s.save(f"{str(mp3.get())}.mp3")
    filename = mp3.get() + ".mp3"
    os.system("start " + filename)


# WHERE YOU WRITE THE TEXT

# Dil Kısmı için 
 # label oluştur 
l2 = tk.Label(root, text="Dili seçiniz (default olarak tanımlanan dil  türkçe=tr)")
l2.pack()

    # Giriş aracı 
lan = tk.StringVar()
language = tk.Entry(root, textvariable=lan)
language.pack()
lan.set("tr")

title = tk.Label(root, text="kaydedilecek dosya adını aşağıya  giriniz..")
title.pack()

# kaydedilecek ses dosyasının  işlemleri 
mp3 = tk.StringVar()
mp3title = tk.Entry(root, textvariable=mp3, width=50)
mp3title.pack()
mp3.set("dosyam")

#
title = tk.Label(root, text="Metninizi aşağıya  giriniz..")
title.pack()
title['bg'] = 'turquoise'

# EVENT LISTENER kısmı 
root.bind("<Return>", lambda x: create_mp3())

t = tk.StringVar()
text = tk.Text(root, bg="orange")
text.pack()

root.mainloop()