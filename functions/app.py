from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

class Character:
    def __init__(self, name, true_attributes, image):
        self.name = name
        self.attributes = true_attributes
        self.image = image

characters = [
    # ======= 
    Character("Bapak", ["pria", "anakkesatu", "umurlebih_30", "bekerja", "manusia", "tidur", "suka_sayur", "uban", "bisa_motor", "menikah", "peliharaan", "hp", "tatto"], "https://i.ibb.co.com/S7H4W9C/20240530-142214.jpg"),
    Character("Mamak", ["anakkesatu", "umurlebih_30", "bekerja", "manusia", "lucu", "suka_sayur", "uban", "bisa_motor", "kepasar", "menikah", "peliharaan", "hp", "juarasatu"], "https://i.ibb.co.com/Scnqf3g/20240530-143804.jpg"),
    Character("I Wayan Lamat", ["anakkesatu", "meninggal", "umurlebih_30", "manusia", "suka_sayur", "uban", "menikah", "peliharaan"], "https://i.ibb.co.com/G0cRDnX/20240530-143255.jpg"),
    Character("Ni Wayan Pasti", ["anakkesatu", "umurlebih_30", "manusia", "lucu", "suka_sayur", "uban", "menikah", "peliharaan"], "https://i.ibb.co.com/8PFqSfm/20240530-144002.jpg"),
    Character("Aditya", ["pria", "anakkesatu", "manusia", "suka_sayur", "bisa_motor", "sekolah", "hp", "juarasatu", "peliharaan"], "https://i.ibb.co.com/19t6xP7/20240530-142121.jpg"),
    Character("Vika", ["manusia", "lucu", "tidur", "sekolah", "juarasatu", "peliharaan"], "https://i.ibb.co.com/qsP7pDL/20240530-141752.jpg"),
    Character("Jinny", ["meninggal", "lucu", "tidur"], "https://i.ibb.co.com/Y3Xk9th/20240530-143421.jpg"),
    Character("Chiko Cicik", ["pria", "suka_olahraga", "lucu", "tidur"], "https://i.ibb.co.com/Lt3sDXz/20240530-142502.jpg"),
    # ======= 
    Character("I Kadek Nurwata", ["pria", "umurlebih_30", "bekerja", "manusia", "lucu", "tidur", "suka_sayur", "bisa_motor", "menikah", "peliharaan", "hp", "tatto"], "https://i.ibb.co.com/s2PsvD4/20240530-145603.jpg"),
    Character("Buk Dek Diah", ["umurlebih_30", "bekerja", "manusia", "tidur", "suka_sayur", "bisa_motor", "menikah", "hp"], "https://i.ibb.co.com/D5cZxZN/20240530-145620.jpg"),
    Character("Agista Queen", ["anakkesatu", "manusia", "lucu", "hp"], "https://i.ibb.co.com/Fsp4RB0/20240530-145635.jpg"),
    # ======= 
    Character("Kak Epin", ["pria", "umurlebih_30", "bekerja", "manusia", "suka_sayur", "uban", "bisa_motor", "menikah", "peliharaan", "kuli", "hp", "tatto"], "https://i.ibb.co.com/MNSrk5T/20240530-144500.jpg"),
    Character("Dong Epin", ["umurlebih_30", "bekerja", "manusia", "suka_sayur", "uban", "bisa_motor", "kepasar", "menikah", "peliharaan", "canang"], "https://i.ibb.co.com/54kDQzf/20240530-142249.jpg"),
    Character("Pak Kris", ["pria", "anakkesatu", "bekerja", "suka_olahraga", "manusia", "tidur", "suka_sayur", "bisa_motor", "peliharaan", "hp", "tatto"], "https://i.ibb.co.com/pP7yMfq/20240530-144329.jpg"),
    Character("Pak Epin", ["pria", "bekerja", "suka_olahraga", "manusia", "tidur", "suka_sayur", "bisa_motor", "hp", "tatto", "peliharaan"], "https://i.ibb.co.com/d4vy7MM/20240530-144525.jpg"),
    Character("Choki", ["pria", "suka_olahraga", "lucu", "tidur", "kejar_ayam"], "https://i.ibb.co.com/W3QJK3C/20240530-142001.jpg"),
    # ======= 
    Character("Qprok", ["pria", "umurlebih_30", "bekerja", "manusia", "suka_sayur", "uban", "bisa_motor", "menikah", "kuli", "hp", "tatto"], "https://i.ibb.co.com/c88d0g3/20240530-145039.jpg"),
    Character("Mek Tut Cangi", ["umurlebih_30", "bekerja", "manusia", "lucu", "tidur", "suka_sayur", "uban", "bisa_motor", "kepasar", "menikah", "canang", "hp"], "https://i.ibb.co.com/74xg0xT/20240530-141906.jpg"),
    Character("Sepa", ["pria", "anakkesatu", "suka_olahraga", "manusia", "tidur", "suka_sayur", "bisa_motor", "sekolah", "peliharaan", "hp"], "https://i.ibb.co.com/BC8Mdq2/20240530-144714.jpg"),
    Character("Opet", ["pria", "manusia", "lucu", "suka_sayur", "sekolah", "hp", "kejar_ayam"], "https://i.ibb.co.com/Ttd8Jnt/20240530-141547.jpg"),
    # =======
    Character("Kakek Ubud", ["pria", "umurlebih_30", "bekerja", "manusia", "tidur", "suka_sayur", "uban", "bisa_motor", "menikah", "peliharaan", "hp", "kacamata"], "https://i.ibb.co.com/2NzFmrR/20240530-145218.jpg"),
    Character("Nenek Ubud", ["umurlebih_30", "bekerja", "manusia", "tidur", "suka_sayur", "uban", "bisa_motor", "menikah", "peliharaan", "hp", "kacamata"], "https://i.ibb.co.com/cY8Qp1B/20240530-145249.jpg"),
    Character("Antha", ["pria", "bekerja", "manusia", "tidur", "suka_sayur", "bisa_motor", "menikah", "peliharaan", "hp"], "https://i.ibb.co.com/cxt5PVH/20240530-143949.jpg"),
    Character("Citra", ["bekerja", "manusia", "tidur", "suka_sayur", "bisa_motor", "menikah", "peliharaan", "hp", "kacamata"], "https://i.ibb.co.com/Hr9921N/20240530-143929.jpg"),
    Character("Aurel", ["anakkesatu", "manusia", "tidur"], "https://i.ibb.co/LC6Pv77/20240501-224409.jpg"), #foto belum
    Character("Achi", ["lucu", "tidur", "lebihduaanak"], "https://i.ibb.co.com/0nrg2y5/20240530-143642.jpg"),
    Character("Kenta", ["pria", "lucu", "tidur", "cederakaki"], "https://i.ibb.co.com/NrbpRqQ/20240530-143539.jpg")
]

main_questions = [
    ("Apakah karakter ini seorang laki-laki?", "pria"),
    ("Apakah karakter ini adalah anak pertama?", "anakkesatu"),
    ("Apakah karakter ini sudah meninggal?", "meninggal"),
    ("Apakah karakter ini umurnya lebih dari 30 tahun?", "umurlebih_30"),
    ("Apakah karakter ini manusia?", "manusia")
]

supporting_questions = [
    ("Apakah karakter ini akhir-akir ini pernah bekerja?", "bekerja"),
    ("Apakah karakter ini suka berolahraga?", "suka_olahraga"),
    ("Apakah karakter ini manusia?", "manusia"),
    ("Apakah karakter ini memiliki uban (rambut berwarna putih) ?", "uban"),
    ("Apakah karakter ini bisa mengendarai motor?", "bisa_motor"),
    ("Apakah karakter ini sering ke pasar?", "kepasar"),
    ("Apakah karakter ini suka mengejar ayam?", "kejar_ayam"),
    ("Apakah karakter ini sudah menikah?", "menikah"),
    ("Apakah karakter ini masih sekolah?", "sekolah"),
    ("Apakah karakter ini botak?", "botak"),
    ("Apakah karakter ini bekerja sebagai kuli bangunan?", "kuli"),
    ("Apakah karakter ini sering membuat canang untuk dijual?", "canang"),
    ("Apakah karakter ini memiliki hp modern (bukan hp jadul)?", "hp"),
    ("Apakah karakter ini memiliki tatto?", "tatto"),
    ("Apakah karakter ini pernah juara satu di sekolah?", "juarasatu"),
    ("Apakah karakter ini memiliki lebih dari 2 anak?", "lebihduaanak"),
    ("Apakah karakter ini sering memakai kacamata", "kacamata"),
    ("Apakah karakter ini mengalami cedera pada kaki?", "cederakaki")
    # ("Apakah karakter ini lucu?", "lucu"),
    # ("Apakah karakter ini suka/sering tidur?", "tidur"),
    # ("Apakah karakter ini suka makan sayur?", "suka_sayur"),
    # ("Apakah karakter ini memiliki hewan peliharaan?", "peliharaan")
]

random.shuffle(main_questions)
random.shuffle(supporting_questions)

current_question_index = 0
is_main_questions_done = False
possible_characters = characters.copy()
asked_questions = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_question_index
    global is_main_questions_done
    global possible_characters
    global asked_questions

    if request.method == 'POST':
        answer = request.form['answer']
        if not is_main_questions_done:
            question, attribute = main_questions[asked_questions[-1]]
        else:
            question, attribute = supporting_questions[asked_questions[-1] - len(main_questions)]

        if answer == 'iya':
            possible_characters = [char for char in possible_characters if attribute in char.attributes]
        elif answer == 'tidak':
            possible_characters = [char for char in possible_characters if attribute not in char.attributes]

        current_question_index += 1

        if current_question_index == len(main_questions):
            is_main_questions_done = True
            current_question_index = 0
            asked_questions = []

        if (is_main_questions_done and current_question_index == len(supporting_questions)) or len(possible_characters) == 1:
            character_name = possible_characters[0].name if possible_characters else "Tidak tau"
            return redirect(url_for('result', character_name=character_name))

    while True:
        next_question_index = random.randint(0, len(main_questions) - 1) if not is_main_questions_done else random.randint(0, len(supporting_questions) - 1)
        if next_question_index not in asked_questions:
            asked_questions.append(next_question_index)
            break

    if not is_main_questions_done:
        question, _ = main_questions[next_question_index]
    else:
        question, _ = supporting_questions[next_question_index]

    return render_template('index.html', question=question)

@app.route('/result/<character_name>')
def result(character_name):
    character = next((char for char in characters if char.name == character_name), None)
    if character:
        return render_template('result.html', character_name=character.name, character_image=character.image)
    else:
        return render_template('result.html', character_name="Tidak tau", character_image=None)

@app.route('/reset')
def reset():
    global current_question_index
    global is_main_questions_done
    global possible_characters
    global asked_questions

    current_question_index = 0
    is_main_questions_done = False
    possible_characters = characters.copy()
    asked_questions = []

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)