# Плеере Dune 
# author: Prokhorov Nikolay
# author: Vladislav Janvarev

import subprocess
import requests
#from voiceassmain import play_voice_assistant_speech
from vacore import VACore


options = {}

# функция на старте
def start(core:VACore):
    manifest = {
        "name": "Dune управление плеером",
        "version": "1.0",
        "require_online": False,

        "description": """
        Проигрывание медиа через Dune HD из определенной папки (оффлайн).
        """,

        "options_label": {
            "player": "mpc-hc|dune Dune - по сети (поддерживается Dune HD Player)",
            "dune_ip": "Для DUNE - внутренний IP адрес",
            "dune_Path": "Сетевой путь до мультфильмов (нужен Dune HD). Например: smb://192.168.1.4/mults/",
        },

        "default_options": {
            "player": "dune",
            "dune_ip": "192.168.0.52",
            "dune_Path": "smb://192.168.0.206/upload/Prochor/video/",
        },

        "commands": {
            "включи плеер": run_player,
            "выключи плеер": standby_player,
            "стоп плеер": stop_player,
            "включи камин": fireplace_player,
        }
    }
    return manifest

def start_with_options(core:VACore, manifest:dict):
    print(manifest["options"])
    global options
    options = manifest["options"]
    return manifest

def run_player(core:VACore, phrase: str):
    if options["player"] == "dune":
        res_str = requests.get(f"http://{options.get('dune_ip')}/cgi-bin/do?cmd=main_screen")
        text = "Плеер включён "
        core.play_voice_assistant_speech(text)

def standby_player(core:VACore, phrase: str):
    if options["player"] == "dune":
        res_str = requests.get(f"http://{options.get('dune_ip')}/cgi-bin/do?cmd=standby")
        text = "Плеер выключен "
        core.play_voice_assistant_speech(text)

def stop_player(core:VACore, phrase: str):
    if options["player"] == "dune":
        res_str = requests.get(f"http://{options.get('dune_ip')}/cgi-bin/do?cmd=main_screen")
        text = "Воспроизведение остановлено "
        core.play_voice_assistant_speech(text)

def fireplace_player(core:VACore, phrase: str):
    if options["player"] == "dune":
        res_str = requests.get(f"http://{options.get('dune_ip')}/cgi-bin/do?cmd=start_file_playback&media_url={options.get('dune_Path')}fireplace.mp4")
        text = "Камин включен "
        core.play_voice_assistant_speech(text)