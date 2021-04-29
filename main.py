from tkinter import *
from tkinter import messagebox as msgbx
from tkinter import scrolledtext as st
from time import sleep
from threading import Thread
from random import choice

list_texts_to_show = [
    "Puede que la tarea que me he impuesto de escribir una historia completa del pueblo romano desde el comienzo mismo de su existencia me recompense por el trabajo invertido en ella, no lo sé con certeza, ni creo que pueda aventurarlo. Porque veo que esta es una práctica común y antiguamente establecida, cada nuevo escritor está siempre persuadido de que ni lograrán mayor certidumbre en las materias de su narración, ni superarán la rudeza de la antigüedad en la excelencia de su estilo. Aunque esto sea así, seguirá siendo una gran satisfacción para mí haber tenido mi parte también en investigar, hasta el máximo de mis capacidades, los anales de la nación más importante del mundo, con un interés más profundo; y si en tal conjunto de escritores mi propia reputación resulta ocultada, me consuelo con la fama y la grandeza de aquellos que eclipsen mi fama.",
    "Hace años, y de intento no se señala cuál, hubo en México una causa célebre. Los autos pasaban de 2,000 fojas y pasaban también de manos de un juez a las de otro juez, sin que pudieran concluir. Algunos de los magistrados tuvieron una muerte prematura y muy lejos de ser natural. Personas de categoría y de buena posición social estaban complicadas, y se hicieron, por este y otros motivos, poderosos esfuerzos para echarle tierra, como se dice comúnmente; pero fue imposible. El escándalo había sido grande, la sociedad de la capital y aun de los Estados había fijado su atención, y se necesitaba un castigo ejemplar para contener desmanes que tomaban grandes proporciones. Se hicieron muchas prisiones, pero a falta de pruebas, los presuntos reos eran puestos en libertad. Al fin llegó a descubrirse el hilo, y varios de los culpables fueron juzgados, condenados a muerte y ejecutados. El principal de ellos, que tenía una posición muy visible, tuvo un fin trágico.",
    "En el año 1878 obtuve el título de doctor en medicina por la Universidad de Londres, asistiendo después en Netley a los cursos que son de rigor antes de ingresar como médico en el ejército. Concluidos allí mis estudios, fui puntualmente destinado el 5.0 de Fusileros de Northumberland en calidad de médico ayudante. El regimiento se hallaba por entonces estacionado en la India, y antes de que pudiera unirme a él, estalló la segunda guerra de Afganistán. Al desembarcar en Bombay me llegó la noticia de que las tropas a las que estaba agregado habían traspuesto la línea montañosa, muy dentro ya de territorio enemigo. Seguí, sin embargo, camino con muchos otros oficiales en parecida situación a la mía, hasta Candahar, donde sano y salvo, y en compañía por fin del regimiento, me incorporé sin más dilación a mi nuevo servicio.",
    "Acostumbran los historiadores ¡oh Sosio Seneción!, cuando en la descripción de los países hay puntos de que no tienen conocimiento, suprimir éstos en la carta, poniendo en los últimos extremos de ella esta advertencia: de aquí adelante no hay sino arenales faltos de agua y silvestres, o pantanos impenetrables, o hielos como los de la Escitia, o un mar cuajado. Pues a este modo, habiendo yo de escribir estas vidas comparadas, en las que se tocan tiempos a que la atinada crítica y la historia no alcanzan, acerca de ellos me estará muy bien prevenir igualmente: de aquí arriba no hay más que sucesos prodigiosos y trágicos, materia propia de poetas y mitólogos, en la que no se encuentra certeza ni seguridad. Y habiendo escrito del legislador Licurgo y del rey Numa, me parece que no será fuera de propósito subir hasta Rómulo, pues que tanto nos acercamos a su tiempo; pero examinando, para decirlo con Esquilo.",
    "La triste necesidad, que me ha tenido siempre con un pie sobre el cuello, me obliga a vender mis Memorias. Nadie puede hacerse una idea de cuánto he sufrido por tener que hipotecar mi tumba; pero me obligan a este postrer sacrificio mis juramentos y la coherencia de mi conducta. Por un apego acaso pusilánime, consideraba estas Memorias como confidentes de los que nunca hubiera querido separarme; mi intención era legárselas a madame de Chateaubriand; ella las daría a conocer según su voluntad, o las destruiría, lo que hoy desearía más que nunca.",
    "En el principio sólo existía el Caos. El Cielo y la Tierra formaban una masa confusa, en la que el todo y la nada se entremezclaban como la suciedad en el agua. Por doquier reinaba una espesa niebla que jamás logró ver ojo humano y a la que Pan-Ku consiguió dispersar con su portentosa fuerza. Lo puro quedó entonces separado de lo impuro y apareció la suprema bondad, que esparce sus bendiciones sobre toda criatura. Su mundo es el de la luz. Quien a él se acerca descubre el camino que conduce al reino del bien. Mas el que quiera penetrar en el secreto del principio de cuanto existe debe leer La crónica de los orígenes.",

]
seconds_to_write = 60
seconds_counted = 0
words_typed = 0
stop_program = False
text_to_show = choice(list_texts_to_show)
list_words_to_write = text_to_show.split(" ")
list_words_written = []
total_words = len(list_words_to_write)

desk_app = Tk()
desk_app.title("Type Speed Test")
desk_app.config(bg="#063A3F")
desk_app.geometry("1000x650")


def background_task(func, args):
    th = Thread(target=func, args=args)
    th.start()
    return th


def write_record_wpm(wpm):
    with open("record_WPM.txt", mode="w") as file:
        file.write(str(wpm))


def get_record_wpm():
    with open("record_WPM.txt") as file:
        return int(file.readline())


def words_correctly_typed():
    words_correct = 0
    for _ in range(words_typed):
        if list_words_written[_][:-1] == list_words_to_write[_]:
            words_correct += 1
    return words_correct


def finish_program():
    global words_typed, seconds_counted, list_words_written, stop_program, record_wpm, text_to_show, list_words_to_write

    user_entry_txt.config(state="disabled")
    stop_program = True

    if words_typed > record_wpm:
        write_record_wpm(words_typed)
        record_wpm = get_record_wpm()

    restart = msgbx.askretrycancel(title="WPM",
                                   message=f"Your wrote {words_typed} words in {seconds_counted} "
                                           f"seconds, WPM = {words_typed}, and {words_correctly_typed()} "
                                           f"words were typed correctly.")

    if restart:
        words_typed = 0
        seconds_counted = 0
        list_words_written = []
        text_to_show = choice(list_texts_to_show)
        list_words_to_write = text_to_show.split(" ")
        area_text.config(state="normal")
        area_text.delete("0.0", END)
        area_text.insert(INSERT, text_to_show)
        area_text.config(state="disabled")
        label_seconds["text"] = f"Time: {seconds_to_write}s"
        label_words_written["text"] = f"Words: 0/{total_words}"
        user_entry_txt.config(state="normal")
        user_entry_txt.delete(0, END)
        user_entry_txt.focus()
        stop_program = False
        background_task(detect_first_key_entry, ())
    else:
        desk_app.destroy()


def time_counter():
    global seconds_to_write, seconds_counted, stop_program

    while seconds_counted < seconds_to_write and not stop_program:
        sleep(1)
        seconds_counted += 1
        label_seconds["text"] = f"Time: {seconds_to_write - seconds_counted}s"
    if not stop_program:
        finish_program()


def detect_word_typed():
    global words_typed
    finish_text = False

    while not finish_text and not stop_program:
        new_word = user_entry_txt.get()

        if " " in new_word:
            user_entry_txt.delete(0, END)
            list_words_written.append(new_word)
            if words_typed == 120:
                area_text.see(END)
            words_typed += 1
            label_words_written["text"] = f"Words: {words_typed}/{total_words}"
        sleep(0.07)


def detect_first_key_entry():
    text_in_entry_space = ""
    while text_in_entry_space == "":
        text_in_entry_space = user_entry_txt.get()

    background_task(time_counter, ())
    detect_word_typed()


record_wpm = get_record_wpm()

title = Label(text="Type Speed Test", bg="#063A3F", fg="white", font=("Courier", 35, "bold"))
title.grid(column=1, row=0, pady=12)

label_words_written = Label(text=f"Words: 0/{total_words}", bg="#063A3F", fg="white", font=("helvetica", 15))
label_words_written.grid(column=0, row=0)

label_seconds = Label(text=f"Time: {seconds_to_write}s", bg="#063A3F", fg="white", font=("helvetica", 15))
label_seconds.grid(column=2, row=0)

area_text = st.ScrolledText(width=58, height=13, bg="#317379", fg="white", font=("Courier", 20), wrap="word")
area_text.insert(INSERT, text_to_show)
area_text.configure(state='disabled')
area_text.grid(column=0, row=1, pady=30, padx=25, columnspan=3)

label_record_wpm = Label(text=f"Record\n{record_wpm} WPM", bg="#063A3F", fg="white", font=("helvetica", 13))
label_record_wpm.grid(column=2, row=2)

user_entry_txt = Entry(width=20, font=("helvetica", 16))
user_entry_txt.focus()
user_entry_txt.grid(column=1, row=2)

button_restart = Button(text="Restart", bg="#063A3F", fg="white", font=("helvetica", 13), command=finish_program)
button_restart.grid(column=0, row=2)

background_task(detect_first_key_entry, ())

desk_app.mainloop()
