import tkinter as tk

from buttons import MainWindow


def main():
    root = tk.Tk()
    my_gui = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    print('Starting Script...')
    main()