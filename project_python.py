import tkinter as tk
from tkinter import PhotoImage    
from tkinter import scrolledtext
from tkinter import ttk
import subprocess
root=tk.Tk()
root.title("Python'It")
root.geometry("800x800")


mainframe=tk.Frame(root)
mainframe.grid(row=0,column=0,sticky="nsew")
#images
mainimage= PhotoImage(file="pixelcut-export.png")
lessonimage= PhotoImage(file="pixelcut-export.png")






#functions
def exitbutton():
    root.destroy()
def start_button():
    mainframe.grid_forget()
    lesson_frame=tk.Frame(root)
    lesson_frame.grid(row=0,column=0,sticky="nsew")
    for i in range(10):
        lesson_frame.grid_columnconfigure(i, weight=1)
        lesson_frame.grid_rowconfigure(i, weight=1)
    lesson_label = tk.Label(lesson_frame, image=lessonimage)
    lesson_label.place(x=0, y=0, relwidth=1, relheight=1)
    def undostart_button():
        lesson_frame.grid_forget()
        mainframe.grid(row=0,column=0,sticky="nsew")
    def create_topic_frame(file_path, l_image):
        global completed_topics  # Use the global variable to track completed topics
        completed_topics += 1 
        lesson_frame.grid_forget()
        t2frame = tk.Frame(root)
        t2frame.grid(row=0, column=0, columnspan=10, rowspan=10, sticky="nsew")
        for i in range(10):
            t2frame.grid_columnconfigure(i, weight=1)
            t2frame.grid_rowconfigure(i, weight=1)
        
        canvas = tk.Canvas(t2frame)
        canvas.place(x=0, y=0, relwidth=1, relheight=0.2)

        image = PhotoImage(file=l_image)
        canvas.create_image(-100, -50, anchor="nw", image=image)
        canvas.image = image

        # Function to save selected text to notebook
        def save_to_notebook():
            try:
                selected_text = t1text.get(tk.SEL_FIRST, tk.SEL_LAST)
                notebook_file_path = "Notebook_saved.txt"  # Change this path later
                with open(notebook_file_path, 'a', encoding='utf-8') as notebook_file:
                    notebook_file.write(selected_text + "\n")  # Add a newline for separation
                print("Text saved to notebook.")
            except tk.TclError:
                print("No text selected.")

        tsavefile = tk.Button(t2frame, text="Save To Notebook", width=17, height=2, command=save_to_notebook)
        tsavefile.grid(row=1, column=9)

        t1text = scrolledtext.ScrolledText(t2frame, wrap="word", font=("Helvetica", 12), bg="#daa373", fg="#333333", padx=10, pady=10, borderwidth=2, relief="solid")
        t1text.grid(row=4, rowspan=10, columnspan=10, sticky="nsew")

        tquizbutton = tk.Button(t2frame, text="Jump to Quiz", width=10, height=2, command=lambda: subprocess.Popen(["python", "quiz_main.py"]))
        tquizbutton.grid(row=2, column=9, padx=0)

        def back():
            t2frame.destroy()
            lesson_frame.grid(row=0, column=0, sticky="nsew")

        t1back = tk.Button(t2frame, text="Back", width=10, height=2, command=back)
        t1back.grid(row=2, column=1, padx=0)

        def fileread():
            with open(file_path, 'r', encoding='utf-8') as t2file:
                stuff2 = t2file.read()
                t1text.insert(tk.END, stuff2)
                t1text.config(state=tk.DISABLED)

        root.after(100, fileread)







        

    #  10 buttons for the topic wala

    left_button1 = tk.Button(lesson_frame, text="Topic 1", width=20, height=2,command=lambda: create_topic_frame( "t_1content.txt","1.png"))
    left_button1.grid(row=1, column=2,columnspan=2, padx=10, pady=0)

    left_button2 = tk.Button(lesson_frame, text="Topic 2", width=20, height=2,command=lambda: create_topic_frame("t2.txt","2.png"))
    left_button2.grid(row=2, column=2,columnspan=2, padx=10, pady=0)

    left_button3 = tk.Button(lesson_frame, text="Topic 3", width=20, height=2,command=lambda: create_topic_frame("t3.txt","3.png"))
    left_button3.grid(row=3, column=2,columnspan=2, padx=10, pady=6)

    left_button4 = tk.Button(lesson_frame, text="Topic 4", width=20, height=2,command=lambda: create_topic_frame("t4.txt","4.png"))
    left_button4.grid(row=4, column=2,columnspan=2, padx=10, pady=0)

    left_button5 = tk.Button(lesson_frame, text="Topic 5", width=20, height=2,command=lambda: create_topic_frame("t5.txt","5.png"))
    left_button5.grid(row=5, column=2,columnspan=2, padx=10, pady=0)

    right_button6 = tk.Button(lesson_frame, text="Topic 6", width=20, height=2,command=lambda: create_topic_frame("t6.txt","6.png" ))
    right_button6.grid(row=1, column=6,columnspan=2, padx=10, pady=0)

    right_button7 = tk.Button(lesson_frame, text="Topic 7", width=20, height=2,command=lambda: create_topic_frame("t7.txt", "7.png"))
    right_button7.grid(row=2, column=6, columnspan=2,padx=10, pady=0)

    right_button8 = tk.Button(lesson_frame, text="Topic 8", width=20, height=2,command=lambda: create_topic_frame("t8.txt", "8.png"))
    right_button8.grid(row=3, column=6,columnspan=2, padx=10, pady=0)

    right_button9 = tk.Button(lesson_frame, text="Topic 9", width=20, height=2,command=lambda: create_topic_frame("t9.txt", "9.png"))
    right_button9.grid(row=4, column=6,columnspan=2, padx=10, pady=0)

    right_button10 = tk.Button(lesson_frame, text="Topic 10", width=20, height=2,command=lambda: create_topic_frame("t3.txt","1.png"))
    right_button10.grid(row=5, column=6,columnspan=2, padx=10, pady=0)

    back_button = tk.Button(lesson_frame, text="Back to Main Menu", command=undostart_button, width=20, height=2)
    back_button.grid(row=6, column=4, columnspan=2, pady=20)

    label1 = tk.Label(lesson_frame, text="Lessons",font=("Arial",20)) 
    label1.grid(row=0, column=0, columnspan=10, sticky="new")




        

    
main_label = tk.Label(mainframe, image=mainimage)
main_label.place(x=0, y=0, relwidth=1, relheight=1)


def open_notebook_frame():
    # Create a new frame for the notebook
    notebook_frame = tk.Frame(root, bg="#7a9bae")
    notebook_frame.grid(row=0, column=0, sticky="nsew")
    
    for i in range(10):
        notebook_frame.grid_columnconfigure(i, weight=1)
        notebook_frame.grid_rowconfigure(i, weight=1)

    nlabel = tk.Label(notebook_frame, text="Notebook", bg="#96cbdc",font=("Arial",20))
    nlabel.grid(row=0, column=0, columnspan=10, sticky="nsew")

    # Create a ScrolledText widget to display the notebook contents
    notebook_text = scrolledtext.ScrolledText(notebook_frame, wrap="word", font=("Helvetica", 12), bg="#daa373", fg="#333333", padx=10, pady=10, borderwidth=2, relief="solid")
    notebook_text.grid(row=1, column=0, rowspan=10, columnspan=10, sticky="nsew")

    # Function to read the notebook file and display its contents
    def load_notebook():
        try:
            with open("Notebook_saved.txt", 'r', encoding='utf-8') as notebook_file:
                contents = notebook_file.read()
                notebook_text.delete(1.0, tk.END)  
                notebook_text.insert(tk.END, contents)
                notebook_text.config(state=tk.DISABLED)
        except FileNotFoundError:
            notebook_text.insert(tk.END, "Notebook file not found.")
            notebook_text.config(state=tk.DISABLED)

    # Load notebook contents when the frame is created
    root.after(100, load_notebook)

    def back_to_main():
        notebook_frame.destroy()  # Close the notebook frame and return to main
        mainframe.grid(row=0, column=0, sticky="nsew")

    nback = tk.Button(notebook_frame, text="Back", command=back_to_main, width=10, height=2)
    nback.grid(row=0, column=1, pady=10)

    # Function to clear the selected text from the notebook and update the file
    def clear_selected_text():
        try:
            # Get the selected text
            start_index = notebook_text.index(tk.SEL_FIRST)
            end_index = notebook_text.index(tk.SEL_LAST)
            selected_text = notebook_text.get(start_index, end_index)

            # Remove the selected text from the ScrolledText widget
            notebook_text.config(state=tk.NORMAL)  # Enable editing
            notebook_text.delete(start_index, end_index)  # Delete selected text
            notebook_text.config(state=tk.DISABLED)  # Make it read-only again

            # Read current contents from the file
            with open("Notebook_saved.txt", 'r', encoding='utf-8') as notebook_file:
                contents = notebook_file.read()

            # Remove the selected text from the contents
            updated_contents = contents.replace(selected_text, "", 1)  # Remove only the first occurrence

            # Save the updated contents back to the file
            with open("Notebook_saved.txt", 'w', encoding='utf-8') as notebook_file:
                notebook_file.write(updated_contents)

            print("Selected text cleared and notebook updated.")
            load_notebook()  # Reload the notebook contents to reflect changes

        except tk.TclError:
            print("No text selected to clear.")

    clear_button = tk.Button(notebook_frame, text="Clear", command=clear_selected_text, width=10, height=2)
    clear_button.grid(row=0, column=8, pady=10)  # Place the Clear button next to the Back button



#configuring the rows and column for work

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
for i in range(10):
    mainframe.grid_columnconfigure(i, weight=1)
    mainframe.grid_rowconfigure(i, weight=1)



#progress part

total_topics = 10
completed_topics = 0  # Increment this when a topic is completed
completed_quizzes = 0


def view_progress():
    
    progress_window = tk.Toplevel(root)
    progress_window.title("Progress Tracker")
    progress_window.geometry("400x200")
    
    total_progress = (completed_topics + completed_quizzes) / (total_topics + total_topics) * 100  # 100% for both topics and quizzes
    total_progress = min(total_progress, 100)  # Ensure it doesn't exceed 100%


    progress_label = tk.Label(progress_window, text=f"Progress: {total_progress:.2f}%", font=("Arial", 16))
    progress_label.grid(row=0, column=0, columnspan=2, pady=20)


    progress_bar = ttk.Progressbar(progress_window, length=300, mode='determinate')
    progress_bar.grid(row=1, column=0, columnspan=2, pady=20)
    progress_bar['value'] = total_progress  

 
    close_button = tk.Button(progress_window, text="Close", command=progress_window.destroy)
    close_button.grid(row=2, column=0, columnspan=2, pady=10)

    def update_progress():
        total_topics = 10
        total_progress = (completed_topics + completed_quizzes) / (total_topics + total_topics) * 100
        total_progress = min(total_progress, 100)  
        progress_bar['value'] = total_progress  

 
    update_progress()

#main frame work

mainlabel=tk.Label(mainframe,text="Python'It",font=("Arial",20))
mainlabel.grid(row=0,column=0,columnspan=10,sticky="new",)

startbutton= tk.Button(mainframe,text="Start Lesson",width=20,height=2,command=start_button)
startbutton.grid(row=3,column=4,columnspan=2,pady=5)

quizbutton=tk.Button(mainframe,text="Take Quiz",width=20,height=2,command=lambda : subprocess.Popen(["python","quiz_main.py"]))
quizbutton.grid(row=4,column=4,columnspan=2,pady=5)

progressbutton=tk.Button(mainframe,text="View Progress",width=20,height=2,command= view_progress)
progressbutton.grid(row=5,column=4,columnspan=2,pady=5)

notebookbutton=tk.Button(mainframe,text="Open Notebook",width=20,height=2,command=open_notebook_frame)
notebookbutton.grid(row=6,column=4,columnspan=2,pady=5)

exitbutton=tk.Button(mainframe,text="Exit",width=20,height=2,command=exitbutton)
exitbutton.grid(row=7,column=4,columnspan=2,pady=5)








root.mainloop()