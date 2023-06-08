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
