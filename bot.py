import telebot
import asyncio
import os
from telebot.types import InputMediaPhoto
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import time
TOKEN = "8778713544:AAEqhHMUzZUrQ2uPPQeXIFNwbcTEcvRUOow"

bot = telebot.TeleBot(TOKEN)

# -----------------------
# القائمة الرئيسية
# -----------------------
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📘 الدروس", "📝 التمارين مع الحل")
    markup.add("📂 مواضيع BAC", "📊 المراجعة النهائية")
    markup.add("ℹ️ مساعدة")
    return markup


# -----------------------
# قائمة الدروس
# -----------------------
def lessons_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📈 الدوال", "🔢 المتتاليات")
    markup.add("🎲 الاحتمالات", "➗ القسمة في Z")
    markup.add("🧮 الأعداد المركبة")
    markup.add("⬅️ رجوع")
    return markup


# -----------------------
# قائمة الدوال
# -----------------------
def functions_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("الدالة الأسية", "الدالة اللوغاريتمية")
    markup.add("دراسة الدوال")
    markup.add("⬅️ رجوع")
    return markup


# -----------------------
# قائمة التمارين
# -----------------------
def exercises_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("تمارين الدوال", "تمارين المتتاليات")
    markup.add("تمارين الاحتمالات")
    markup.add("تمارين الأعداد المركبة")
    markup.add("⬅️ رجوع")
    return markup


# -----------------------
# START
# -----------------------
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 مرحبا بك في بوت الرياضيات\nاختر من القائمة:",
        reply_markup=main_menu()
    )


# -----------------------
# الدروس
# -----------------------
@bot.message_handler(func=lambda message: message.text == "📘 الدروس")
def lessons(message):
    bot.send_message(
        message.chat.id,
        "اختر محور الدروس:",
        reply_markup=lessons_menu()
    )


# -----------------------
# الدوال
# -----------------------
@bot.message_handler(func=lambda message: message.text == "📈 الدوال")
def functions(message):
    bot.send_message(
        message.chat.id,
        "محور الدوال:",
        reply_markup=functions_menu()
    )


# -----------------------
# دروس الدوال
# -----------------------
@bot.message_handler(func=lambda message: message.text == "الدالة الأسية")
def exp_lesson(message):
    bot.send_message(message.chat.id, "ملخص الدالة الأسية قريبًا 📄")


@bot.message_handler(func=lambda message: message.text == "الدالة اللوغاريتمية")
def log_lesson(message):
    bot.send_message(message.chat.id, "ملخص الدالة اللوغاريتمية قريبًا 📄")


@bot.message_handler(func=lambda message: message.text == "دراسة الدوال")
def study_functions(message):
    bot.send_message(message.chat.id, "شرح دراسة الدوال قريبًا 📄")


# -----------------------
# التمارين
# -----------------------
@bot.message_handler(func=lambda message: message.text == "📝 التمارين مع الحل")
def exercises(message):
    bot.send_message(
        message.chat.id,
        "اختر نوع التمارين:",
        reply_markup=exercises_menu()
    )


@bot.message_handler(func=lambda message: message.text == "تمارين الدوال")
def ex_functions(message):
    bot.send_message(message.chat.id, "تمارين الدوال مع الحل قريبًا ✏️")


@bot.message_handler(func=lambda message: message.text == "تمارين المتتاليات")
def ex_sequences(message):
    bot.send_message(message.chat.id, "تمارين المتتاليات مع الحل قريبًا ✏️")


# 2️⃣ زر تمارين الاحتمالات
@bot.message_handler(func=lambda message: message.text == "تمارين الاحتمالات")
def ex_prob(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)  # 4 أزرار في كل صف

    buttons = [KeyboardButton(f"تمرين {i}") for i in range(1, 29)]
    markup.add(*buttons)
    markup.add("⬅️ رجوع")
    bot.send_message(
        message.chat.id,
        "اختر التمرين الذي تريد حله:",
        reply_markup=markup
    )

# @bot.message_handler(func=lambda message: message.text.startswith("تمرين"))
# def send_exercise(message):

#     num = message.text.split()[1]
#     folder = f"probabilité/exercices/ex{num}"

#     try:
#         files = os.listdir(folder)

#         media = []
#         for file in sorted(files):
#             path = os.path.join(folder, file)
#             media.append(InputMediaPhoto(open(path, "rb")))

#         bot.send_media_group(message.chat.id, media)

#     except:
#         bot.send_message(message.chat.id, "هذا التمرين غير متوفر بعد.")

@bot.message_handler(func=lambda message: message.text.startswith("تمرين"))
def send_exercise(message):

    num = message.text.split()[1]
    file_path = f"probabilité/exercices/ex{num}.pdf"

    try:
        with open(file_path, "rb") as pdf:
            bot.send_document(
                message.chat.id,
                pdf,
                caption="🚫 هذا المحتوى محمي من التحميل والتوجيه",
                protect_content=True
            )

    except:
        bot.send_message(message.chat.id, "هذا التمرين غير متوفر بعد.")

@bot.message_handler(func=lambda message: message.text == "تمارين الأعداد المركبة")
def ex_complex(message):
    bot.send_message(message.chat.id, "تمارين الأعداد المركبة قريبًا ✏️")


# -----------------------
# BAC
# -----------------------
@bot.message_handler(func=lambda message: message.text == "📂 مواضيع BAC")
def bac(message):
    bot.send_message(message.chat.id, "مواضيع BAC مع الحلول قريبًا 📚")


# -----------------------
# مراجعة نهائية
# -----------------------
@bot.message_handler(func=lambda message: message.text == "📊 المراجعة النهائية")
def revision(message):
    bot.send_message(message.chat.id, "ملخص شامل لجميع المحاور قريبًا 📊")


# -----------------------
# مساعدة
# -----------------------
@bot.message_handler(func=lambda message: message.text == "ℹ️ مساعدة")
def help_menu(message):
    bot.send_message(
        message.chat.id,
        "استخدم الأزرار للتنقل بين الدروس والتمارين.\nاكتب /start لإظهار القائمة."
    )


# -----------------------
# رجوع
# -----------------------
@bot.message_handler(func=lambda message: message.text == "⬅️ رجوع")
def back(message):
    bot.send_message(
        message.chat.id,
        "القائمة الرئيسية:",
        reply_markup=main_menu()
    )




# -----------------------
# درس الاحتمالات
# -----------------------
# @bot.message_handler(func=lambda message: message.text == "🎲 الاحتمالات")
# def probabilities_lesson(message):
#     bot.send_message(message.chat.id, "إليك ملف درس الاحتمالات 📄")
#     with open("probabilité/resume_probabilité.pdf", "rb") as pdf:
#         bot.send_document(message.chat.id, pdf,"هذا المحتوى محمي من التحميل والتوجيه 🚫",True)
@bot.message_handler(func=lambda message: message.text == "🎲 الاحتمالات")
def probabilities_lesson(message):
    bot.send_message(message.chat.id, "إليك ملف درس الاحتمالات 📄")

    with open("probabilité/resume_probabilité.pdf", "rb") as pdf:
        bot.send_document(
            message.chat.id,
            pdf,
            caption="هذا المحتوى محمي من التحميل والتوجيه 🚫",
            protect_content=True
        )

# تشغيل البوت
print("Bot is running...")
bot.infinity_polling()


# while True:
#     try:
#         print("Bot is running...")
#         bot.infinity_polling(timeout=60, long_polling_timeout=60)
#     except Exception as e:
#         print("Error:", e)
#         time.sleep(10)


# bot.remove_webhook()
# bot.infinity_polling()
