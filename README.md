# Irene-Voice-Assistant Plugin
 
**plugin_fuzzy_thefuzz.py**

Плагин для метода нечеткого сравнения строк - модификация

Было res = fuzz.ratio(cmdsub,key)
Fuzz.ratio он сравнивает строку и оценку на основе того, насколько данная строка соответствует.

Стало res = fuzz.WRatio(cmdsub,key)
WRatio дает лучший результат, чем простое соотношение. Он обрабатывает нижний и верхний регистры, а также некоторые другие параметры.

Подробнее
https://maxbachmann.github.io/RapidFuzz/Usage/fuzz.html

**plugin_fireplace.py**

Плагин для воспроизведения видео камина на плеере Dune

Dune HD API
http://dune-hd.com/firmware/ip_control/dune_ip_control_overview.txt

**irene_plugin_fuzzy_ai_sentence**
https://github.com/janvarev/irene_plugin_fuzzy_ai_sentence

Установка без NVIDIA только CPU<br>
cd /opt/Irene-Voice-Assistant/plugins/
wget https://raw.githubusercontent.com/janvarev/irene_plugin_fuzzy_ai_sentence/main/plugin_fuzzy_ai_sentence.py
pip3 install torch==2.0.0+cpu torchvision==0.15.1+cpu torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cpu
pip3 install sentence-transformers
