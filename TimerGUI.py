import tkinter as tk
from tkinter import messagebox
import threading
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        self.time_left = 0
        self.running = False
        self.timer_thread = None

        self.label = tk.Label(root, text="00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.end_button = tk.Button(root, text="End", command=self.root.quit)

        self.start_button.pack(side=tk.LEFT, padx=10)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        self.end_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        if not self.running:
            self.time_left = int(input("Enter timer minutes: ")) * 60
            self.running = True
            self.timer_thread = threading.Thread(target=self.update_timer)
            self.timer_thread.start()

    def update_timer(self):
        while self.time_left > 0 and self.running:
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.label.config(text=time_str)
            time.sleep(1)
            self.time_left -= 1

        if self.time_left == 0:
            self.running = False
            self.timer_completed()

    def stop_timer(self):
        self.running = False
        self.timer_thread.join()

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.label.config(text="00:00")

    def timer_completed(self):
        messagebox.showinfo("Timer Completed", "Timer has finished!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
