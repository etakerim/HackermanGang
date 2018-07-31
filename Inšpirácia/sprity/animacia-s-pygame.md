## Animácia sekvencie obrázkov v Pythone

*Autor: Miroslav Hájek, 2018-07-31*

*Inšpirácia: Daniel Shiffman ([Video - Animated Sprites](https://thecodingtrain.com/CodingChallenges/111-animated-sprite.html))*

____________________________________________________________________________________________________________________________________________________________________________________________________

Pri tvorbe hier nám zvyčajne nestačia len čiary, kruhy a obdĺžniky, ale chceme použiť pripravené obrázky na otexturovanie vykreslovaných predmetov. Pokiaľ ide o zložitejšiu scénu potrebujeme tiež upravovať jej súčasti nezávisle na sebe. Použitým *spritov* (malé rastrové obrázky) môžeme napríklad animovať vodu, oheň, trávu, pohyby hráča a iných postáv.

Ukážeme si ako vytvoriť ilúziu bežiacich panáčikov. Najlepšie nám na tento účel poslúži programovací jazyk **Python** a balíček **pygame**. Návod ako všetko nainštalovať na svoj počítač nájdete na [webstránke pygamu](https://www.pygame.org/wiki/GettingStarted). 

____

#### Vytvorenie okna

Keďže pygame tvorí veľmi tenkú vrstvu nad grafických systémom počítača, používa sa niekedy ťažkopádne, ale časom si všimnete podobností a zapamätáte si dôležité funkcie, ktoré budete dookola používať. Najprv ukážem celý kód pre vytvorenie okna a potom si ho rozoberieme (Na miesta označené komentárom #číslo vložíme neskôr dalšie riadky súvisiace s animáciou):

```python
import pygame
import sys

WIDTH = 800
HEIGHT = 500
WHITE = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
#1
timer = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    window.fill(WHITE)
    #2
    pygame.display.update()
    timer.tick(30)
```



Uznávam, že na začiatok je toho poriadne veľa, ale poďme pekne postupne.

```python
import pygame
```

Povieme, že chceme použiť funkcie z pygamu v našom programe. Na prístup k veciam v balíčku musíme pristupovať cez bodku `pygame.NázovFunkcie` .

```python
WIDTH = 800
HEIGHT = 500
WHITE = (255, 255, 255)
```

Vytvoríme si [konštanty](https://cs.wikipedia.org/wiki/Konstanta): `WIDTH` a `HEIGHT` označujú výšku a šírku okna v pixeloch a `WHITE` je [RGB](https://sk.wikipedia.org/wiki/RGB) zápis bielej farby.

```python
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
```

Na začiatku programu si musí pygame nastaviť prostredie a potom vytvoríme grafické okno (`window`) so žiadúcim rozlíšením.

```python
timer = pygame.time.Clock()
```

Pripravíme si časovač, ktorý nám dovolí nastaviť stálu rýchlosť prekreslovania - [FPS](https://sk.wikipedia.org/wiki/Obrazov%C3%A1_frekvencia).

```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
```

Dostávame sa k začiatku [**herného cyklu**](https://gamedevelopment.tutsplus.com/articles/gamedev-glossary-what-is-the-game-loop--gamedev-2469). Pozostáva z dvoch častí. Aktuálne sa sústredíme na **spracovanie udalostí**. Pri kliknutí myšou, stlačení klávesy alebo v tomto prípade pri kliknutí na *zatvárací krížik okna* sa vytvorí udalosť, ktoré môžeme v prípade potreby spracovať. V tomto prípade ukončíme pygame a aj celý program.

```python
	window.fill(WHITE)
    # Tu patrí kód na kreslenie
    pygame.display.update()
    timer.tick(30)
```

Druhá časť cyklu (pozor stále odsadená tabulátorom!) sa stará o **kreslenie na obrazovku**. Medzi vymazaním okna na farbu pozadia (bielu) a poslaním zmien na obrazovku vložíme neskôr kreslenie spritu. Nakoniec nám časovač vytvorí také oneskorenie, aby sme mali 30 FPS medzi prekresleniami.

____

#### Načítanie obrázkov do zoznamu

[Obrázky bežiaceho panáčika](https://opengameart.org/content/stick-man-runner) som pre ľahšie načítanie poskladal do jedného obrázku (*sprite sheet*), podobajúceho sa na filmový pás (**Kód patrí do časti #1**)

![Sprite sheet][https://github.com/etakerim/HackermanGang/blob/master/In%C5%A1pir%C3%A1cia/sprity/stickmen.png] 



```python
FRAME_COUNT = 12
FRAME_WIDTH = 80
FRAME_HEIGHT = 100

spritesheet = pygame.image.load('stickmen.png').convert_alpha()
sx, sy, sw, sh = spritesheet.get_rect() 
```

Grafiku načítame zo súboru a spracujeme na rýchlejšie kreslenie pomocou `convert_alpha()`.  Ide o obrázok s rozmermi 960 x 100, kde je 12 snímok, každá s rozmermi 100 x 80.

Na rozkúskovanie snímkov animácie budeme potrebovať šírku, lepšie povedané dĺžku, celého "pásu" - `sw`. Žiaľ vieme získať len rozmery celého obrázka naraz, ostatné nás preto zatiaľ nebudú zaujímať. 

Poznačíme si aj počet snímkov animácie a rozmery snímku, aby sme nepoužívali nič nehovoriace čísla.

```python
window.blit(spritesheet, (0, 0))

for x in range(0, sw, FRAME_WIDTH):
    pygame.draw.line(window, (0, 0, 0), (x, 0), (x, FRAME_HEIGHT))
    # Kreslenie čiary: okno, čierna farba, začiatok a koniec (x, y)
    
pygame.display.update()
```

Tieto riadky vo výsledku nepoužijeme, ale poslúžia dobre na odtestovanie a ilustráciu rozsekávania. 

`blit` si môžete predstaviť, ako lepenie dvoch kúskov papiera na seba pri tvorení koláže. Na okno (výkres) nalepíme celý spritesheet (novinový ústrižok) na súradnice x = 0,  y = 0 . Bystrejší si všimnú, že sa nezmestí do okna, ale to nám momentálne neprekáža. Za každým snímkom nakreslíme čiernu vertkálnu čiaru oddelujúcu snímky. Takto si overíme, či ich môžeme rozdeliť, tak ako sme si mysleli. 

```python
animation = []

for x in range(0, sw, FRAME_WIDTH):
    frame = pygame.Surface((FRAME_WIDTH, FRAME_HEIGHT), pygame.SRCALPHA)    
    frame.blit(spritesheet, (0, 0), pygame.Rect(x, 0, FRAME_WIDTH, FRAME_HEIGHT))
    animation.append(frame)
```

V tejto časti si konečne načítame animáciu a uvedieme ju do pohybu. Začneme vytvorením zoznamu na snímky - `animation`. Vidíme tu presne rovnaký typ cyklu ako bol ten prechádzajúci. Vysvetlíme si podrobne jednotlivé kroky, ktoré vykonáva.

```python
frame = pygame.Surface((FRAME_WIDTH, FRAME_HEIGHT), pygame.SRCALPHA)
```

Jeden snímok (`frame`) bude predstavovať malý obrázok (v počítačovej grafike sa softvérovo vykreslované obrázky nazývajú `Surface`). Použitým `SRCALPHA` zachováme [priehľadnosť](https://www.quora.com/What-exactly-is-an-alpha-channel-in-an-image), aby za panáčikom neskončila veľká čierna plocha.

```python
frame.blit(spritesheet, (0, 0), pygame.Rect(x, 0, FRAME_WIDTH, FRAME_HEIGHT))
```

Tu použime `blit`  trochu inak ako predtým. Princíp však zostáva rovnaký. Zo "sprite sheetu" vyberieme menšiu oblasť snímku a prekopírujeme ju do premennej, kde bude vždy jedna snímka oddelená od ostatných.

```python
animation.append(frame)
```

Na záver zostáva vložiť oddelený snímok do zoznamu snímkov a toto spravíme aj pre všetky ostatné snímky.

V časti #1 máme teda nasledujúce príkazy na načítanie animácie zo súboru:

```python
FRAME_COUNT = 12
FRAME_WIDTH = 80
FRAME_HEIGHT = 100

spritesheet = pygame.image.load('stickmen.png').convert_alpha()
sx, sy, sw, sh = spritesheet.get_rect() 

animation = []

for x in range(0, sw, FRAME_WIDTH):
    frame = pygame.Surface((FRAME_WIDTH, FRAME_HEIGHT), pygame.SRCALPHA)    
    frame.blit(spritesheet, (0, 0), pygame.Rect(x, 0, FRAME_WIDTH, FRAME_HEIGHT))
    animation.append(frame)
```

____

#### Bežiaci panáčik ožíva

Nášho panáčika uvidíme bežať na mieste, keď pridáme nasledujúce:

```python
# Do časti #1:
index = 0
# Do časti #2
window.blit(animation[index], (0, 0))
index += 1
```

To hovorí, že do ľavého horného rohu umiestníme, to čo sa nachádza na aktuálnom políčku animácie, ktoré nám povie premenná `index`. V cykle ju preto zakaždým zväčšíme o 1, aby sme dostali vždy ďalšiu snímku. 

Keď však skusíme spustiť takýto program panáčik zmizne po zlomku sekundy alebo ho vôbec neuvidíme. Čo viac, vypľuvne to na nás chybu `IndexError: list index out of range`. Čo teraz? 

Animácia má len 12 snímkov a herný cyklus sa vykonáva 30-krát za sekundu, z toho vyplýva, že `i` bude za malú chvílu oveľa viac ako 12. Riešenie je zmeniť výpočet indexu nasledujúceho políčka. Naivne sa dá takto:

```python
index += 1
if index > len(animation):
    index = 0
```

Je to prehľadné a rýchle, čo môže postačovať, ale existuje ešte jeden elegantnejší spôsob. Uznávam, že trocha komplikovanejší:

```python
index = (index + 1) % len(animation)
```

Keď vezmeme zvyšok po delení vždy sa budeme točiť akokeby na hodinových ručičkách dookola. Vyberte si sympatickejší prístup.

___

#### Pohybujúce sa guličky

Vrátime sa k jednoduchšiemu príkladu guličky, ktorá sa posúva z horizontálne po obrazovke zľava doprava:

```python
# Pred herným cyklom
x = 0
# Animácia
pygame.draw.circle(window, color=(255, 0, 0), pos=(x, 100), radius=50)
x += 10    
```

Potom si niekto vymyslel, že by chcel tie guličky tri a napokon by bolo super, keby každá išla inou rýchlosťou.

```python
# Pred herným cyklom
x = 0
x1 = 0
x2 = 0
# Animácia
pygame.draw.circle(window, (255, 0, 0), (x, 100), 50)
pygame.draw.circle(window, (255, 0, 0), (x, 100), 50)
pygame.draw.circle(window, (255, 0, 0), (x, 100), 50)
x += 5 
x1 += 10
x2 += 15
```

Ako viete takéto opakovania sa dajú vyriešiť cyklom a zoznamom lôpt, ale my musíme do toho napasovať ešte snímky animácie, ktoré máme v ďalšom poli, a tiež rýchlosť ich premietania. Dostávame sa do situácie, kedy zoznamy prestávajú byť praktické. Naštastie aj na to sa myslelo a preto existujú spôsoby ako zlúčiť súvisiace premenné "pod jednu strechu".  

____

#### Sprite na znovupoužitie

Okrem toho môžeme neskôr chcieť načítať iné sprity a vytvoriť interakcie medzi nimi. V pythone slúžia na vytvorenie vlastných "bytostí" **triedy (class) **. Pozrime sa na to, čo má mať taký sprite.

##### Sprite 

* Pozícia na obrazovke - x, y
* Obrázok alebo snímky animácie - animation
* Aktuálny snímok animácie - index
* Rýchlosť zmeny (pohybu / animácie) - speed

**Trieda** nie je nič iné ako naša **predstava, o vlastnostiach a schopnostiach** vytváranej veci. Priblížme si to na príklade z bežného života. Popisujeme napríklad dom. Zaujímal by nás napríklad jeho typ (rodinný dom, panelák, ...), počet poschodí, adresa, mená jeho obyvateľov. Podstatné je, aby to stačilo pre náš program a nie sa snažiť zachytiť všetko z reálneho sveta.

**Konkrétny** dom sa nazýva **objekt**. Už nehovoríme o žiadaných vlastnostiach, ale o ich hodnotách. "Rodinný dvojposchodový dom na Zelenej ulici 23 v Mestečku obýva Janko a Katka."

Preveďme teraz náš rozbor spritu do pythonu:

```python
class Sprite:
	def __init__(self, x, y, speed, animation):
        self.x = x
        self.y = y
        self.speed = speed
        self.animation = animation
        self.index = 0
```

Vytvorili sme si triedu `Sprite`, ktorá pri tvorbe konkrétneho objektu potrebuje vedieť informácie súvisiace s jej polohou a vizuálnym znázornením. `__init__` predstavuje špeciálnu funkciu (v žargóne [OOP](https://sk.wikipedia.org/wiki/Objektovo_orientovan%C3%A9_programovanie): metódu), ktorú každá trieda, berúca hodnoty "zvonka", musí obsahovať.

Zložitejšie je porozumieť ako do toho zapadá `self` (v iných programovacích jazykov: `this`). Zastupuje objekt danej triedy (jedinca daného živočíšneho druhu), ktorý aktuálne vykonáva danú funkciu. Čiže na priblíženie: 

```python
# Vytvoríme dva objekty triedy (typu) Sprite
stickman = Sprite(0, 0, 0.8, animation)
stickwoman = Sprite(100, 0, 1, animation)
# Ešte sa nevedia nakresliť, ale pre ilustráciu
stickman.draw(window)       # self je stickman
stickwoman.draw(window)	    # self je stickwoman
```

____

Dokončime náš zámer a povedzme spritu ako sa má nakresliť.

```python
class Sprite:
    # ...
    def draw(self, window):
        i = int(self.index) % len(self.animation)
        window.blit(self.animation[i], (self.x, self.y))
```

Všimnite si, že všetky premenné, ktoré sme priradili pri vytváraní Spritu, voláme cez `self.`.  Ako ste zistili, je to preto, že každý objekt má tieto hodnoty iné (svoje vlastné).

```python
i = int(self.index) % len(self.animation)
```

Reálny index pre snímok animácie si vypočítame zvlášť, pretože ak sa panáčik pohybuje pomaly môže sa stať, že chceme ten istý obrázok zobraziť viackrát. Aby sa index a pozícia menili, tak dopíšeme do triedy sprite funkciu pre animovanie:

```python
def animate(self):
	self.index += self.speed
    self.x += self.speed * 5
    if self.x > WIDTH:
    	self.x = -FRAME_WIDTH   
```

Po prejdení za pravý okraj obrazovky sa panáčik objaví za ľavým okrajom a beží ďalej doprava. Okrem toho zväčšujeme x súradnicu o päť násobok rýchlosti.  Konštanta je zvolená z kozmetických dôvodov, aby rýchlosť behu vyzerala prirodzene k posunu doprava.

____

#### Šprint s vetrom o závod

Obráťme pozornosť späť k týmto príkazom v hlavnom programe:

```python
# Do časti #1:
index = 0
# Do časti #2
window.blit(animation[index], (0, 0))
index += 1
```

Vytvorme namiesto toho viacero animovaných panáčikov, ktorí medzi sebou budú závodiť. Potrebné ingrediencie sme si už napísali. V časti #1 vytvoríme skupinku bežcov, pričom každý bude mať inú rýchlosť a inú pozíciu na y osi.

```python
import random

runners = []
for y in range(0, sh, FRAME_HEIGHT):
    s = Sprite(0, y, random.random() + 0.5, animation)
    runners.append(s)
```

V časti #2 nám zostáva prekresliť animáciu každého z bežcov.

```python
for runner in runners:
    runner.draw(window)
    runner.animate()
```

____

#### Zapojte predstavivosť

Celý funkčný program nájdete na githube spolu s použitou grafikou, ktoré musíte umiestniť do jedného priečinka: [Odkaz na projektík](https://github.com/etakerim/HackermanGang/tree/master/In%C5%A1pir%C3%A1cia/sprity).

Skúste využiť znalosti, ktoré ste nadobudli čítaním tohto článku. Vytvorte si vlastnú minihru a  zakomponujte animované textúry, ktoré vylepšia vizuálnu kvalitu vášho diela.

![Bežíme!](https://github.com/etakerim/HackermanGang/blob/master/In%C5%A1pir%C3%A1cia/sprtty/animation.gif)

