from tkinter import *
from tkinter import ttk
from googletrans import Translator
'''Для избежания ошибок при работе скрипта
рекомендуется устанавливать именно googletrans==3.1.0a0
'''
translator = Translator()


# Функция для создания и размещения элементов на главном окне
def create_widgets(root):
    root.title("Переводчик")
    root.geometry("700x500")

    header = ttk.Label(root, text="Перевод на русский")
    header.place(x=10, y=450)

    lang = StringVar(value="Перевод на русский")
    russian_lang = ttk.Radiobutton(
        root,
        text="Перевод на русский",
        value="Перевод на русский",
        variable=lang
    )
    russian_lang.pack()
    russian_lang.place(x=170, y=150)

    english_lang = ttk.Radiobutton(
        root,
        text="Перевод на английский",
        value="Перевод на английский",
        variable=lang
    )
    english_lang.place(x=430, y=150)

    editor = Text(root)
    editor.pack(fill=BOTH, expand=1)
    editor.place(x=100, y=40, width=500, height=70)

    output_text = Text(root)
    output_text.pack(fill=BOTH, expand=1)
    output_text.place(x=100, y=250, width=500, height=70)

    button = ttk.Button(root, text="Перевести", command=translate_text)
    button.pack()
    button.place(x=295, y=200)

    return lang, editor, output_text


def translate_text():
    text = editor.get('1.0', 'end')
    output_text.delete('1.0', 'end')

    if lang.get() == "Перевод на русский":
        result = translator.translate(text, dest='ru')
    elif lang.get() == "Перевод на английский":
        result = translator.translate(text, dest='en')

    output_text.insert("1.0", result.text)


root = Tk()
lang, editor, output_text = create_widgets(root)

root.mainloop()
