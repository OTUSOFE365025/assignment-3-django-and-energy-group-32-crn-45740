# gui_scanner.py
import os, sys, django
from decimal import Decimal
import tkinter as tk
from tkinter import messagebox, ttk

# ---------------- Theme / layout tweaks you can easily change ----------------
WINDOW_SIZE   = "380x420"   # make the window smaller or bigger here
ACCENT        = "#2d6cdf"   # primary accent (Scan button)
DANGER        = "#e25555"   # Clear Cart
NEUTRAL       = "#666666"   # Exit
BG            = "#f7f7fb"   # window background
FG            = "#111111"
FONT_BASE     = ("Arial", 11)
FONT_TITLE    = ("Arial", 14, "bold")
# -----------------------------------------------------------------------------

# setup Django ORM environment
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import Product


class CashRegisterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cash Register Scanner")
        self.root.geometry(WINDOW_SIZE)
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.total = Decimal("0.00")

        # ---------------- Title ----------------
        tk.Label(root, text="Cash Register Scanner", font=FONT_TITLE, bg=BG, fg=FG).pack(pady=(10, 6))

        # ---------------- Display (Treeview) ----------------
        display_frame = tk.Frame(root, bg=BG)
        display_frame.pack(padx=10, pady=(0, 8), fill="both", expand=True)

        columns = ("Product", "Price")
        self.tree = ttk.Treeview(display_frame, columns=columns, show="headings", height=9)
        self.tree.heading("Product", text="Product Name")
        self.tree.heading("Price", text="Price ($)")
        self.tree.column("Product", width=230, anchor="w")
        self.tree.column("Price", width=80, anchor="e")

        # Scrollbar
        vsb = ttk.Scrollbar(display_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        display_frame.rowconfigure(0, weight=1)
        display_frame.columnconfigure(0, weight=1)

        # ---------------- Input (UNDER the display) ----------------
        input_frame = tk.Frame(root, bg=BG)
        input_frame.pack(padx=10, pady=(4, 6), fill="x")

        tk.Label(input_frame, text="Enter UPC:", font=FONT_BASE, bg=BG, fg=FG).grid(row=0, column=0, padx=(0, 6))
        self.upc_entry = tk.Entry(input_frame, font=FONT_BASE, width=18)
        self.upc_entry.grid(row=0, column=1, padx=(0, 6))
        self.upc_entry.bind("<Return>", self.scan_product)
        self.upc_entry.focus()

        # Colored Scan button next to the entry
        self.scan_btn = tk.Button(
            input_frame, text="Scan", font=FONT_BASE,
            command=self.scan_product, bg=ACCENT, fg="white",
            activebackground=ACCENT, activeforeground="white", relief="flat"
        )
        self.scan_btn.grid(row=0, column=2)

        # ---------------- Total ----------------
        total_frame = tk.Frame(root, bg=BG)
        total_frame.pack(padx=10, pady=(6, 8), fill="x")

        self.total_label = tk.Label(total_frame, text="Total: $0.00", font=("Arial", 13, "bold"), bg=BG, fg=FG)
        self.total_label.pack(anchor="e")

        # ---------------- Bottom Buttons ----------------
        btn_frame = tk.Frame(root, bg=BG)
        btn_frame.pack(padx=10, pady=(2, 10), fill="x")

        self.clear_btn = tk.Button(
            btn_frame, text="Clear Cart", font=FONT_BASE,
            command=self.clear_cart, bg=DANGER, fg="white",
            activebackground=DANGER, activeforeground="white", relief="flat"
        )
        self.clear_btn.pack(side="left")

        self.exit_btn = tk.Button(
            btn_frame, text="Exit", font=FONT_BASE,
            command=root.destroy, bg=NEUTRAL, fg="white",
            activebackground=NEUTRAL, activeforeground="white", relief="flat"
        )
        self.exit_btn.pack(side="right")

        # Light styling for ttk so it blends a bit better
        self._style_tree()

    # ---------- Style helpers ----------
    def _style_tree(self):
        style = ttk.Style()
        # Use default theme but tweak row height and fonts a bit
        try:
            style.configure("Treeview", rowheight=24, font=FONT_BASE)
            style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
        except Exception:
            pass

    # ---------- Actions ----------
    def scan_product(self, event=None):
        upc = self.upc_entry.get().strip()
        if not upc:
            messagebox.showwarning("Input Error", "Please enter a UPC code.")
            return

        try:
            product = Product.objects.get(upc=upc)
            self.add_to_cart(product)
        except Product.DoesNotExist:
            messagebox.showerror("Not Found", f"No product found for UPC: {upc}")
        finally:
            self.upc_entry.delete(0, tk.END)
            self.upc_entry.focus()

    def add_to_cart(self, product):
        # Insert row
        # Ensure price prints as 2-decimal string even if Decimal
        self.tree.insert("", "end", values=(product.name, f"{Decimal(product.price):.2f}"))
        # Update total
        self.total += Decimal(product.price)
        self._refresh_total()

    def clear_cart(self):
        if messagebox.askyesno("Clear Cart", "Clear all items?"):
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.total = Decimal("0.00")
            self._refresh_total()

    def _refresh_total(self):
        self.total_label.config(text=f"Total: ${self.total:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CashRegisterGUI(root)
    root.mainloop()
