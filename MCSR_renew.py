from dearpygui.core import *
from dearpygui.dearpygui import *
from dearpygui.logger import *
import webbrowser
import linecache as lc
import pyautogui as pagman
import pydirectinput as pdi
import keyboard

#pyinstaller MCSR.py -F -w -i icon.ico

gamemodelist = ['Survival', 'Hardcore', 'Creative']
difficultylist = ['Easy', 'Normal', 'Hard', 'Peaceful']

pagman.PAUSE = 0.07
pdi.PAUSE = 0.07

def githubpdie():
    webbrowser.open('https://github.com/GlitchleX/MCSeedReroller')

def macro():
    pdi.press('tab')
    pdi.press('enter')
    pdi.press('tab', presses = 3)
    pdi.press('enter')
    pdi.press('tab')
    if str(get_value(2)) == 'Hardcore':
        pdi.press('enter')
    if str(get_value(2)) == 'Creative':
        pdi.press('enter')
        pdi.press('enter')
    pdi.press('tab')
    if str(get_value(3)) == 'Peaceful':
        pdi.press('enter', presses = 2)
    if str(get_value(3)) == 'Easy':
        pdi.press('enter', presses = 3)
    if str(get_value(3)) == 'Hard':
        pdi.press('enter')
    pdi.press('tab', presses = 4)
    pdi.press('enter')
    pdi.press('tab', presses = 3)
    if str(get_value(6)) == 'Use SSG 1.16.1 Seed':
        pagman.write('2483313382402348964')
    if str(get_value(6)) == 'Use Copied Text':
        pagman.hotkey('ctrl', 'c')
    if str(get_value(6)) == 'Use Custom/Random Seed':
        pagman.write(get_value(7))
    pdi.keyDown('shift')
    pdi.press('tab', presses = 2)
    pdi.keyUp('shift')
    pdi.press('enter')

def htoggle():
    if str(get_value(1)) == 'True':
        keyboard.add_hotkey(hotkey = 'f4', callback = macro)
    if str(get_value(1)) == 'False':
        keyboard.remove_hotkey(macro)

def customseed():
    if str(get_value(6)) == 'Use Custom/Random Seed':
        configure_item(7, enabled=True)        
    if str(get_value(6)) != 'Use Custom/Random Seed':
        configure_item(7, enabled=False)

def setmacrodelay():
    if str(get_value(5)) == 'False':
        print(str(get_value(4)))
    if str(get_value(5)) == 'True':
        if float(get_value(4)) < 0.07:
            set_value(item=4, value=0.07)
    pagman.PAUSE = float(get_value(4))
    pdi.PAUSE = float(get_value(4))

def toggledelay():
    if str(get_value(5)) == 'True':
        if float(get_value(4)) < 0.07:
            set_value(item = 4, value = 0.07)
    pagman.PAUSE = float(get_value(4))
    pdi.PAUSE = float(get_value(4))

viewport = create_viewport(title='MCSpeedRun Utility', width=900, height=600, resizable=False)

with font_registry():
    add_font('SourceHanSansK-Normal.otf', 20, default_font=True)

with window(label="main window", width=500, height=150, no_resize=True) as window1:
    with tab_bar(label='ajklfkwjfnjkwejfkwehjifukr'):
        with tab(label='Main'):
            add_text(default_value='This is MCSpeedRun Utility\nBut Nothing here')
        with tab(label='Auto Seed Reset'):
            add_text(' -No more mouse macro')
            add_spacing(count=2)
            add_separator()
            add_spacing(count=2)
            add_combo(id=6, label=6, width=400, items=['Use SSG 1.16.1 Seed', 'Use Copied Text', 'Use Custom/Random Seed'], default_value='Use SSG 1.16.1 Seed', callback=customseed)
            add_input_text(id=7, label='Set Seed by Input', width=400, enabled=False)
            add_spacing(count=2)
            add_separator()
            add_spacing(count=2)
            add_text('Difficulty Setting')
            add_radio_button(id=3, items=difficultylist, default_value='Easy')
            add_text('Gamemode Setting', pos=[212, 168])
            add_radio_button(id=2, items=gamemodelist, pos=[212, 198], default_value='Survival')
            add_spacing(count=2)
            add_separator()
            add_spacing(count=2)
            add_checkbox(id=1, label = 'Enable Hotkey', callback=htoggle)
            add_slider_float(id=4, width=200, format='%.2f', min_value=0, max_value=0.1, label='Input Delay', callback=setmacrodelay, default_value=0.07)
            add_checkbox(id=5, label='Enable Input Delay Limitter', default_value=True, callback=toggledelay)



set_primary_window(window1, True)
dpg.setup_dearpygui(viewport=viewport)
dpg.show_viewport(viewport)
dpg.start_dearpygui()
