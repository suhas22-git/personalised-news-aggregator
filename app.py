import tkinter as tk
from tkinter import ttk
import requests

API_KEY = "992325d1c966461098d47a32e9fe0172"

root = tk.Tk()
root.title("Personalised News Aggregator")
root.geometry("550x450")

# Heading
heading = tk.Label(root, text="Personalised News Aggregator", font=("Arial", 16, "bold"))
heading.pack(pady=10)

# Category label
label = tk.Label(root, text="Select News Category")
label.pack()

# Dropdown
categories = ["technology", "sports", "business", "entertainment", "health"]
category_box = ttk.Combobox(root, values=categories)
category_box.pack()
category_box.set("technology")

# Function to fetch news
def get_news():
    category = category_box.get()
    url = f"https://newsapi.org/v2/everything?q={category}&apiKey={API_KEY}"


    response = requests.get(url)
    data = response.json()
    
    print(data)


    text_area.delete("1.0", tk.END)

    for article in data["articles"][:6]:
        text_area.insert(tk.END, "• " + article["title"] + "\n\n")

# Button
btn = tk.Button(root, text="Get News", command=get_news)
btn.pack(pady=10)

# Text area
text_area = tk.Text(root, wrap="word", height=15, width=65)
text_area.pack(padx=10, pady=10)

root.mainloop()
