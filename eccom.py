# -*- coding: utf8 -*-
import telebot
bot = telebot.TeleBot('1444319453:AAEDHxwmiUnPVPIry9nd1SQtqbOjlDQP_f8')



@bot.message_handler(commands=['start'])
def welcome(message):
     bot.send_message(message.chat.id, "Привет, дружок. Тут ты найдешь ответь на экз по экономике.\nПросто введи номер вопросы. \nВот список вопросов: \n 1.Представление об экономике до меркантилизма \n 2.Первые научные представления об экономике (меркантилизм, физиократы, классики, марксизм) \n 3.Современные направления в экономической науке. \n 4.Предмет, структура и функции экономической теории	\n 5.Экономические законы и категории.")
     bot.send_message(message.chat.id, "\n 6.Методы изучения экономической жизни.\n 7.Общественное производство и его стадии \n 8.Потребности и блага \n 9.Ресурсы и проблема выбора\n 10.Факторы производства\n 11.Эффективность производства: понятие и показатели.\n 12.Собственность как экономическая категория. \n 13.Место собственности в экономической системе.")




@bot.message_handler(content_types=['text'])
def otvet(message):
        if message.chat.type == "private":
            if message.text.lower()=="1":
                doc = open('1.txt', 'rb')
                bot.send_document(message.chat.id,doc)

            elif message.text=="2":
                doc = open('2.txt', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text=="3":
                doc = open('3.txt', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text=="4":
                doc = open('4.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text=="5":
                 doc = open('5.txt', 'rb')
                 bot.send_document(message.chat.id,doc)
            elif message.text.lower()=="6":
                 doc = open('6.pdf', 'rb')
                 bot.send_document(message.chat.id,doc)
            elif message.text.lower()=="7":
                doc = open('7.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text.lower()=="8":
                doc = open('8.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text.lower()=="9":
                doc = open('9.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text=="10":
                doc = open('10.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text=="11":
                doc = open('11.pdf', 'rb')
                bot.send_document(message.chat.id,doc)    
            elif message.text=="12":
                doc = open('12.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text=="13":
                doc = open('13.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text=="14":
                doc = open('14.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text=="15":
                doc = open('15.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text=="16":
                doc = open('16.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
            elif message.text=="17":
                doc = open('17.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
            
            
            
            
            
                
            
         
   
            else:
                bot.send_message(message.chat.id,"poka net")
 



 





bot.polling(none_stop=True)
