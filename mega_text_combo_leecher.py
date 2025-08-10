import re, threading, webbrowser, tkinter.filedialog as fd, tkinter.messagebox as mb
import customtkinter as ctk

CREDITS_URL = "https://t.me/therealyashvirgaming"
CREDITS_TEXT = "Made with love ♥ by Yashvir Gaming"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mega Text Combo Leecher")
        self.geometry("1100x700")
        self.minsize(980, 580)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.header = ctk.CTkLabel(self, text="Mega Text Combo Leecher", font=("Segoe UI Semibold", 22))
        self.header.grid(row=0, column=0, columnspan=2, padx=16, pady=(12, 6), sticky="nw")

        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.grid(row=1, column=0, padx=(16, 8), pady=(6, 8), sticky="nsew")
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(1, weight=1)
        ctk.CTkLabel(self.left_frame, text="Text:", font=("Segoe UI", 13)).grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))
        self.input_box = ctk.CTkTextbox(self.left_frame, wrap="none")
        self.input_box.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

        self.right_mid = ctk.CTkFrame(self)
        self.right_mid.grid(row=1, column=1, padx=(8, 16), pady=(6, 8), sticky="nsew")
        self.right_mid.grid_columnconfigure(0, weight=1)
        self.right_mid.grid_rowconfigure(1, weight=1)
        ctk.CTkLabel(self.right_mid, text="Combo:", font=("Segoe UI", 13)).grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))
        self.output_box = ctk.CTkTextbox(self.right_mid, wrap="none", state="normal")
        self.output_box.grid(row=1, column=0, padx=(10, 120), pady=(0, 10), sticky="nsew")

        self.ctrl_panel = ctk.CTkFrame(self.right_mid, width=120)
        self.ctrl_panel.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nse")
        self.ctrl_panel.grid_propagate(False)

        self.btn_open = ctk.CTkButton(self.ctrl_panel, text="Open", command=self.open_file, width=100)
        self.btn_open.grid(row=0, column=0, padx=10, pady=(10, 10))
        self.btn_leech = ctk.CTkButton(self.ctrl_panel, text="Leech", command=self.start_leech, width=100)
        self.btn_leech.grid(row=1, column=0, padx=10, pady=10)
        self.btn_save = ctk.CTkButton(self.ctrl_panel, text="Save", command=self.save_file, width=100)
        self.btn_save.grid(row=2, column=0, padx=10, pady=10)
        self.btn_reset = ctk.CTkButton(self.ctrl_panel, text="Reset", command=self.reset_all, width=100)
        self.btn_reset.grid(row=3, column=0, padx=10, pady=10)
        self.btn_exit = ctk.CTkButton(self.ctrl_panel, text="Exit", command=self.destroy, width=100)
        self.btn_exit.grid(row=7, column=0, padx=10, pady=(80, 10), sticky="s")

        self.status = ctk.CTkLabel(self, text="", anchor="w")
        self.status.grid(row=2, column=0, columnspan=2, sticky="ew", padx=16, pady=(0, 6))

        self.credit_btn = ctk.CTkButton(self, text="Credits", command=self.show_credits, height=34)
        self.credit_btn.grid(row=3, column=0, columnspan=2, padx=16, pady=(0, 12), sticky="ew")

        self.re_pat = re.compile(r'([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})\s*:\s*([^\s|;]+)', re.IGNORECASE)

    def set_busy(self, busy=True, msg=""):
        state = "disabled" if busy else "normal"
        for b in (self.btn_open, self.btn_leech, self.btn_save, self.btn_reset, self.btn_exit, self.credit_btn):
            b.configure(state=state)
        self.status.configure(text=msg)

    def open_file(self):
        fn = fd.askopenfilename(title="Open text file", filetypes=[("Text files","*.txt"), ("All files","*.*")])
        if not fn: return
        try:
            with open(fn, "r", encoding="utf-8", errors="ignore") as fr:
                data = fr.read()
            self.input_box.insert("end", data if data.endswith("\n") else data + "\n")
            self.status.configure(text=f"Loaded: {fn}")
        except Exception as e:
            mb.showerror("Error", str(e))

    def save_file(self):
        data = self.output_box.get("1.0", "end").strip()
        if not data:
            mb.showinfo("Info", "Nothing to save.")
            return
        fn = fd.asksaveasfilename(title="Save combos", defaultextension=".txt", filetypes=[("Text files","*.txt")])
        if not fn: return
        try:
            with open(fn, "w", encoding="utf-8") as fw:
                fw.write(data + ("\n" if not data.endswith("\n") else ""))
            self.status.configure(text=f"Saved: {fn}")
        except Exception as e:
            mb.showerror("Error", str(e))

    def reset_all(self):
        self.input_box.delete("1.0", "end")
        self.output_box.delete("1.0", "end")
        self.status.configure(text="")

    def start_leech(self):
        raw = self.input_box.get("1.0", "end")
        if not raw.strip():
            mb.showinfo("Info", "Paste text first.")
            return
        t = threading.Thread(target=self.leech_worker, args=(raw,), daemon=True)
        self.set_busy(True, "Processing...")
        t.start()

    def leech_worker(self, raw):
        matches = []
        append = matches.append
        for m in self.re_pat.finditer(raw):
            append(f"{m.group(1)}:{m.group(2)}")
        out = "\n".join(matches)
        self.after(0, self.finish_leech, out, len(matches))

    def finish_leech(self, out, n):
        self.output_box.delete("1.0", "end")
        if out:
            self.output_box.insert("1.0", out + ("\n" if not out.endswith("\n") else ""))
        self.set_busy(False, f"Found {n} combos")

    def show_credits(self):
        w = ctk.CTkToplevel(self)
        w.title("Credits")
        w.geometry("420x180")
        w.resizable(False, False)
        ctk.CTkLabel(w, text=CREDITS_TEXT, font=("Segoe UI Semibold", 16)).pack(pady=(18, 6))
        link = ctk.CTkLabel(w, text=CREDITS_URL, font=("Consolas", 14, "underline"))
        link.pack(pady=6)
        link.bind("<Button-1>", lambda e: webbrowser.open_new(CREDITS_URL))
        ctk.CTkButton(w, text="Open Link", command=lambda: webbrowser.open_new(CREDITS_URL), width=120).pack(pady=10)
        ctk.CTkButton(w, text="Close", command=w.destroy, width=120).pack(pady=(4, 12))

if __name__ == "__main__":
    App().mainloop()
