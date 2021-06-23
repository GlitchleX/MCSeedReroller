from dearpygui.core import *
from dearpygui.simple import *
import webbrowser
import linecache as lc
import pyautogui as pagman
import pydirectinput as pdi
import keyboard
import time

keylist = ['F4', 'NumberKey 1', 'F']
gamemodelist = ['Survival', 'Hardcore', 'Creative']
difficultylist = ['Easy', 'Normal', 'Hard', 'Peaceful']
macrot = ['Mouse Macro', 'Keyboard Macro']

pagman.PAUSE = 0.02
pdi.PAUSE = 0.02

def githubpdie():
    webbrowser.open('https://github.com/GlitchleX/MCSeedReroller')

def macro():
    print('sans!')
    if str(macrot[get_value('macrotype')]) == 'Mouse Macro':
        print('more snas!')
        xp = int(lc.getline('config.txt', 9).strip())
        yp = int(lc.getline('config.txt', 10).strip())
        pdi.click(x = xp, y = yp, button = 'left')
        pdi.click(button = 'left')

        xp = int(lc.getline('config.txt', 13).strip())
        yp = int(lc.getline('config.txt', 14).strip())
        pdi.click(x = xp, y = yp, button = 'left')

        xp = int(lc.getline('config.txt', 17).strip())
        yp = int(lc.getline('config.txt', 18).strip())
        if str(gamemodelist[get_value('gamemode')]) == 'Hardcore':
            pdi.click(x = xp, y = yp, button = 'left')
        if str(gamemodelist[get_value('gamemode')]) == 'Creative':
            pdi.click(x = xp, y = yp, button = 'left')
            pdi.click()

        xp = int(lc.getline('config.txt', 21).strip())
        yp = int(lc.getline('config.txt', 22).strip())
        if str(difficultylist[get_value('difficulty')]) == 'Peaceful':
            for n in range(2):
                pdi.click(x = xp, y = yp, button = 'left')
        if str(difficultylist[get_value('difficulty')]) == 'Easy':
            for n in range(3):
                pdi.click(x = xp, y = yp, button = 'left')
        if str(difficultylist[get_value('difficulty')]) == 'Hard':
            pdi.click(x = xp, y = yp, button = 'left')

        xp = int(lc.getline('config.txt', 25).strip())
        yp = int(lc.getline('config.txt', 26).strip())
        pdi.click(x = xp, y = yp, button = 'left')

        xp = int(lc.getline('config.txt', 29).strip())
        yp = int(lc.getline('config.txt', 30).strip())
        pdi.click(x = xp, y = yp, button = 'left')
        if str(get_value('seedtype')) == 'Use SSG 1.16.1 Seed':
            pagman.write('2483313382402348964', _pause=False)
        if str(get_value('seedtype')) == 'Use Copied Text':
            pagman.hotkey('ctrl', 'c')
        if str(get_value('seedtype')) == 'Use Custom/Random Seed':
            pagman.write(get_value('custom_seed'))
        
        xp = int(lc.getline('config.txt', 33).strip())
        yp = int(lc.getline('config.txt', 34).strip())
        pdi.click(x = xp, y = yp, button = 'left')

    if str(macrot[get_value('macrotype')]) == 'Keyboard Macro':
        pdi.press('tab', _pause = False)
        pdi.press('enter', _pause = False)
        pdi.press('tab', _pause = False, presses = 3)
        pdi.press('enter', _pause = False)
        pdi.press('tab', _pause = False)
        if str(gamemodelist[get_value('gamemode')]) == 'Hardcore':
            pdi.press('enter', _pause = False)
        if str(gamemodelist[get_value('gamemode')]) == 'Creative':
            pdi.press('enter', _pause = False)
            pdi.press('enter', _pause = False)
        pdi.press('tab', _pause = False)
        if str(difficultylist[get_value('difficulty')]) == 'Peaceful':
            pdi.press('enter', _pause = False, presses = 2)
        if str(difficultylist[get_value('difficulty')]) == 'Easy':
            pdi.press('enter', _pause = False, presses = 3)
        if str(difficultylist[get_value('difficulty')]) == 'Hard':
            pdi.press('enter', _pause = False)
        pdi.press('tab', _pause = False, presses = 4)
        pdi.press('enter')
        pdi.press('tab', _pause = False, presses = 3)
        if str(get_value('seedtype')) == 'Use SSG 1.16.1 Seed':
            pagman.write('2483313382402348964', _pause=False)
        if str(get_value('seedtype')) == 'Use Copied Text':
            pagman.hotkey('ctrl', 'c')
        if str(get_value('seedtype')) == 'Use Custom/Random Seed':
            pagman.write(get_value('custom_seed'))
        pdi.keyDown('shift', _pause = False)
        pdi.press('tab', _pause = False, presses = 2)
        pdi.keyUp('shift', _pause = False)
        pdi.press('enter', _pause = False)

def htoggle():
    while str(get_value('hotkeytoggle')) == 'True':
        keyboard.wait(hotkey = 'f4', suppress=False)
        macro()
    if str(get_value('hotkeytoggle')) == 'False':
        pass


def customseed():
    if str(get_value('seedtype')) == 'Use Custom/Random Seed':
        configure_item('custom_seed', enabled=True)        
    if str(get_value('seedtype')) != 'Use Custom/Random Seed':
        configure_item('custom_seed', enabled=False)

def setmacrodelay():
    pagman.PAUSE = float(get_value('macrodelay'))
    pdi.PAUSE = float(get_value('macrodelay'))
    print(float(get_value('macrodelay')))

bgred = int(lc.getline('config.txt', 37).strip())
bggreen = int(lc.getline('config.txt', 38).strip())
bgblue = int(lc.getline('config.txt', 39).strip())
bgalpha = int(lc.getline('config.txt', 40).strip())

set_theme_item(mvGuiCol_WindowBg, bgred, bggreen, bgblue, bgalpha)

with window('main'):
    add_additional_font('SourceHanSansK-Normal.otf', 20, 'korean')
    with menu_bar(name = 'menubar'):
        with menu(name = 'menu1', label = 'Debug'):
            add_menu_item(name = 'm1item1', label = 'Show Logger', callback = lambda: show_logger())
            add_menu_item(name = 'm1item2', label = 'Show Theme Changer(Debug mode)', callback = lambda: show_style_editor())
            
        with menu(name = 'menu2', label = 'More'):
            add_menu_item(name = 'm2item1', label = 'Github Page', callback = githubpdie)
            
    add_spacing(count = 1)

    with tab_bar('tab1'):
        with tab(name = 'maintab', label = 'Main'):
            add_spacing(count = 2)
            add_same_line(xoffset = 35)
            add_image(name = 'Logo', value = 'logo.png')
            add_spacing(count = 2)
            add_separator()
            add_spacing(count = 2)
            add_text('Developed by ChobojaX')
            add_button(name='github', label='Github', callback = githubpdie)

        with tab(name = 'config', label = 'General Setting'):
            add_spacing(count = 2)
            add_text(' -This tab can`t change config, if you want to change config, edit config.txt file')
            add_combo(name = 'seedtype', items = ['Use SSG 1.16.1 Seed', 'Use Copied Text', 'Use Custom/Random Seed'], label = 'Seed Setting', default_value = 'Use SSG 1.16.1 Seed', callback = customseed)
            add_input_text(name = 'custom_seed', label = 'Set Custom Seed', hint = 'Keep it blank to use a random seed', enabled = False)
            add_spacing(count = 1)
            add_text('Macro hotkey')
            add_same_line()
            add_text(name = '(?)', tip = 'Disabled because i don`t want to see more bugs\nAlways Use "F4"')
            add_radio_button(name = 'keybind', items = keylist, horizontal=True, enabled = False)
            add_spacing(count = 1)
            add_text('Gamemode Setting')
            add_radio_button(name = 'gamemode', items = gamemodelist, horizontal=True)
            add_spacing(count = 1)
            add_text('Difficulty Setting')
            add_radio_button(name = 'difficulty', items = difficultylist, horizontal=True)

        with tab(name = 'macrotab', label = 'Macro Setting'):
            add_spacing(count = 2)
            add_checkbox(name = 'hotkeytoggle', label = 'Enable Hotkey', callback = htoggle)
            add_text('This option have a bug so if you enable this one time,\nhotkey will work while python cmd process is alive.\nand you can`t disable this if you don`t close this')
            add_spacing(count = 2)
            add_text('Macro Type')
            add_same_line()
            add_text(name = '(?)', tip = 'I rec')
            add_radio_button(name = 'macrotype', items = macrot, enabled = True, default_value=1)
            add_spacing(count = 2)
            add_text('PAUSE value')
            add_same_line()
            add_text(name = '(?)', tip = 'Small value will make macro VERY faster, but it can be buggy\nPyAutoGUI/PyDirectInput`s default value is 0.1\nEdit this before enable hotkey or value won`t be change')
            add_slider_float(name = 'macrodelay', label = '', min_value = 0, max_value = 0.1, default_value = 0.02, width = 200, format = '%.2f', callback = setmacrodelay)


    set_main_window_size(900,600)
    set_primary_window('main', True)
    set_main_window_pos(200,200)
    set_main_window_resizable(False)
    set_main_window_title('Seed Reroller')

start_dearpygui()

