import datetime
import json

id = 0
note = dict()
work = True


def create_note():
    global note
    global id
    note[id] = dict()
    note[id]['date'] = datetime.datetime.now().strftime('%H:%M %d.%m.%Y')
    note[id]['title'] = input('Введите тему заметки: \n')
    note[id]['content'] = input('Введите текст заметки: \n')
    note[id]['editing_date'] = '-'
    with open('notes.json', 'w') as file:
        json.dump(note, file, indent=2)
    print('Заметка успешно добавлена')
    id += 1


def delete_note():
    global note
    del note[int(input('Введите идентификатор заметки, которую хотите удалить: \n'))]
    with open('notes.json', 'w') as file:
        json.dump(note, file, indent=2)
    print('Заметка успешно удалена')


def edit_note():
    global note
    code = int(input('Введите идентификатор заметки, которую хотите изменить: \n'))
    note[code]['content'] = (input('Введите измененный текст заметки:\n'))
    note[code]['editing_date'] = datetime.datetime.now().strftime('%H:%M %d.%m.%Y')
    with open('notes.json', 'w') as file:
        json.dump(note, file, indent=2)
    print('Заметка успешно изменена')


def print_note_list():
    with open('notes.json', 'r') as file:
        note = json.load(file)
    for code, item in note.items():
        print(f"{code}: {item['date']} {item['title']} {item['content']} {item['editing_date']}")

while(work):
    temp = int(input('1 - создать заметку \n2 - редактировать заметку \n3 - удалить заметку \n4 - посмотреть все заметки \n0 - выход\n'))
    if temp == 1:
        create_note()
    if temp == 2:
        edit_note()
    if temp == 3:
        delete_note()
    if temp == 4:
        print_note_list()
    if temp == 0:
        work = False