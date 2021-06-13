from dearpygui.core import *
from dearpygui.simple import *
import webbrowser
import linecache as lc
import pyautogui
import pydirectinput
from pynput.keyboard import Listener
import keyboard


keylist = ['W', 'R', 'O']
gamemodelist = ['Survival', 'Hardcore', 'Creative']
difficultylist = ['Easy', 'Normal', 'Hard', 'Peaceful']

def githubpydirectinpute():
    webbrowser.open('https://github.com/GlitchleX/MCSeedReroller')

def macro():
    xp = int(lc.getline('config.txt', 9).strip())
    yp = int(lc.getline('config.txt', 10).strip())
    pydirectinput.click(x = xp, y = yp, button = 'left')
    pydirectinput.click(button = 'left')

    xp = int(lc.getline('config.txt', 13).strip())
    yp = int(lc.getline('config.txt', 14).strip())
    pydirectinput.click(x = xp, y = yp, button = 'left')

    xp = int(lc.getline('config.txt', 17).strip())
    yp = int(lc.getline('config.txt', 18).strip())
    if str(gamemodelist[get_value('gamemode')]) == 'Hardcore':
        pydirectinput.click(x = xp, y = yp, button = 'left')
    if str(gamemodelist[get_value('gamemode')]) == 'Creative':
        pydirectinput.click(x = xp, y = yp, button = 'left')
        pydirectinput.click()

    xp = int(lc.getline('config.txt', 21).strip())
    yp = int(lc.getline('config.txt', 22).strip())
    if str(difficultylist[get_value('difficulty')]) == 'Peaceful':
        for n in range(2):
            pydirectinput.click(x = xp, y = yp, button = 'left')
    if str(difficultylist[get_value('difficulty')]) == 'Easy':
        for n in range(3):
            pydirectinput.click(x = xp, y = yp, button = 'left')
    if str(difficultylist[get_value('difficulty')]) == 'Hard':
        pydirectinput.click(x = xp, y = yp, button = 'left')

    xp = int(lc.getline('config.txt', 25).strip())
    yp = int(lc.getline('config.txt', 26).strip())
    pydirectinput.click(x = xp, y = yp, button = 'left')

    xp = int(lc.getline('config.txt', 29).strip())
    yp = int(lc.getline('config.txt', 30).strip())
    pydirectinput.click(x = xp, y = yp, button = 'left')
    if str(get_value('ssgseed')) == 'True':
        pyautogui.write('2483313382402348964', _pause=False)
    if str(get_value('ssgseed')) == 'False':
        pyautogui.write(get_value('seed'))
    
    xp = int(lc.getline('config.txt', 33).strip())
    yp = int(lc.getline('config.txt', 34).strip())
    pydirectinput.click(x = xp, y = yp, button = 'left')

def toggle():
    while str(get_value('hotkeytoggle')) == 'True':
        if str(keylist[get_value('keybind')]) == 'W':
            if keyboard.is_pressed('Alt + W'):
                macro()
                break
        if str(keylist[get_value('keybind')]) == 'R':
            if keyboard.is_pressed('Alt + R'):
                macro()
                break
        if str(keylist[get_value('keybind')]) == 'O':
            if keyboard.is_pressed('Alt + O'):
                macro()
                break




with window('main'):
    add_additional_font('SourceHanSansK-Normal.otf', 20, 'korean')

    with tab_bar('tab1'):
        with tab(name = 'maintab', label = 'Main'):
            add_image(name = 'Logo', value = 'logo.png')
            add_spacing(count = 2)
            add_separator()
            add_spacing(count = 2)
            add_text('ChobojaX가 개발함')
            add_button(name='github', label='깃허브', callback = githubpydirectinpute)

        with tab(name = 'config', label = '설정'):
            add_spacing(count = 2)
            add_text(' -이 탭에서는 좌표에 대한 설정을 하지 못합니다. 좌표 설정은 config.txt 파일을 수정해 주세요')
            add_input_text(name = 'seed', label = '시드')
            add_checkbox(name = 'ssgseed', label = '2483313382402348964 시드 사용')
            add_spacing(count = 1)
            add_text('매크로 시작 키 (Alt키와 조합하여 사용)')
            add_radio_button(name = 'keybind', items = keylist)
            add_spacing(count = 1)
            add_text('게임모드 설정')
            add_radio_button(name = 'gamemode', items = gamemodelist)
            add_spacing(count = 1)
            add_text('난이도 설정')
            add_radio_button(name = 'difficulty', items = difficultylist)

        with tab(name = 'runtab', label = '실행'):
            add_spacing(count = 2)
            add_button(name = 'runmacro', label = '매크로 실행하기', callback = macro)
            add_spacing(count = 2)
            add_checkbox(name = 'hotkeytoggle', label = '단축키 활성화', callback = toggle)
            add_text('만약 키 설정을 바꾸셨다면\n이 버튼을 껏다 켜주셔야 합니다')

    set_main_window_size(820,600)
    set_primary_window('main', True)
    set_main_window_pos(200,200)
    set_main_window_resizable(True)
    set_main_window_title('Seed Reroller')

start_dearpygui()
