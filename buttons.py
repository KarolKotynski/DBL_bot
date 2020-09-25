from threading import Thread
import tkinter as tk

from button_actions import (
    bool_dictionary,
    attack_monster,
    auto_heal,
    auto_senzu,
    train_ki,
    antikick,
    cavebot,
    spell_or_heal,
    msgcheck,
    battle_list_area_func
)


class MainWindow(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.auto_attack_btn = tk.Button(self, text='Auto Attack', command=self.auto_attack_thread)
        self.auto_heal_btn = tk.Button(self, text='Auto Heal', command=self.auto_heal_thread)
        self.auto_senzu_btn = tk.Button(self, text='Auto Senzu', command=self.auto_senzu_thread)
        self.train_ki_btn = tk.Button(self, text='Train KI', command=self.train_ki_thread)
        self.anti_kick_btn = tk.Button(self, text='Antikick', command=self.antikick_thread)
        self.cavebot_btn = tk.Button(self, text='Cavebot', command=self.cavebot_thread)
        self.spell_or_heal_btn = tk.Button(self, text='Cast spell or Heal', command=self.spell_or_heal_thread)
        self.msgcheck_btn = tk.Button(self, text='MSGcheck', command=self.msgcheck_thread)
        self.monster_label = tk.Label(self, text='Monster')
        self.health_percent_label = tk.Label(self, text='Health Percent')
        self.mana_percent_label = tk.Label(self, text='Mana Percent')
        self.monster_entry = tk.Entry(self, justify='center')
        self.health_percent = tk.Entry(self, justify='center')
        self.mana_percent = tk.Entry(self, justify='center')
        self.master = master
        self.master.title('DBL helper')
        self.master.geometry('400x300')
        self.master.wm_attributes('-topmost', 1)
        self.master.resizable(0, 0)
        self.buttons()
        self.pack()
        self.battle_list_thread = Thread(target=battle_list_area_func)
        self.battle_list_thread.start()

    def buttons(self):
        # BUTTONS
        self.auto_attack_btn.grid(row=0, column=0, sticky='nswe')
        self.auto_attack_btn.configure(width=17, height=2, background='snow', borderwidth=2)

        self.auto_heal_btn.grid(row=1, column=0, sticky='nswe')
        self.auto_heal_btn.configure(width=17, height=2, background='snow', borderwidth=2)

        self.auto_senzu_btn.grid(row=2, column=0, sticky='nswe')
        self.auto_senzu_btn.configure(width=17, height=2, background='snow', borderwidth=2)

        self.train_ki_btn.grid(row=3, column=0, sticky='nswe')
        self.train_ki_btn.configure(width=17, height=2, background='snow', borderwidth=2)

        self.anti_kick_btn.grid(row=4, column=0, sticky='nswe')
        self.anti_kick_btn.configure(width=17, height=2, background='snow', borderwidth=2)

        self.cavebot_btn.grid(row=5, column=0, sticky='nswe')
        self.cavebot_btn.configure(width=17, height=2, background='snow', borderwidth=2)

        self.spell_or_heal_btn.grid(row=6, column=0, sticky='nswe')
        self.spell_or_heal_btn.configure(width=17, height=2, background='snow', borderwidth=2)

        self.msgcheck_btn.grid(row=3, column=1, sticky='nswe')
        self.msgcheck_btn.configure(width=17, height=2, background='snow', borderwidth=2)

        # LABELS
        self.monster_label.grid(sticky='nswe', row=0, column=1)

        self.health_percent_label.grid(sticky='nswe', row=1, column=1)

        self.mana_percent_label.grid(sticky='nswe', row=2, column=1)

        # ENTRY
        self.monster_entry.grid(sticky='nswe', row=0, column=2)
        self.monster_entry.insert(0, 'Wolf')

        self.health_percent.grid(sticky='nswe', row=1, column=2)
        self.health_percent.insert(0, '70')

        self.mana_percent.grid(sticky='nswe', row=2, column=2)
        self.mana_percent.insert(0, '70')

    def auto_attack_thread(self):
        if not bool_dictionary['Auto Attack']:
            bool_dictionary['Auto Attack'] = True
            self.auto_attack_btn.configure(background='green')
            attack_func = Thread(target=attack_monster, args=(self.monster_entry.get(),))
            attack_func.start()
        else:
            bool_dictionary['Auto Attack'] = False
            self.auto_attack_btn.configure(background='snow')

    def auto_heal_thread(self):
        if not bool_dictionary['Auto Heal']:
            bool_dictionary['Auto Heal'] = True
            self.auto_heal_btn.configure(background='green')
            heal_func = Thread(target=auto_heal, args=(self.health_percent.get(),))
            heal_func.start()
        else:
            bool_dictionary['Auto Heal'] = False
            self.auto_heal_btn.configure(background='snow')

    def auto_senzu_thread(self):
        if not bool_dictionary['Auto Senzu']:
            bool_dictionary['Auto Senzu'] = True
            self.auto_senzu_btn.configure(background='green')
            senzu_func = Thread(target=auto_senzu, args=(self.mana_percent.get(),))
            senzu_func.start()
        else:
            bool_dictionary['Auto Senzu'] = False
            self.auto_senzu_btn.configure(background='snow')

    def train_ki_thread(self):
        if not bool_dictionary['Train KI']:
            bool_dictionary['Train KI'] = True
            self.train_ki_btn.configure(background='green')
            train_ki_func = Thread(target=train_ki, args=(self.mana_percent.get(),))
            train_ki_func.start()
        else:
            bool_dictionary['Train KI'] = False
            self.train_ki_btn.configure(background='snow')

    def antikick_thread(self):
        if not bool_dictionary['Antikick']:
            bool_dictionary['Antikick'] = True
            self.anti_kick_btn.configure(background='green')
            anti_kick_func = Thread(target=antikick)
            anti_kick_func.start()
        else:
            bool_dictionary['Antikick'] = False
            self.anti_kick_btn.configure(background='snow')

    def cavebot_thread(self):
        if not bool_dictionary['Cavebot']:
            bool_dictionary['Cavebot'] = True
            self.cavebot_btn.configure(background='green')
            cavebot_func = Thread(target=cavebot)
            cavebot_func.start()
        else:
            bool_dictionary['Cavebot'] = False
            self.cavebot_btn.configure(background='snow')

    def spell_or_heal_thread(self):
        if not bool_dictionary['Cast spell or Heal']:
            bool_dictionary['Cast spell or Heal'] = True
            self.spell_or_heal_btn.configure(background='green')
            spell_or_heal_func = Thread(target=spell_or_heal, args=(self.health_percent.get(),))
            spell_or_heal_func.start()
        else:
            bool_dictionary['Cast spell or Heal'] = False
            self.spell_or_heal_btn.configure(background='snow')

    def msgcheck_thread(self):
        if not bool_dictionary['MSGcheck']:
            bool_dictionary['MSGcheck'] = True
            self.msgcheck_btn.configure(background='green')
            msgcheck_func = Thread(target=msgcheck)
            msgcheck_func.start()
        else:
            bool_dictionary['MSGcheck'] = False
            self.msgcheck_btn.configure(background='snow')
