import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("750x500")

        

        self.topics = {
            "Topic 1": [
                Question("What is the output of the following code? `if True: print('Yes') else: print('No')`", ["Yes", "No", "Error", "None"], "Yes"),
                Question("Which loop is used to iterate over a sequence (e.g., list, tuple, string)?", ["for loop", "while loop", "do-while loop", "foreach loop"], "for loop"),
                Question("What keyword is used to skip the current iteration of a loop?", ["skip", "break", "pass", "continue"], "continue"),
                Question("What is the purpose of the `else` clause in a for loop?", ["To execute if the loop terminates normally", "To execute regardless of loop termination", "To handle exceptions", "To break out of the loop"], "To execute if the loop terminates normally"),
                Question("What is the output of `for i in range(1, 10, 2): print(i)`?", ["1 2 3 4 5 6 7 8 9", "1 3 5 7 9", "2 4 6 8 10", "1 2 4 6 8"], "1 3 5 7 9"),
            ],
            "Topic 2": [
                Question("Which of the following is an immutable data type?", ["list", "set", "tuple", "dictionary"], "tuple"),
                Question("What will be the result of `5 // 2`?", ["2.5", "2", "3", "2.0"], "2"),
                Question("Which operator is used to check if two values are equal?", ["=", "==", "!=", "==="], "=="),
                Question("What type of literal is `3.14`?", ["Integer", "Float", "String", "Complex"], "Float"),
                Question("What is the output of `print(3 * 'abc')`?", ["abcabcabc", "abc", "abcabc abcabc", "Error"], "abcabcabc"),
            ],
            "Topic 3": [
                Question("What is the output of `'Python'[1:4]`?", ["'Pyt'", "'yth'", "'ytho'", "'yth'"], "'yth'"),
                Question("How do you convert a string to uppercase?", ["string.upper()", "string.capitalize()", "string.toUpperCase()", "string.casefold()"], "string.upper()"),
                Question("What does `'Hello'.find('e')` return?", ["1", "-1", "True", "False"], "1"),
                Question("How do you concatenate two strings in Python?", ["str1.append(str2)", "str1 + str2", "str1.concat(str2)", "str1.join(str2)"], "str1 + str2"),
                Question("What is the output of `'Python'.lower()`?", ["'python'", "'Python'", "'PYTHON'", "'PythoN'"], "'python'"),
            ],
            "Topic 4": [
                Question("Which keyword is used to handle exceptions?", ["try", "except", "catch", "raise"], "except"),
                Question("What exception is raised when a division by zero is attempted?", ["ZeroDivisionError", "ValueError", "TypeError", "ArithmeticError"], "ZeroDivisionError"),
                Question("How do you raise an exception in Python?", ["raise Exception()", "throw Exception()", "except Exception()", "assert Exception()"], "raise Exception()"),
                Question("What is the purpose of the `finally` clause?", ["To execute code regardless of an exception", "To catch exceptions", "To re-raise exceptions", "To terminate a program"], "To execute code regardless of an exception"),
                Question("What is the output of the following code? `try: print(1/0) except ZeroDivisionError: print('Error') finally: print('Done')`", ["Error Done", "Error", "Done", "ZeroDivisionError"], "Error Done"),
            ],
            "Topic 5": [
                Question("Which method is used to read the entire content of a file?", ["read()", "readline()", "readlines()", "readfile()"], "read()"),
                Question("How do you open a file in write mode?", ["open('file.txt', 'r')", "open('file.txt', 'w')", "open('file.txt', 'a')", "open('file.txt', 'rw')"], "open('file.txt', 'w')"),
                Question("What does the `close()` method do?", ["Closes the file", "Saves the file", "Deletes the file", "Opens the file"], "Closes the file"),
                Question("What is the output of `file.read()` if the file is empty?", ["None", "EOF", "", "Error"], ""),
                Question("How can you write a string to a file?", ["file.write(string)", "file.append(string)", "file.insert(string)", "file.add(string)"], "file.write(string)"),
            ],
            "Topic 6": [
                Question("What is the keyword to define a function?", ["function", "def", "fun", "func"], "def"),
                Question("What is the output of the following code? `def func(a, b=2): return a + b; print(func(3))`", ["3", "5", "TypeError", "None"], "5"),
                Question("What does the `return` statement do in a function?", ["Terminates the function", "Returns a value from the function", "Both a and b", "None of the above"], "Both a and b"),
                Question("How do you call a function named `my_function`?", ["my_function()", "call my_function()", "execute my_function()", "run my_function()"], "my_function()"),
                Question("What is a lambda function?", ["A function with no name", "A function with no parameters", "A function defined using the `lambda` keyword", "Both a and c"], "Both a and c"),
            ],
            "Topic 7": [
                Question("What is a nested function?", ["A function defined inside another function", "A function called from another function", "A function that calls itself", "A function that returns another function"], "A function defined inside another function"),
                Question("What is the purpose of a nested function?", ["To create closures", "To organize code", "To provide encapsulation", "All of the above"], "All of the above"),
                Question("What is a closure in Python?", ["A function with no parameters", "A function that returns another function", "A nested function that remembers the enclosing function's variables", "A function with default parameters"], "A nested function that remembers the enclosing function's variables"),
                Question("How do you define a nested function?", ["def outer(): def inner(): pass", "def outer() { def inner() }", "def outer(inner(): pass)", "def outer(inner() {}"], "def outer(): def inner(): pass"),
                Question("What is the output of the following code? `def outer(): x = 5; def inner(): return x; return inner; print(outer()())`", ["5", "Error", "None", "0"], "5"),
            ],
            "Topic 8" : [
    Question("What is a Python decorator?", ["A function that adds functionality to another function", "A loop structure", "A conditional statement", "A module"], "A function that adds functionality to another function"),
    Question("How do you define a simple decorator in Python?", ["def decorator(func):", "def func(decorator):", "def decorator(){}", "def func():"], "def decorator(func):"),
    Question("Which symbol is used to apply a decorator to a function?", ["@", "#", "$", "&"], "@"),
    Question("What is the output of the following code?\n```\ndef decorator(func):\n    def wrapper():\n        print('Hello')\n        func()\n        print('Goodbye')\n    return wrapper\n\n@decorator\ndef say_hello():\n    print('Hello, World!')\nsay_hello()\n```", ["Hello\nHello, World!\nGoodbye", "Hello, World!", "Goodbye\nHello\nHello, World!", "Hello\nGoodbye\nHello, World!"], "Hello\nHello, World!\nGoodbye"),
    Question("What is a common use case for decorators?", ["Modifying strings", "Looping through lists", "Logging and authentication", "Handling exceptions"], "Logging and authentication"),
            ]

        }


        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)

        for i in range(10):
            self.main_frame.grid_columnconfigure(i, weight=1)
            self.main_frame.grid_rowconfigure(i, weight=1)
            def exit():
                root.destroy()
        self.exitbutton=tk.Button(self.main_frame,text="Exit",command=exit,width=20,height=2)
        self.exitbutton.grid(row=9,column=2)
        # Create buttons for topics
        for idx, topic in enumerate(self.topics.keys()):
            column = 0 if idx < 4 else 1  # Place first 5 buttons in column 0, next 5 in column 1
            row = idx % 4 # Row number for the current button
            tk.Button(self.main_frame, text=topic, command=lambda t=topic: self.start_quiz(t), height=2, width=20).grid(row=row, column=column, padx=10, pady=10)

    def start_quiz(self, topic):
        self.current_topic = topic
        self.questions = self.topics[topic]
        self.current_question_index = 0
        self.score = 0
        self.user_answers = []

        self.main_frame.pack_forget()
        self.quiz_frame = tk.Frame(self.root)
        self.quiz_frame.pack(pady=20)

        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.option_buttons = []

        for option in range(4):
            rb = tk.Radiobutton(self.quiz_frame, text="", variable=self.var, value="", font=("Arial", 14))
            rb.pack(anchor='w')
            self.option_buttons.append(rb)

        self.prev_button = tk.Button(self.quiz_frame, text="Previous", command=self.previous_question)
        self.prev_button.pack(side='left', padx=10)

        self.next_button = tk.Button(self.quiz_frame, text="Next", command=self.next_question)
        self.next_button.pack(side='left', padx=10)

        self.submit_button = tk.Button(self.quiz_frame, text="Submit", command=self.submit_quiz)
        self.submit_button.pack(side='left', padx=10)

        self.back_button = tk.Button(self.quiz_frame, text="Back to Topics", command=self.back_to_topics)
        self.back_button.pack(side='left', padx=10)

        self.display_question()

    def display_question(self):
        question = self.questions[self.current_question_index]
        self.question_label.config(text=question.prompt)
        self.var.set("") 

        for idx, option in enumerate(question.options):
            self.option_buttons[idx].config(text=option, value=option)

    def next_question(self):
        if self.current_question_index < len (self.questions) - 1:
            self.user_answers.append(self.var.get())  
            self.current_question_index += 1
            self.display_question()

    def previous_question(self):
        if self.current_question_index > 0:
            self.user_answers.append(self.var.get())
            self.current_question_index -= 1
            self.display_question()

    def submit_quiz(self):
        self.user_answers.append(self.var.get())  
        self.score = sum(1 for i, answer in enumerate(self.user_answers) 
                         if answer.strip().lower() == self.questions[i].answer.strip().lower())
        messagebox.showinfo("Quiz Result", f"You scored {self.score} out of {len(self.questions)}")
        self.back_to_topics()

    def back_to_topics(self):
        self.quiz_frame.pack_forget()
        self.main_frame.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()