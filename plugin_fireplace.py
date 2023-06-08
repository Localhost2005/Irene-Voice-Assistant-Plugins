# Камин на плеере Dune 
# author: Prokhorov Nikolay

import random
from vacore import VACore

# стартовая процедура
def start(core: VACore):
    manifest = { 
        'name': 'Плеер DUNE', 
        'version': '1.0',
        'require_online': False, 
        "description": """
Камин на плеере Dune. 
Голосовые команды: "включи камин, выключи камин". 
""",        

        'commands': {
            'включи камин' : play_dune,
            'выключи камин' : standby_dune,
            'стоп камин' : stop_dune,            
            }
    }
    return manifest

def play_dune(core: VACore, phrase: str):
    import requests
    res_str = requests.get("http://192.168.0.52/cgi-bin/do?cmd=start_playlist_playback&media_url=storage_name://usb_storage_0e2c_c182/fireplace.mp4&loop_mode=1")
    text = 'Камин включён '
    core.play_voice_assistant_speech(text)
    
def stop_dune(core: VACore, phrase: str):
    import requests
    res_str = requests.get("http://192.168.0.52/cgi-bin/do?cmd=main_screen")
    text = 'Воспроизведение Камина остановлено '
    core.play_voice_assistant_speech(text)     
    
def standby_dune(core: VACore, phrase: str):
    import requests
    res_str = requests.get("http://192.168.0.52/cgi-bin/do?cmd=standby")
    text = 'Камин выключен '
    core.play_voice_assistant_speech(text)    

