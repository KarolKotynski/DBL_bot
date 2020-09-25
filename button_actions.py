import ctypes
import random
import time
import winsound

import autoit
import cv2 as cv2
import keyboard
import numpy as np
import pyautogui

from utils.current_images import current_image

user32 = ctypes.windll.user32

bool_dictionary = {
    'Auto Attack': False,
    'Auto Heal': False,
    'Auto Senzu': False,
    'Train KI': False,
    'Antikick': False,
    'Cavebot': False,
    'Cast spell or Heal': False,
    'MSGcheck': False,
    'ENABLE BOT': False
}

battle_list_area = dict(
    left=0,
    top=0,
    width=188,
    height=900)

minimap_area = dict(
    left=0,
    top=0,
    width=188,
    height=420)

chat_area = dict(
    left=0,
    top=0,
    width=int(user32.GetSystemMetrics(0)),
    height=int(user32.GetSystemMetrics(0)))

health_info_area = [0, 0]

monsters_dictionary = dict(available=0, attacked=0)


def attack_monster(monster):
    while bool_dictionary['Auto Attack']:
        find_monster(monster)
        if not bool_dictionary['Auto Attack']:
            break


def auto_heal(percent_hp):
    while bool_dictionary['Auto Heal']:
        check_hp(percent_hp, health_info_area)
        if not bool_dictionary['Auto Heal']:
            break


def auto_senzu(percent_mana):
    while bool_dictionary['Auto Senzu']:
        check_mana(percent_mana, health_info_area, title='senzu')
        if not bool_dictionary['Auto Senzu']:
            break


def train_ki(percent_mana):
    while bool_dictionary['Train KI']:
        check_mana(percent_mana, health_info_area, title='Train KI')
        if not bool_dictionary['Train KI']:
            break


def antikick():
    while bool_dictionary['Antikick']:
        pyautogui.keyDown('ctrl')
        pyautogui.press('right')
        pyautogui.press('left')
        pyautogui.keyUp('ctrl')
        time.sleep(random.randint(500, 700))
        if not bool_dictionary['Antikick']:
            break


def cavebot():
    waypoint = 1
    while bool_dictionary['Cavebot']:
        current_minimap = current_image(minimap_area)
        searching_waypoint = cv2.imread(f'waypoints/wpt{waypoint}.png')
        template = cv2.matchTemplate(current_minimap, searching_waypoint, cv2.TM_CCOEFF_NORMED)
        threshold = 0.95
        template_loc = np.where(template >= threshold)
        # print(template_loc[0], template_loc[1])
        # print(f'avbl: {monsters_dictionary["available"]}, attacked: {monsters_dictionary["attacked"]}')
        if not bool_dictionary['Auto Attack']:
            monsters_dictionary["available"] = 0
            monsters_dictionary["attacked"] = 0
        if len(template_loc[0]) != 0 and monsters_dictionary["available"] == 0 \
                and monsters_dictionary["attacked"] == 0:
            x_mouse, y_mouse = pyautogui.position()
            pyautogui.moveTo(template_loc[1][0] + minimap_area['left'], template_loc[0][0] + 2 + minimap_area['top'], 0)
            pyautogui.click()
            pyautogui.moveTo(x_mouse, y_mouse, 0)
            time.sleep(2)
        elif len(template_loc[0]) == 0 and monsters_dictionary["available"] == 0 \
                and monsters_dictionary["attacked"] == 0:
            waypoint += 1
        else:
            pass
        if waypoint > 20:
            waypoint = 1
        if keyboard.is_pressed("delete") or not bool_dictionary['Cavebot']:
            bool_dictionary['Cavevot'] = False
            break


def spell_or_heal(percent_hp):
    while bool_dictionary['Cast spell or Heal']:
        heal = check_hp(percent_hp, health_info_area)
        if heal == 'I\'m fine..':
            pyautogui.press('f1')
        if not bool_dictionary['Cast spell or Heal']:
            break


def msgcheck():
    while bool_dictionary['MSGcheck']:
        current_chat = current_image(chat_area)
        searching_message = cv2.imread('window_references/msgcheck.png')
        template = cv2.matchTemplate(current_chat, searching_message, cv2.TM_CCOEFF_NORMED)
        threshold = 0.95
        template_loc = np.where(template >= threshold)
        # print(template_loc[0], template_loc[1])
        if len(template_loc[0]) != 0:
            winsound.Beep(700, 500)
        if not bool_dictionary['MSGcheck']:
            break


def find_monster(monster):
    monster = monster.replace(' ', '_').lower()
    current_img = current_image(battle_list_area)
    enemy_img = cv2.imread(f'monsters/{monster}_unmarked.png')
    if_attack = cv2.imread(f'monsters/{monster}_marked.png')
    template_unmarked = cv2.matchTemplate(current_img, enemy_img, cv2.TM_CCOEFF_NORMED)
    template_marked = cv2.matchTemplate(current_img, if_attack, cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    loc_unmarked = np.where(template_unmarked >= threshold)
    loc_marked = np.where(template_marked >= threshold)
    # print(loc_unmarked[0], loc_unmarked[1])
    if len(loc_unmarked[0]) != 0 and len(loc_marked[0]) == 0:
        x_mouse, y_mouse = pyautogui.position()
        pyautogui.moveTo(loc_unmarked[1][0] + battle_list_area['left'],
                        loc_unmarked[0][0] + battle_list_area['top'] + 15, 0)
        pyautogui.click()
        pyautogui.moveTo(x_mouse, y_mouse, 0)
    monsters_dictionary['available'] = len(loc_unmarked[0])
    monsters_dictionary['attacked'] = len(loc_marked[0])


def check_hp(percent_hp, health_info):
    start_bar_x, start_bar_y = health_info[0:2]
    start_bar_x = int(start_bar_x + 4)
    start_bar_y = int(start_bar_y + 20)
    heal = autoit.pixel_get_color(int(start_bar_x + (int(percent_hp) / 100 * 181)), start_bar_y)

    # print(f'Heal percent:{percent_hp}, heal color: {heal}')
    time.sleep(random.uniform(0.2, 0.3))
    if heal != 4521796:
        pyautogui.press('f3')
        return 'Heal me!'
    else:
        return 'I\'m fine..'


def check_mana(percent_mana, health_info, title='None'):
    start_bar_x, start_bar_y = health_info[0:2]
    start_bar_x = int(start_bar_x + 4)
    start_bar_y = int(start_bar_y + 38)

    mana = autoit.pixel_get_color(int(start_bar_x + (int(percent_mana) / 100 * 181)), start_bar_y)
    # print(f'Mana percent:{percent_mana}, mana color: {mana}')
    if title == 'senzu':
        if mana != 4474111:
            pyautogui.press('f11')
            time.sleep(random.uniform(2.0, 2.1))
    else:
        if mana == 4474111:
            pyautogui.press('f12')
            time.sleep(random.uniform(0.4, 0.5))


#############################################################################################
def battle_list_area_func():
    while True:
        battle_info = pyautogui.locateOnScreen('window_references/battle_info.png')
        if battle_info is None:
            battle_list_backup = window_resolution_backup()
            for key in battle_list_area.keys():
                battle_list_area[key] = battle_list_backup[key]
        else:
            battle_list_area['left'] = int(battle_info[0])
            battle_list_area['top'] = int(battle_info[1])
            battle_list_area['width'] = 188
            battle_list_area['height'] = 900

        health_info = pyautogui.locateOnScreen('window_references/health_info.png')
        if health_info is None:
            health_info_area[0] = 0
            health_info_area[1] = 0
        else:
            health_info_area[0] = health_info[0]
            health_info_area[1] = health_info[1]

        minimap_info = pyautogui.locateOnScreen('window_references/minimap_info.png')
        if minimap_info is None:
            minimap_area_backup = window_resolution_backup()
            for key in minimap_area.keys():
                minimap_area[key] = minimap_area_backup[key]
        else:
            minimap_area['left'] = int(minimap_info[0])
            minimap_area['top'] = int(minimap_info[1])
            minimap_area['width'] = 188
            minimap_area['height'] = 900

        chat_info = pyautogui.locateOnScreen('window_references/chat_info.png')
        chat_end_info = pyautogui.locateOnScreen('window_references/chat_end_info.png')
        if chat_info is None or chat_end_info is None:
            chat_area_backup = window_resolution_backup()
            for key in chat_area.keys():
                chat_area[key] = chat_area_backup[key]
        else:
            chat_area['left'] = int(chat_info[0]) - 6
            chat_area['top'] = int(chat_info[1])
            chat_area['width'] = int(chat_end_info[0] + chat_end_info[3] - chat_info[0])
            chat_area['height'] = int(user32.GetSystemMetrics(1) - chat_info[1])


########################################################################################################

def window_resolution_backup():
    window_resolution = dict(
        left=0,
        top=0,
        width=user32.GetSystemMetrics(0),
        height=user32.GetSystemMetrics(1))
    return window_resolution
