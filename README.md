# PowerMode Switcher

## Описание

Скрипт помогает экономить энергию при автономной работе. Он включает режим экономии энергии, что немного снижает производительность, но позволяет продлить время работы ноутбука или системы с резервным питанием. Подходит пользователям, у которых есть источники бесперебойного или резервного питания и кто хочет снизить энергопотребление при работе от батареи.

## Как работает

Скрипт проверяет текущий режим питания и включает экономию энергии. В консоли выводится текущий режим и сообщение о переключении.

## Настройка

1. Установи Python 3.

2. Скопируй содержимое файла `power_mode.py` на свой компьютер.

3. Найди GUID схем питания:

   * Открой командную строку (Win + R → `cmd`)
   * Введи команду:

     ```
     powercfg /list
     ```
   * Скопируй GUID нужного режима, например:

     ```
     Сбалансированный: 381b4222-f694-41f0-9685-ff5bb260df2e  
     Энергосбережение: a1841308-3541-4fab-bc81-f71556f20b4a  
     Высокая производительность: 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c  
     ```

4. Внеси GUID в Python код:

   ```python
   GUIDS = {
       "energy_saver": "a1841308-3541-4fab-bc81-f71556f20b4a"
   }
   ```

   При желании можно добавить и другие режимы.

5. Чтобы изменить время показа консоли, найди строку:

   ```python
   time.sleep(3)
   ```

   и измени число на нужное количество секунд.

## Запуск

Дважды кликни по `power_mode.py` или запусти через терминал:

```
python power_mode.py
```

---

## English version

### Description

The script helps save power during battery or backup operation. It enables the power saving mode, slightly reducing performance but extending uptime. It’s useful for users with UPS or backup systems who want to lower power consumption.

### How it works

The script checks the current power plan and switches to the energy saver mode. It prints the current and new power mode in the console.

### Setup

1. Install Python 3.

2. Copy the `power_mode.py` file to your computer.

3. Find the power plan GUIDs:

   * Open Command Prompt (Win + R → `cmd`)
   * Run:

     ```
     powercfg /list
     ```
   * Copy the GUIDs you need, for example:

     ```
     Balanced: 381b4222-f694-41f0-9685-ff5bb260df2e  
     Power saver: a1841308-3541-4fab-bc81-f71556f20b4a  
     High performance: 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c  
     ```

4. Edit the GUID in the Python code:

   ```python
   GUIDS = {
       "energy_saver": "a1841308-3541-4fab-bc81-f71556f20b4a"
   }
   ```

   You can add more modes if needed.

5. To change how long the console stays open, modify:

   ```python
   time.sleep(3)
   ```

   Set any number of seconds you prefer.

### Run

Double-click `power_mode.py` or run it in the terminal:

```
python power_mode.py
```
