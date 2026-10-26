from groq import Groq
import tkinter as tk
def  get_text():
    topic = entry_1.get()
    client = Groq(api_key='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')
    response = client.chat.completions.create(model='openai/gpt-oss-120b', messages=[{
    'role': "user",
    "content": f"recommend what channels to watch if I like{topic}.Give a short point to point answer in a way matching the given topic and using emojis matching the given topic.remove the * symbols and use suffiecient spacing to make the answer look less congested while looking elegent",
}])
    (response.choices[0].message.content)
    answer_label = tk.Label(window,text=response.choices[0].message.content,font=("TT Fors Bold", 12),fg="#eceada",bg="#cb3b09")
    answer_label.pack(pady=10)


window = tk.Tk()
window.title("TubeRadar")
window.geometry("800x800")
window.configure(bg="#cb3b09")
header = tk.Label(window, text="TubeRadar",font=("TT Fors Bold", 30,'bold','underline'),fg="#eceada",bg="#cb3b09")
header.pack(pady=10)
label_1 = tk.Label(window,text='Topics & themes —',font=("TT Fors Bold", 16,'bold','underline'),fg="#eceada",bg="#cb3b09")
label_1.pack(pady=20,padx=20,anchor="w")

entry_1 = tk.Entry(window,bg="#eceada",fg="#6e0f2d",font=("TT Fors Bold", 16),borderwidth=0,relief="flat")
entry_1.pack()
button_1 = tk.Button(window,bg="#eceada",fg="#6e0f2d",font=("TT Fors Bold", 16),text='best channels to watch',command=get_text)
button_1.pack(pady=10)
window.mainloop()
