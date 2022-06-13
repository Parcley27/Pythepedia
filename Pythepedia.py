import tkinter as tk
import time

topics_list = open('Topics.txt', 'a')
read_topics_list = open('Topics.txt', 'r')
past_searches = open('Past Searches.txt', 'a')

#app colours
#title 'royalblue4'
#bg 'gray99'
#fg/text 'black'
#buttons/text fields 'gray95'

#clear files ⬇
#topics_list.truncate(0)
#past_searches.truncate(0)

#stage options
#search box, not found, found, item list

window = tk.Tk()
window.configure(bg = 'gray99')
window.title('Pythepedia')
window.iconbitmap('icon.ico')

global search_term
global topic_found
global search_topic2
global term_number

term_number = 0

global stage
stage = 'search box'

def cont_btn(event):
  global search_term
  global stage

  past_searches = open('Past Searches.txt', 'a')
  
  if stage == 'search box':
    search_term = search_topic.get()
    search_term.lstrip()
    search_term.strip()
    search_term.rstrip()
    
    print(search_term)
    print('Search Term Logged')
    
    past_searches.write(search_term)
    past_searches.write('\n')
    past_searches.close()

    for widget in window.winfo_children():
      widget.destroy()
  
    search_engine()

    stage = 'display results'

  if stage == 'not found':
    print('it works')
    
    for widget in window.winfo_children():
      widget.destroy()
      
    new_search_term()
    stage = 'search box'

def list_btn(event):
  global stage
  
  for widget in window.winfo_children():
    widget.destroy()
    
  new_search_term()
  stage = 'search box'

def new_btn(event):
  global stage

  for widget in window.winfo_children():
    widget.destroy()

  new_search_term()
  stage = 'search box'

def init_search_bar(event):
  print(event.char)

def search_engine():
  global stage
  global search_term
  global topic_found

  read_topics_list = open('C:/Users/poxley/Documents/Python/Pythepedia/Topics.txt', 'r')

  search_term.lstrip()
  search_term.lstrip()
  search_term.strip()
  search_term.rstrip()
  
  topic_to_find = search_term.lower()

  lines = []
  with read_topics_list as file:
    lines = [line.rstrip() for line in file]

  print(lines)
  topic_found = (topic_to_find in lines)
  
      
  topics_list.close()
  
  if topic_found:
    
    #TO DO NEXT

    stage = 'found'
    
    top_buffer = tk.Label(width = 1, bg = 'gray99')
    top_buffer.pack()
    
    title_display = tk.Label(text = 'PYTHEPDEIA\n~~~~~~~~~~', bg = 'gray99', fg = 'royalblue4')
    title_display.pack()

    title_buffer = tk.Label(width = 50, bg = 'gray99')
    title_buffer.pack()

    buffer = tk.Label(width = 50, bg = 'grey99')
    
    topic_found_notice = tk.Label(text = 'Topic Found', bg = 'gray99', fg = 'black')
    topic_found_notice.pack()

    display_term = search_term.rstrip()
    display_term = display_term.capitalize()

    display_search_term = tk.Label(text = '"' + search_term.capitalize() + '"', bg = 'gray99')
    display_search_term.pack()

    buffer.pack()

    topic = search_term  + '.txt'
    topic_file = open(topic, 'r')
    lines = topic_file.readlines()

    for i in range(len(lines)):
      line_content = lines[i]
      line = tk.Label(text = line_content, bg = 'gray99')
      line.pack()
    file.close()

    bottom_buffer = tk.Label(width = 1, bg = 'gray99')
    bottom_buffer.pack()

    new_search_button = tk.Button(text = 'Search Again', width = 16, height = 2, bg = 'gray95', fg = 'black')
    new_search_button.pack()
    new_search_button.bind('<Button-1>', new_btn)

    bottom_buffer.pack()

    

  if not topic_found:
    stage = 'not found'
    
    for widget in window.winfo_children():
      widget.destroy()
    
    top_buffer = tk.Label(width = 1, bg = 'gray99')
    top_buffer.pack()
    
    title_display = tk.Label(text = 'PYTHEPDEIA\n~~~~~~~~~~', bg = 'gray99', fg = 'royalblue4')
    title_display.pack()

    title_buffer = tk.Label(width = 50, bg = 'gray99')
    title_buffer.pack()

    display_search_term = tk.Label(text = '"' + search_term.rstrip() + '" was not found', bg = 'gray99')
    display_search_term.pack()

    button_buffer = tk.Label(width = 1, bg = 'gray99')
    button_buffer.pack()

    list_button = tk.Button(text = 'View Item List', width = 16, height = 2, bg = 'gray95', fg = 'black')
    list_button.pack()
    list_button.bind('<Button-1>', list_btn)

    bottom_buffer = tk.Label(width = 1, bg = 'gray99')
    bottom_buffer.pack()
    
def new_search_term():
  
  global search_term
  global search_topic
  global term_number
  global stage

  stage == 'search box'

  term_number = term_number + 1

  if term_number == 1:
    top_buffer = tk.Label(bg = 'gray99', width = 1)
    top_buffer.pack()

    title_display = tk.Label(text = 'PYTHEPDEIA\n~~~~~~~~~~' , bg = 'gray99', fg = 'royalblue4') 
    title_display.pack()

    search_prompt = tk.Label(text = 'Please enter a search term:', bg = 'gray99',  fg = 'black', width = 50, height = 3)
    search_prompt.pack()

    search_topic = tk.Entry(bg = 'gray95', width = 50, justify = 'center')
    search_topic.pack()
    search_topic.bind('<Key>', init_search_bar)

    search_bar_buffer = tk.Label(bg = 'gray99', width = 1)
    search_bar_buffer.pack()

    continue_button = tk.Button(text = 'Continue', width = 16, height = 2, bg = 'gray95', fg = 'black')
    continue_button.pack()
    continue_button.bind('<Button-1>', cont_btn)

    credit_buffer = tk.Label(bg = 'gray99', width = 1)
    credit_buffer.pack()

    credit = tk.Label(text = 'Created by Parcley27, on Python 3.10.2', bg = 'gray99', fg = 'royalblue4')
    credit.pack()

    bottom_buffer = tk.Label(bg = 'gray99', width = 1)
    bottom_buffer.pack()

  else:
    read_topics_list = open('Topics with caps.txt', 'r')
    lines = read_topics_list.readlines()

    slot_content = ''

    top_buffer = tk.Label(width = 1, bg = 'gray99')
    top_buffer.pack()
  
    title_display = tk.Label(text = 'PYTHEPDEIA\n~~~~~~~~~~', bg = 'gray99', fg = 'royalblue4')
    title_display.pack()

    search_prompt = tk.Label(text = 'Please enter an accepted search term:', bg = 'gray99',  fg = 'black', width = 50, height = 3)
    search_prompt.pack()

    search_topic = tk.Entry(bg = 'gray95', width = 50, justify = 'center')
    search_topic.pack()
    search_topic.bind('<Key>', init_search_bar)

    search_bar_buffer = tk.Label(bg = 'gray99', width = 1)
    search_bar_buffer.pack()

    continue_button = tk.Button(text = 'Continue', width = 16, height = 2, bg = 'gray95', fg = 'black')
    continue_button.pack()
    continue_button.bind('<Button-1>', cont_btn)

    button_buffer = tk.Label(bg = 'gray99', width = 1)
    button_buffer.pack()

    list_title = tk.Label(text = 'Topics List:', bg = 'gray99')

    for i in range(len(lines)):
      slot_content = lines[i]
      slot = tk.Label(text = slot_content, width = 20, height = 2, bg = 'gray99', fg = 'black')
      slot.pack()    
    topics_list.close()

new_search_term()
