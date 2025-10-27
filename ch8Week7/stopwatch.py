import tkinter as tk

def startTimer():
    if running:
        global timer
        timer += 1
        timeText.configure(text = str(timer))
    root.after(10, startTimer)

def start():
    global running
    running = True

def stop():
    global running
    running = False

running = False

root = tk.Tk()

timer = 0

timeText = tk.Label(root, text = "0", font = ("Helvetica", 80))
timeText.pack()

startButton = tk.Button(root, text = "시작", bg = "yellow", command = start)
startButton.pack(fill = tk.BOTH)

stopButton = tk.Button(root, text = "중지", bg = "yellow", command = stop)
stopButton.pack(fill = tk.BOTH)

startTimer()
root.mainloop()