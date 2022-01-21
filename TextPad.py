import tkinter as tk 
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
from datetime import datetime
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate 
import speech_recognition as sr
from emoji import emojize
import os 

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Text Pad')
main_application.wm_iconbitmap('icon.ico')


############################################  main menu  ################################################

main_menu = tk.Menu()
#file icons
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png') 

file = tk.Menu(main_menu, tearoff=False)



#####edit 
#edit icons 
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_menu, tearoff=False)


######## view icons 
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')
view = tk.Menu(main_menu, tearoff=False)


######## color theme 
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')
color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)


#font_color, bg_color
color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}

######## emoji
Face_with_Tears_of_Joy_icon = tk.PhotoImage(file="icons2/Face_With_Tears_Of_Joy.png")
Rolling_On_The_Floor_Laughing_icon = tk.PhotoImage(file="icons2/Rolling_On_The_Floor_laughing.png")
loudly_crying_face = tk.PhotoImage(file="icons2/loudly_crying_face.png")
pleading_face = tk.PhotoImage(file="icons2/pleading_face.png")
Face_With_Hand_Over_Mouth = tk.PhotoImage(file="icons2/Face_With_Hand_Over_Mouth.png")
Folded_Hands = tk.PhotoImage(file="icons2/Folded_Hands.png")
Face_With_Tongue = tk.PhotoImage(file="icons2/Face_With_Tongue.png")
Beaming_Face_With_Smiling_Eyes = tk.PhotoImage(file="icons2/Beaming_Face_With_Smiling_Eyes.png")
Thumbs_Up = tk.PhotoImage(file="icons2/Thumbs_Up.png")
Face_Blowing_A_Kiss = tk.PhotoImage(file="icons2/Face_Blowing_A_Kiss.png")

emoji = tk.Menu(main_menu, tearoff=False)

emoji_choice = tk.StringVar()
emoji_icons = (Face_with_Tears_of_Joy_icon, Rolling_On_The_Floor_Laughing_icon, loudly_crying_face, pleading_face, Face_With_Hand_Over_Mouth, Folded_Hands, Face_With_Tongue, Beaming_Face_With_Smiling_Eyes, Thumbs_Up, Face_Blowing_A_Kiss)

emoji_dict = {
    "😂" : "\U0001F602",
    "🤣" : "\U0001F923",
    "😭" : "\U0001F62D",
    "🥺" : "\U0001F97A",
    "🤭" : "\U0001F92D",
    "🙏" : "\U0001F64F",
    "😛" : "\U0001F61B",
    "😊" : "\U0001F60A",
    "👍" : "\U0001F44D",
    "😘" : "\U0001F618",
}

# Tools
tools = tk.Menu(main_menu, tearoff=False)

# cascade 
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)
main_menu.add_cascade(label='Emoji', menu=emoji)
main_menu.add_cascade(label='Tools', menu=tools)

# -------------------------------------&&&&&&&& End main menu &&&&&&&&&&& ----------------------------------
##########################################  toolbar  ################################################


tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)                                                         

## font box

# syntax for using all font styles (by default type is tuple)
font_tuple = tk.font.families()                                                               

# variable to store user selected font styles
font_family = tk.StringVar()                                                                  
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')

# only displaying the name of the font styles
font_box['values'] = font_tuple                                                               

# by default font used
font_box.current(font_tuple.index('Arial'))                                                   
font_box.grid(row=0, column=0, padx=5)


## size box 

# variable to store user selected font size
size_var = tk.IntVar()                                                                        
font_size = ttk.Combobox(tool_bar, width=14, textvariable = size_var, state='readonly')
font_size['values'] = tuple(range(8,82,2))                                                      
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

## highlight button
highlight_btn = tk.Button(tool_bar,text='HIGHLIGHT',fg='blue')
highlight_btn.grid(row=0,column=2,padx=5)

## clear button
clear_btn = tk.Button(tool_bar,text='CLEAR',fg='blue')
clear_btn.grid(row=0,column=3,padx=3)

## bold button 
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=5, padx=5)

## italic button 
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=6, padx=5)

## underline button 
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0, column=7, padx=5)

## font color button 
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=8,padx=5)

## align left 
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=9, padx=5)

## align center 
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=10, padx=5)

## align right 
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=11, padx=5)

# -------------------------------------&&&&&&&& End toolbar  &&&&&&&&----------------------------------

##########################################text editor ##############################################

text_editor = tk.Text(main_application)                                              
text_editor.config(wrap='word', relief=tk.FLAT)

def current_datetime():
    now = datetime.now()
    text_editor.insert(tk.INSERT, now.strftime("%a  %d/%m/%Y   %H:%M:%S"))
    text_editor.insert(tk.INSERT, '\n \n')
current_datetime()

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality 
current_font_family = 'Arial'
current_font_size = 12

def change_font(event=None):
    global current_font_family
    # changing default font style to user selected font style  
    current_font_family = font_family.get()                                          
    text_editor.configure(font=(current_font_family, current_font_size))
    
def change_fontsize(event=None):
    global current_font_size
    # changing default font size to user selected font size
    current_font_size = size_var.get()                                              
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

######## buttons functionality 

# Highlight button functionality
def highlight():
    #configuring a tag called start 
    text_editor.tag_configure("start", background="black", foreground="yellow")
    
    # if no text is selected then tk.TclError exception occurs 
    try:
        text_editor.tag_add("start", "sel.first", "sel.last")         
    except tk.TclError: 
        pass

highlight_btn.configure(command=highlight)

# Clear Button functionailty
def clear():
    # if no text is selected then tk.TclError exception occurs
    try:
        text_editor.tag_remove("start","sel.first","sel.last")
    except tk.TclError:
        pass

clear_btn.configure(command=clear)


# bold button functionality
def change_bold():
    bold_font = tk.font.Font(text_editor, text_editor.cget('font'))
    bold_font.configure(weight = 'bold')
    
    # using tags to change the weight of selected text
    text_editor.tag_configure('bold',font = bold_font)                             

    # if no text is selected then tk.TclError exception occurs
    try:
        current_tags = text_editor.tag_names('sel.first')
        if 'bold' in current_tags:
            text_editor.tag_remove('bold','sel.first','sel.last')
        else:
            text_editor.tag_add('bold','sel.first','sel.last')
    except tk.TclError:
        pass
    
bold_btn.configure(command=change_bold)


# italic functionlaity
def change_italic():
    italic_font = tk.font.Font(text_editor, text_editor.cget('font'))
    italic_font.configure(slant = 'italic')
    
    # using tags to italic the selected text
    text_editor.tag_configure('italic',font = italic_font)                        

    # if no text is selected then tk.TclError exception occurs
    try:
        current_tags = text_editor.tag_names('sel.first')
        if 'italic' in current_tags:
            text_editor.tag_remove('italic','sel.first','sel.last')
        else:
            text_editor.tag_add('italic','sel.first','sel.last')
    except tk.TclError:
        pass

italic_btn.configure(command=change_italic)

# underline functionality 
def change_underline():
    underline_font = tk.font.Font(text_editor, text_editor.cget('font'))
    
    # in font class underline has value 1(True) or 0(False)
    underline_font.configure(underline = 1)           
    
    # using tags to underline the selected text                   
    text_editor.tag_configure(1,font = underline_font)

    # if no text is selected then tk.TclError exception occurs
    try:
        current_tags = text_editor.tag_names('sel.first')
        if 1 in current_tags:
            text_editor.tag_remove(1,'sel.first','sel.last')
        else:
            text_editor.tag_add(1,'sel.first','sel.last')
    except tk.TclError:
        pass

underline_btn.configure(command=change_underline)


## font color functionality 
def change_font_color():
    # colorchooser module has method name 
    # askcolor which makes the color window
    color_var = tk.colorchooser.askcolor()                  
    if color_var:
        color_font = tk.font.Font(text_editor, text_editor.cget('font'))
        # color_var = ((R,G,B),hexavalue) - for foreground
        text_editor.tag_configure('color',font = color_font, foreground = color_var[1])                                     

        try:
            current_tags = text_editor.tag_names('sel.first')
            if 'color' in current_tags:
                text_editor.tag_remove('color','sel.first','sel.last')
            else:
                text_editor.tag_add('color','sel.first','sel.last')
        except tk.TclError:
            pass

font_color_btn.configure(command=change_font_color)

### align functionality 

def align_left():
    text_content = tk.font.Font(text_editor, text_editor.cget('font'))
    text_editor.tag_config('left', justify=tk.LEFT)
    try:
        current_tags = text_editor.tag_names('sel.first')
        if 'left' not in current_tags:
            text_editor.tag_add('left','sel.first','sel.last')
        else:
            text_editor.tag_remove('left','sel.first','sel.last')
    except tk.TclError:
        pass

align_left_btn.configure(command=align_left)

## center 
def align_center():
    text_content = tk.font.Font(text_editor, text_editor.cget('font'))
    text_editor.tag_config('center', justify=tk.CENTER)
    try:
        current_tags = text_editor.tag_names('sel.first')
        if 'center' not in current_tags:
            text_editor.tag_add('center','sel.first','sel.last')
        else:
            text_editor.tag_remove('center','sel.first','sel.last')
    except tk.TclError: 
        pass

align_center_btn.configure(command=align_center)

## right 
def align_right():
    text_content = tk.font.Font(text_editor, text_editor.cget('font'))
    text_editor.tag_config('right', justify=tk.RIGHT)
    try:
        current_tags = text_editor.tag_names('sel.first')
        if 'right' not in current_tags:
            text_editor.tag_add('right','sel.first','sel.last')
        else:
            text_editor.tag_remove('right','sel.first','sel.last')
    except tk.TclError:
        pass

align_right_btn.configure(command=align_right)


text_editor.configure(font=('Arial', 12))
# -------------------------------------&&&&&&&& End text editor &&&&&&&&&&& ----------------------------------


##############################################statusbar###################################################

status_bar = ttk.Label(main_application, text = 'Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False 
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True 
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)


# -------------------------------------&&&&&Endstatusbar&&&&& --------------------------------------------


############################### main menu functinality #####################################

## variable 
url = ''

## new functionality
def new_file(event=None):
    global url 
    url = ''
    text_editor.delete(1.0, tk.END)
    current_datetime()

## file commands 
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)

## Types of messagebox: showinfo,showwarning,showerror,askquestion,askokcancel,askyesno 
## open functionality

def open_file(event=None):
    global url 
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            current_datetime()
            text_editor.insert(tk.INSERT, '\n \n')
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    main_application.title(os.path.basename(url))

file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)

## save file 

def save_file(event=None):
    global url 
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return 

file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command = save_file)


## save as functionality 
def save_as(event=None):
    global url 
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return 


file.add_command(label='Save As', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_as)

## exit functionality 

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return 
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)


############ find functionality

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

## edit commands 
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X', command= lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command = find_func)

## view check button 

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False 
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True 

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False 
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True 


view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0,variable = show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)


## color theme 
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(bg=bg_color, fg=fg_color) 
count = 0
# to iterate items of color_icons variable                                                                  
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1 

## emoji 
def add_emoji():
    chosen_emoji = emoji_choice.get()
    emoji_tuple = emoji_dict.get(chosen_emoji)
    emoji_value = emoji_tuple[0]
    text_editor.insert(tk.INSERT, (emoji_value))
count = 0
for i in emoji_dict:
    emoji.add_radiobutton(label = i, image=emoji_icons[count], variable = emoji_choice, compound=tk.LEFT, command=add_emoji)
    count += 1


##speech to text
def speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source=source,timeout=10)
        try:
            text = r.recognize_google(audio)
            result = '{}'.format(text)
            text_editor.insert(tk.INSERT, result)
        except sr.RequestError as e:
            messagebox.showerror('Network Error','Make sure your computer has an active Internet connection')
        except:
            messagebox.showinfo('Recognition Problem','Sorry could not recognize')

tools.add_command(label='Speech to Text', command=speech_recognition)

## Language converter
def english_to_hindi():
    def clearAll() : 
        # whole content of text area  is deleted  
        text1_field.delete('1.0', 'end') 
        text2_field.delete('1.0', 'end')
    def convert():
        # get a whole input content from text box 
        # ignoring \n from the text box content 
        input_text = text1_field.get("1.0", "end")[:-1] 
        output_text = transliterate(input_text, sanscript.ITRANS,sanscript.DEVANAGARI) 
        
        text2_field.insert('end -1 chars', output_text) 
    
    
    # Driver code  
    if __name__ == "__main__" :
        root = tk.Tk()  
        root.configure(background = 'black')  
        root.geometry("400x350")  
        root.title("Converter")  

        label1 = tk.Label(root, text = " English Text ",fg = 'yellow',bg = 'black')  
        label2 = tk.Label(root, text = " Hindi Text",fg = 'yellow',bg = 'black')  
        label1.grid(row = 1, column = 0, padx = 10, pady = 10)   
        label2.grid(row = 3, column = 0, padx = 10, pady = 10) 
           
        text1_field = tk.Text(root, height = 5, width = 25, font = "lucida 13")  
        text2_field = tk.Text(root, height = 5, width = 25, font = "lucida 13")   
        text1_field.grid(row = 1, column = 1, padx = 10, pady = 10)   
        text2_field.grid(row = 3, column = 1, padx = 10, pady = 10)  
      
        button1 = tk.Button(root, text = "Convert into Hindi text",bg = "red", fg = "black", command = convert)          
        button1.grid(row = 2, column = 1)  
        button2 = tk.Button(root, text = "Clear", bg = "red", fg = "black", command = clearAll) 
        button2.grid(row = 4, column = 1)  
           
        root.mainloop()   

tools.add_command(label='English to Hindi', command=english_to_hindi)

# -------------------------------------&&&&&&&& End main menu  functinality&&&&&&&&&&& ----------------------------------

main_application.config(menu=main_menu)

#### bind shortcut keys 
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)

main_application.mainloop()
