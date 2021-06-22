import tkinter as tk

import threadom
from threadom import Threadom, QueueTail
import time


def worker(queue=None, i=10):
    pause = 0.2
    if not queue:
        time.sleep(pause)
        return
    while i > 0:
        queue.put(None)
        i -= 1
        time.sleep(pause)
    queue.put(QueueTail)


class Spinner:
    def __init__(self, root, strvar):
        self._root = root
        self._strvar = strvar
        self._i = 0
        self._items = ("/", "|", "\\", "|")
        self._strvar.set("|")

    def spin(self):
        self._strvar.set(self._items[self._i])
        self._i += 1
        self._i = 0 if self._i == 4 else self._i


def run_tasks(root, threadom, spinner, n=19):
    consumer = lambda _, spinner=spinner: spinner.spin()
    threadom.run(target=worker, consumer=consumer)
    n -= 1
    if n > 0:
        command = (lambda root=root,
                          threadom=threadom,
                          spinner=spinner,
                          n=n: run_tasks(root, threadom, spinner, n))
        root.after(200, command)

def consume_queue(root, threadom, spinner, n=19):
    queue = threadom.q()
    consumer = (lambda var, spinner=spinner:
                spinner.spin() if var is not QueueTail else None)
    target_kwargs = {"queue": queue, "i": n}
    threadom.run(target=worker,
                 target_kwargs=target_kwargs)
    threadom.consume(queue, consumer=consumer)


def main():
    root = tk.Tk()
    root.title("Test Multithreading")
    root.geometry("+0+0")
    threadom = Threadom(root)
    # string var
    strvar = tk.StringVar()
    # spinner
    spinner = Spinner(root, strvar)
    # label
    label = tk.Label(root, font=(None, 200),
                     textvariable=strvar)
    label.pack(padx=50, pady=50,
               fill=tk.BOTH, expand=1)
    # footer
    frame = tk.Frame(root)
    frame.pack(fill=tk.X)
    # button spin
    command = lambda spinner=spinner: spinner.spin()
    button_a = tk.Button(frame, text="Spin",
                         command=command)
    button_a.pack(side=tk.LEFT)
    # button run tasks
    command = (lambda root=root, spinner=spinner:
               run_tasks(root, threadom, spinner))
    button_b = tk.Button(frame, text="Run Tasks",
                         command=command)
    button_b.pack(side=tk.LEFT)
    # button consume queue
    command = (lambda root=root, spinner=spinner:
               consume_queue(root, threadom, spinner))
    button_c = tk.Button(frame, text="Consume Queue",
                         command=command)
    button_c.pack(side=tk.LEFT)
    # mainloop
    root.mainloop()


if __name__ == "__main__":
    print("https://github.com/pyrustic/threadom")
    main()
