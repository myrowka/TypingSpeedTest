from tkinter import *


TIMER = 60
story_text = """
This Short Story The Golden Egg is quite interesting to all the people. Enjoy reading this story. Haria, a poor barber
 lived alone in his small hut. He was dedicated to his work. And whatever he earns was enough to fulfill his needs. 
 One evening, after returning from work, Haria was hungry. “What shall I cook tonight?" he thought. Just then he heard 
 a hen clucking outside his hut. “That hen would make a great feast for me," thought Haria and prepared to catch the 
 hen. With a little effort he was able to catch the hen. As he was about to kill the hen, it squeaked, “Please do not 
 kill me, O kind man! I will help you." Haria stopped. Though he was surprised that the hen spoke, he asked, “How can 
 you help me?"“If you spare my life, I will lay a golden egg everyday for you," said the hen. Haria’s eyes got widened 
 in delight. Haria was surprised to hear this promise. “A golden egg! That too everyday! But why should I believe you?
 You might be lying," said Haria. “If I do not lay a golden egg tomorrow, you can kill me," said the hen. After this 
 promise, Haria spared the hen and waited for the next day.The next morning, Haria found a golden egg lying outside his
 hut and the hen sitting beside it. “It is true! You really can lay a golden egg!" exclaimed Haria with great delight.
He did not reveal this incident to any one, fearing that others would catch the hen.
"""

window = Tk()
window.title('Typing speed test')

title_label = Label(text='Try to type as much word from the text below as you can. Only words with more than one'
                         ' char count. Press start to see the text and begin.', fg='red')
title_label.grid(column=0, row=0)

timer_label = Label(text=f'{TIMER} seconds left')
timer_label.grid(column=0, row=3)

text_field = Text(window, width=100, height=10, state='disabled', wrap=WORD)
text_field.grid(column=0, row=4)


def begin():
    text_label = Label(text=story_text, justify=LEFT)
    text_label.grid(column=0, row=1)

    title_label.grid_remove()

    begin_button.config(state=DISABLED)

    text_field.config(state=NORMAL)
    text_field.delete('1.0', END)
    start()


def start(counter=TIMER):

    timer_label.config(text=f'{counter} seconds left')
    if counter > 0:
        window.after(1000, start, counter - 1)
    else:
        text_field.config(state=DISABLED)
        result = 0
        words_text = story_text.split()

        typed = text_field.get("1.0", END)
        typed_words = typed.split()
        for word in typed_words:
            if word.isalpha() and len(word) > 1 and word in words_text:
                result += 1
                words_text.remove(word)
        timer_label.config(text=f'Your result is: {result} words', fg='red')
        begin_button.config(state=ACTIVE)


begin_button = Button(text='Start', width=20, command=begin)
begin_button.grid(column=0, row=2)

window.mainloop()
