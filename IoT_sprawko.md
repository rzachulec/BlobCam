# Usługi i aplikacje Internetu Rzeczy - projekt
## Kamera z czujnikiem ruchu połączona z aplikacją mobilną

#### Aleksander Pajorski, Jan Narożny

### 1. Raspberry Pi

#### 1.1 Wymagane elementy

- Raspberry Pi
- Kompatybilna kamera (https://help.prusa3d.com/pl/article/camera-compatibility-rpi-prusalink_654918)
- Kompatybilny czujnik ruchu PIR

Raspberry Pi powinno być zaktualizowane do najnowszej dystrybucji Raspbian OS 'bookworm'. Należy wykonać 

    sudo apt update && sudo apt full-upgrade

aby upewnić się że bibloteki potrzebne do obsługi kamery są dostępne i aktualne.

#### 1.2 Podłączenie kamery i czujnika

Kamerę podączyć należy przy użyciu dedykowanego kabla oraz portu na płytce Pi. Kabel musi być dokładnie osadzony, częścią z kontaktami skierowany w przeciwnym kierunku niż zatrzask, a sam zatrzask równie dociśnięty. Czujnik ruchu podłączyć według poniższego schematu:

![Schemat podłączenia czujnika ruchu](https://projects-static.raspberrypi.org/projects/physical-computing/248971027a596f3437da45bafd2bd8a8cc35cb95/en/images/pir_wiring.png)

Czujnik ruchu posiada 3 piny: Vcc, Gnd, oraz Out. Powinne być one podpisane. Powyższy schemat jest poglądowy ponieważ w zależności od użytej wersji płytki ułożenie pinów GPIO może się różnić. Pin Vcc na czujniku podłączyć do pinu zasilającego 5V, pin Gnd do analogcznego pinu na płytce Pi, a Out do któregokolwiek z pinów GPIO. W tym przypadku użyty został pin 4. Do przetestowania podłączenia czujnika ruchu: 

#### 1.3 Stworzenie środowiska wirtualnego

    python3 -m venv venv

    # windows:
    venv\Scripts\activate

    # macOS i linux:
    source venv/scripts/activate

    pip install -r requirements.txt

#### 1.4 Weryfiakcja podłączenia kamery i czunika

Aby zweryfikować poprawne podłączenie czujnika:
    
    python3 pirTest.py

Zakończyć ctrl+c. Następnie aby zweryfikować podłączenie kamery:

    rpicam-still -n -o test.jpg

