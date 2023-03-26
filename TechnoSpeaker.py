import os
import tkinter as tk

def speak_text():
    x = text_input.get()
    command = f"PowerShell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')"
    os.system(command)
    text_input.delete(0, tk.END)

if __name__ == '__main__':
    window = tk.Tk()
    window.title("TechnoSpeaker")

    window.geometry("400x200+100+100")

    text_input = tk.Entry(window, width=50, font=("Arial", 14))
    text_input.pack(pady=20)
    text_input.configure(bg="#f0f0f0", fg="#000000", relief="solid", bd=1)

    speak_button = tk.Button(window, text="Speak", command=speak_text, font=("Arial", 14), bg="#4CAF50", fg="#ffffff")
    speak_button.pack(pady=10)
    speak_button.configure(relief="raised", bd=3)

    window.mainloop()