import PySimpleGUI as sg
sg.theme("azure3")
sg.theme_text_color("#C1CDCD")
window = sg.Window(title="Profile",
layout=[[sg.Text("SELAMAT DATANG DI KELAS",
font=("Arial",25))],
[sg.Text("NPM : 22100100545 ")],
[sg.Text("Nama : SLAMET RAMADHAN ")],
[sg.Text("Kelas: 5A Non - Regular Banjarmasin ")]
],
size=(500,200),
font=("Times", 18))
window()
window.close()