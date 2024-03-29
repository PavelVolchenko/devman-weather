# Прогноз погоды
Как быстро, удобно и без лишней информации узнать прогноз погоды? 
Например, с помощью скрипта.

## Необходимо
Установленный интерпретатор [Python](https://www.python.org/downloads/) и
библиотека [requests](https://pypi.org/project/requests/). Пример установки с помощью pip:
```
$ python -m pip install requests
```
## Как запустить
```
$ python main.py
```
## Результат
```
Лондон

       .-.      Drizzle and rain, light drizzle and rain
      (   ).    +13(11) °C     
     (___(__)   ← 8 м/c        
    ‚‘‚‘‚‘‚‘    3 км           
    ‚’‚’‚’‚’    1.8 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Ср. 18 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Местами неболь…│      .-.      Слабая морось  │
│     (   ).    +13(11) °C     │     (   ).    16 °C          │
│    (___(__)   ← 5-7 м/c      │    (___(__)   ↑ 9-13 м/c     │
│     ‘ ‘ ‘ ‘   9 км           │     ‘ ‘ ‘ ‘   2 км           │
│    ‘ ‘ ‘ ‘    0.8 мм | 60%   │    ‘ ‘ ‘ ‘    0.3 мм | 63%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Чт. 19 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │    \  /       Переменная обл…│
│   ,\_(   ).   16 °C          │  _ /"".-.     14 °C          │
│    /(___(__)  ↑ 4-6 м/c      │    \_(   ).   ↖ 2-3 м/c      │
│      ‘ ‘ ‘ ‘  10 км          │    /(___(__)  10 км          │
│     ‘ ‘ ‘ ‘   0.1 мм | 60%   │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пт. 20 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Умеренный дожд…│      .-.      Слабая морось  │
│     (   ).    +13(11) °C     │     (   ).    +11(10) °C     │
│    (___(__)   ↘ 4-6 м/c      │    (___(__)   ↘ 3-5 м/c      │
│   ‚‘‚‘‚‘‚‘    7 км           │     ‘ ‘ ‘ ‘   2 км           │
│   ‚’‚’‚’‚’    3.7 мм | 81%   │    ‘ ‘ ‘ ‘    0.5 мм | 78%   │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Череповец

     \  /       Переменная облачность
   _ /"".-.     +1(-2) °C      
     \_(   ).   → 2 м/c        
     /(___(__)  10 км          
                0.0 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Ср. 18 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Небольшой снег │               Облачно        │
│   ,\_(   ).   +4(-1) °C      │      .--.     +2(-2) °C      │
│    /(___(__)  → 5-6 м/c      │   .-(    ).   ↘ 3-4 м/c      │
│      *  *  *  10 км          │  (___.__)__)  10 км          │
│     *  *  *   0.0 мм | 62%   │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Чт. 19 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │  _`/"".-.     Небольшой снег │
│   ,\_(   ).   +4(2) °C       │   ,\_(   ).   +1(-3) °C      │
│    /(___(__)  ↓ 2 м/c        │    /(___(__)  ↙ 4-6 м/c      │
│      ‘ ‘ ‘ ‘  10 км          │      *  *  *  10 км          │
│     ‘ ‘ ‘ ‘   0.0 мм | 70%   │     *  *  *   0.0 мм | 74%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пт. 20 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│     \   /     Ясно           │
│  _ /"".-.     +3(-1) °C      │      .-.      -1(-5) °C      │
│    \_(   ).   ↙ 5-7 м/c      │   ― (   ) ―   ↙ 3-6 м/c      │
│    /(___(__)  10 км          │      `-’      10 км          │
│               0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Шереметьево

                Пасмурно
       .--.     +7(4) °C       
    .-(    ).   ↗ 5 м/c        
   (___.__)__)  10 км          
                0.0 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Ср. 18 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│  _`/"".-.     Местами дождь  │
│  _ /"".-.     +8(5) °C       │   ,\_(   ).   +7(4) °C       │
│    \_(   ).   → 8-9 м/c      │    /(___(__)  ↗ 5-7 м/c      │
│    /(___(__)  10 км          │      ‘ ‘ ‘ ‘  10 км          │
│               0.0 мм | 0%    │     ‘ ‘ ‘ ‘   0.0 мм | 66%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Чт. 19 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Облачно        │               Пасмурно       │
│      .--.     +8(5) °C       │      .--.     +5(3) °C       │
│   .-(    ).   ↗ 5-6 м/c      │   .-(    ).   ↗ 3-5 м/c      │
│  (___.__)__)  10 км          │  (___.__)__)  10 км          │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пт. 20 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Небольшой дожд…│      .-.      Небольшой дожд…│
│     (   ).    +6(2) °C       │     (   ).    +7(5) °C       │
│    (___(__)   ← 4-6 м/c      │    (___(__)   ← 3-4 м/c      │
│     ‘ ‘ ‘ ‘   9 км           │     ‘ ‘ ‘ ‘   9 км           │
│    ‘ ‘ ‘ ‘    1.1 мм | 82%   │    ‘ ‘ ‘ ‘    1.2 мм | 79%   │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

```