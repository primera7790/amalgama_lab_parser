# Парсер текста песен с переводом

## Используемые технологии:
  - Язык программирования: &nbsp; `python` ;
  - Основные библиотеки: &nbsp; `beautifulsoup4` , `requests` , `lxml` , `urllib3` .

## Описание:
  
  &nbsp; &nbsp; Парсинг текста песен с построчным переводом.<br>
  &nbsp; &nbsp; Указываем URL ссылку на страницу с интересующей композицией на сайте amalgama-lab.com.<br>
  &nbsp; &nbsp; Программа формирует csv-файл таким образом, что после каждой строчки на иностранном языке следует та же строчка на русском.<br>

## Инструкция по запуску:
1. Скачать/скопировать данные репозитория;
2. Установить зависимости, указанные в файле `requirements.txt` ;
3. Запустить файл `health_diet_parser.py` .
  
## Нагляднее:

### Текст композиции на сайте:
<p>
  <img width='800px' src='https://github.com/primera7790/amalgama_lab_parser/blob/main/data/images/website_text.PNG' alt='website_text'/>
</p>

### Консоль при исполнении:
<p>
  <img width='800px' src='https://github.com/primera7790/amalgama_lab_parser/blob/main/data/images/process.PNG' alt='process'/>
</p>

### Текст в результирующем csv-файле:
<p>
  <img width='400px' src='https://github.com/primera7790/amalgama_lab_parser/blob/main/data/images/final_text.PNG' alt='result'/>
</p>
