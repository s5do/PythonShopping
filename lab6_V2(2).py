from tkinter import *

def add():
    # Копируем выбранные товары в корзину
    for i in lis1.curselection(): # возвращает индексы
        tovar = lis1.get(i) # значение эл-та
        lis2.insert(END, tovar) # товар в конец списка
    lis1.selection_clear(0, END) # снимает выделение

def delete():
    # Удаляем выбранные товары из корзины
    for i in reversed(lis2.curselection()): # перебор в обратном пор-ке
        lis2.delete(i)


root = Tk()
root.title("Магазин")
root.geometry("500x350")

lab1 = Label(root, text="Товары")
lab1.grid(row=0, column=0, padx=30, pady=10)

lab2 = Label(root, text="Корзина")
lab2.grid(row=0, column=1, padx=30, pady=10)

tovari = ["Хлеб", "Молоко", "Сыр", "Яблоки",
          "Сок", "Масло", "Сахар", "Чай"]

# можно выбирать несколько товаров
lis1 = Listbox(root, selectmode=MULTIPLE, width=25, height=12) # список товаров
lis1.grid(row=1, column=0, padx=20)

lis2 = Listbox(root, selectmode=MULTIPLE, width=25, height=12) # корзина
lis2.grid(row=1, column=1, padx=20) # список товаров в окне

for i in tovari:
    lis1.insert(END, i) # товары в конец списка

but1 = Button(root, text="Добавить", command=add)
but1.grid(row=2, column=0, pady=10)

but2 = Button(root, text="Удалить", command=delete)
but2.grid(row=2, column=1, pady=10)

root.mainloop() # гланвй цикл обр-ки