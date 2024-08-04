import tkinter as tk
from tkinter import messagebox


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ElectricItem(Item):
    pass


class NonElectricItem(Item):
    pass


electric_items = [
    ElectricItem("یخچال", 10000000),
    ElectricItem("تلویزیون", 7000000),
    ElectricItem("مایکروویو", 3000000),
    ElectricItem("جاروبرقی", 1500000),
    ElectricItem("ماشین لباسشویی", 8000000),
    ElectricItem("ماشین ظرفشویی", 9000000),
    ElectricItem("اجاق گاز", 4000000),
    ElectricItem("کولر گازی", 12000000),
    ElectricItem("آبمیوه گیری", 2000000),
    ElectricItem("مخلوط کن", 1800000)
]

non_electric_items = [
    NonElectricItem("میز", 1500000),
    NonElectricItem("صندلی", 500000),
    NonElectricItem("کتابخانه", 2000000),
    NonElectricItem("کمد", 2500000),
    NonElectricItem("تخت خواب", 3000000),
    NonElectricItem("مبل", 3500000),
    NonElectricItem("فرش", 4000000),
    NonElectricItem("پرده", 700000),
    NonElectricItem("ساعت دیواری", 600000),
    NonElectricItem("آینه", 800000)
]


# ایجاد رابط کاربری با tkinter
class ShoppingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("فروشگاه کالاها")

        self.selected_items = []
        self.total_price = 0

        self.select_button = tk.Button(root, text="لطفا اقلام خود را انتخاب کنید", command=self.show_items)
        self.select_button.pack(pady=10)

    def show_items(self):
        self.items_window = tk.Toplevel(self.root)
        self.items_window.title("انتخاب اقلام")

        self.items_listbox = tk.Listbox(self.items_window, selectmode=tk.MULTIPLE, width=50)
        self.items_listbox.pack(pady=10)

        for item in electric_items + non_electric_items:
            self.items_listbox.insert(tk.END, f"{item.name} - {item.price} تومان")

        self.confirm_button = tk.Button(self.items_window, text="تایید خرید", bg="green", fg="white",
                                        command=self.confirm_purchase)
        self.confirm_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.cancel_button = tk.Button(self.items_window, text="انصراف", bg="red", fg="white",
                                       command=self.items_window.destroy)
        self.cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def confirm_purchase(self):
        selected_indices = self.items_listbox.curselection()
        self.selected_items = [
            electric_items[i] if i < len(electric_items) else non_electric_items[i - len(electric_items)] for i in
            selected_indices]

        self.total_price = sum(item.price for item in self.selected_items)

        self.items_window.destroy()

        messagebox.showinfo("مجموع خرید", f"مجموع خرید شما: {self.total_price} تومان")

        self.pay_button = tk.Button(self.root, text="پرداخت", command=self.process_payment)
        self.pay_button.pack(pady=10)

    def process_payment(self):
        messagebox.showinfo("پرداخت", "پرداخت انجام شد")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root)
    root.mainloop()