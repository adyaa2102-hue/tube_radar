import os
import tkinter as tk
from tkinter import messagebox

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise SystemExit("Missing API_KEY. Create a .env file (see .env.example).")

client = Groq(api_key=API_KEY)

BG = "#cb3b09"
FG = "#eceada"
ACCENT = "#6e0f2d"
FONT = "TT Fors Bold"


def get_text():
    topic = entry_1.get().strip()
    if not topic:
        messagebox.showwarning("TubeRadar", "Please enter a topic first.")
        return

    button_1.config(state="disabled", text="Searching...")
    window.update_idletasks()

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{
                "role": "user",
                "content": (
                    f"Recommend what channels to watch if I like {topic}. "
                    "Give a short point to point answer in a way matching the given topic "
                    "and using emojis matching the given topic. Remove the * symbols and use "
                    "sufficient spacing to make the answer look less congested while looking elegant."
                ),
            }],
        )
        answer_label.config(text=response.choices[0].message.content)
    except Exception as e:
        messagebox.showerror("TubeRadar", f"Something went wrong:\n{e}")
    finally:
        button_1.config(state="normal", text="best channels to watch")


window = tk.Tk()
window.title("TubeRadar")
window.geometry("800x800")
window.configure(bg=BG)

header = tk.Label(window, text="TubeRadar", font=(FONT, 30, "bold", "underline"), fg=FG, bg=BG)
header.pack(pady=10)

label_1 = tk.Label(window, text="Topics & themes —", font=(FONT, 16, "bold", "underline"), fg=FG, bg=BG)
label_1.pack(pady=20, padx=20, anchor="w")

entry_1 = tk.Entry(window, bg=FG, fg=ACCENT, font=(FONT, 16), borderwidth=0, relief="flat")
entry_1.pack()

button_1 = tk.Button(window, bg=FG, fg=ACCENT, font=(FONT, 16),
                     text="best channels to watch", command=get_text)
button_1.pack(pady=10)

answer_label = tk.Label(window, text="", font=(FONT, 12), fg=FG, bg=BG,
                        justify="left", wraplength=740)
answer_label.pack(pady=10)

window.mainloop()
