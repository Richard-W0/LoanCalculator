import tkinter as tk
import tkinter.ttk as ttk
import pyperclip

def calculate_months_to_pay_off_loan():
    starting_sum = float(alkusumma_entry.get())
    yearly_interest = float(vuosikorko_entry.get())
    monthly_payment = float(perusmaksu_entry.get())
    
    skipped_months_str = skipped_months_entry.get()
    skipped_months_list = [int(month.strip()) for month in skipped_months_str.split(",")]
    
    months_interest = yearly_interest / 12 / 100

    months = 0
    unpaid = starting_sum

    while unpaid > 0:
        montly_interest = unpaid * months_interest
        unpaid += montly_interest

        if months + 1 not in skipped_months_list:
            unpaid -= monthly_payment

            if unpaid < monthly_payment:
                last_payment = unpaid
                unpaid = 0
            else:
                last_payment = monthly_payment
        months += 1

    original_result_text = f"lainassa kestää {months} kuukautta maksaa, ja viimeinen maksuerä on {last_payment:.2f}€."
    result_label.config(text=original_result_text, font=("Roboto", 14))

    simplified_result_text = f"{starting_sum}€\t {yearly_interest}%\t {monthly_payment}€\t {months} kuukautta\t {last_payment:.2f}€"
    simplified_result_label.config(text=simplified_result_text)  
    simplified_result_label.pack_forget()  
    
    copy_button.config(state=tk.NORMAL) 
    copy_button.pack(pady=10)

    

def copy_result_to_clipboard():
    simplified_result_text = simplified_result_label.cget("text") 
    pyperclip.copy(simplified_result_text) 
    copy_button.pack_forget() 


window = tk.Tk()
window.title("LainaLaskuri")
window.geometry("650x500")
window.configure(bg="#333333")


input_frame = tk.Frame(window, bg="#333333")  
input_frame.pack(pady=20)

label_font = ("Roboto", 14)
entry_font = ("Roboto", 14)

style = ttk.Style()
style.configure("TLabel", padding=0)
style.configure("TButton", padding=0)

alkusumma_label = tk.Label(input_frame, text="Lainan määrä:", font=label_font, bg="#333333", fg="#FFFFFF")
alkusumma_label.pack()
alkusumma_entry = tk.Entry(input_frame, font=entry_font)
alkusumma_entry.pack()

vuosikorko_label = tk.Label(input_frame, text="Lainan korko (%):", font=label_font, bg="#333333", fg="#FFFFFF")
vuosikorko_label.pack()
vuosikorko_entry = tk.Entry(input_frame, font=entry_font)
vuosikorko_entry.pack()

perusmaksu_label = tk.Label(input_frame, text="Kuukausittainen maksu:", font=label_font, bg="#333333", fg="#FFFFFF")
perusmaksu_label.pack()
perusmaksu_entry = tk.Entry(input_frame, font=entry_font)
perusmaksu_entry.pack()

skipped_months_label = tk.Label(input_frame, text="Kuukaudet ilman maksua (esim. 3, 15), jos ei ole, laita 0:", font=label_font, bg="#333333", fg="#FFFFFF")
skipped_months_label.pack()
skipped_months_entry = tk.Entry(input_frame, font=entry_font)
skipped_months_entry.pack()

calculate_button_image = tk.PhotoImage(width=1, height=1)
calculate_button_image.put("#FF3399", to=(0, 0, 40, 40))  

copy_button_image = tk.PhotoImage(width=1, height=1)
copy_button_image.put("#FF69B4", to=(0, 0, 40, 40))

calculate_button = ttk.Button(window, text="Laske", command=calculate_months_to_pay_off_loan, style="RoundedButton.TButton")
calculate_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Roboto", 14), bg="#333333", fg="white") 
result_label.pack()

simplified_result_label = tk.Label(window, text="", font=("Roboto", 14), bg="#333333", fg="white") 
simplified_result_label.pack()

copy_button = ttk.Button(window, text="Kopioi tiedot Excel:iin", command=copy_result_to_clipboard, style="RoundedButton.TButton")
copy_button.pack(pady=10)
copy_button.config(state=tk.DISABLED) 

style = ttk.Style()
style.configure("RoundedButton.TButton", padding=10, relief="flat", background="#FF69B4", foreground="black",
                font=("Roboto", 16))
style.map("RoundedButton.TButton", background=[("active", "#FF3399")]) 

window.mainloop()