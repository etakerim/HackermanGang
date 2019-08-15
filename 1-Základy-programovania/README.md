## Zbierka úloh z programovania v Pythone

**Kurz**: Základy programovania

**Autor**: Miroslav Hájek

**Licencia:** CC-BY-SA (2019)

____

### Obsah

* [Predslov](#predslov)
* [I. Premenné](#i-premenn-)
* [Ⅱ. Podmienky](#--podmienky)
* [Ⅲ. Cykly](#--cykly)
* [Ⅳ. Náhodné čísla](#--n-hodn----sla)
* [Ⅴ. Reťazce a zoznamy](#--re-azce-a-zoznamy)
* [Ⅵ. Súbory](#--s-bory)
* [Ⅶ. Funkcie](#--funkcie)
* [Zdroje a literatúra](#zdroje-a-literat-ra)

_________

### Predslov



Každý je raz na začiatku a stojí pred výzvou ako zvládnuť kostrbatú cestu, ktorá ho čaká. Programovanie nie je v tomto ohľade výnimkou. Vedieť požiadať neživý predmet, počítač, aby spravil to, čo od neho chceme, stojí nemalé úsilie. Často sa pri tom zasekneme na rôznych chybách objavujúcich sa medzi zadaním a riešením problému. Zo začiatku si prejdeme cez množstvo vzájomných nedorozumení. Rečou stroja sú totiž mystické sekvencie binárnych čísel. Ľudia našťastie vymysleli programovacíe jazyky, vďaka ktorým sa dokážeme lepšie pochopiť. Naučiť sa plynulo rozprávať s týmto cudzincom si aj napriek tomu vyžaduje veľa času a hlavne neustáleho prekonávania nových výziev.

​	Táto zbierka úloh si kladie za cieľ byť tvojim spoločníkom tŕnistým chodníkom pralesom kódu od prvých pozdravov až k rozsiahlym esejám. Umenie textov nebude spočívať v rýmoch básne, ale presnej a usporiadanej logickej štruktúre. Naša činnosť bude podobná tej, ako keď kuchár objaví chutnú kombináciu ingrediencií, ktoré dá dokopy presným postupom a následne svoje majstrovstvo premení do receptu, aby si nové unikátne jedlo mohli uvariť a vychutnať všetci.

​	Pri ochutnávke sveta softvéru prejdeme od priamej rady príkazov, cez rozhodnutia, spracovania množstva údajov v cykloch, až po využívanie súborov na ukladanie celých databáz. Našimi ingredieciami budú dáta a postupom algoritmy, alebo teda programy. Nezaháľajme teda a vydajme sa na púť.

— Autor



> "The psychological profiling [of a programmer] is mostly the ability to shift levels of abstraction, from low level to high level. To see something in the small and to see something in the large."
> — Donald Knuth



____

### I. Premenné



**Premenná** je ako krabička slúžiaca na odkladanie informácií, ktoré si potrebujeme pre vykonanie danej činnosti zapamätať. Podľa účelu sa líšia svojim *dátovým typom*, ktorý sa vytvorí, keď do premennej niečo vložíme (*priradenie*) a určuje to, čo sa vo vnútri nachádza. 

Základné stavebné kamene, z ktorých vyskladáme opis zložitejších javov sú:

* **Logická hodnota** (*bool*) - Boolean môže mať len dve hodnoty - pravda (*True*) alebo nepravda (*False*)

* **Celé číslo** (*int*) - Do integer-u ukladáme ľubovolné kladné a záporné celé čísla (napr. *97*)

* **Desatinné číslo** (*float*) - Líšia sa od celých čísel spôsobom uloženia (napr. *3.14159*)

* **Reťazec** (*str*) - Označujeme ich úvodzovkami alebo apostrofmi a väčšinou predstavujú text napísaný na klávesnici alebo zobrazený na obrazovke. (napr. *"Učím sa programovať!"*)

  

**Cvičenia:**

1. **Pozdrav** - Vytvor program, ktorý ťa po vložení mena pozdraví.  Zameň pozdrav a zároveň nechaj program sa rozlučiť.

   ```
   Ako sa voláš?: ______
   Ahoj ______
   ```

   

2. **Básnik** - Vytváraš básničky na počkanie. Dnes sa ti ťažko premýšľa nad kreatívnymi textami, tak si chceš ušetriť námahu tým, že budeš meniť len rým.

   ```
   Napíš slovo, ktoré sa rýmuje so slovom strach: _____
   Tu je báseň:
   Z počítačov mával som vždy strach,
   teraz som však šťastný ako _____.
   ```

   

3. **Pozvánka** - Každému kamarátovi chceš poslať pozvánku na svoju narodeninovú oslavu. Okrem mena v správe potrebuješ meniť aj čas konania oslavy (nie všetci chodia načas), vec, ktorú priniesie a jedlo, ktoré bude mať prichystané. 

   ```
   Meno kamaráta: _____
   Čas oslavy: _____
   Prines: _____
   Jedlo: ______
   
   Ahoj _____,
   pozývam ťa na moju narodeninovú oslavu, ktorá sa bude konať 12.4. o _____. Nezabudni priniesť _____ a pekný darček. Na večeru ťa čaká _____ a samozrejme lahodná torta. Teším sa na teba! :)
   ```

   

4. **Prevod jednotiek teploty** - Si na návšteve v Amerike a keď ideš von nevieš ako sa máš obliecť, lebo na teplomere vidíš len stupne Fahrenheita. Premeň ich na stupne Celzia.

    ```
    Vonku je °F: _____
    Doma by to bolo _____°C.
    ```

    

5. **Cesta autom** - Plánuješ trasu na výlet autom a chceš zistiť akou rýchlosťou musíte priemerne ísť, aby ste stihli navštíviť všetky miesta a prišli večer včas do hotela.  

    ```
    Dĺžka cesty (km): ____
    Odchod z domu (hodina): ____
    Príchod do hotela (hodina): ____
    
    Pôjdete priemerne ____ km/h.
    ```

    

6. **Kúpalisko** - Začína sa letná sezóna a prevádzka kúpaliska musí pred otvorením plne napustiť bazény v areáli. Všetky sú kvádrového tvaru a poznáme ich rozmery. Zaujíma nás spotrebovaná voda na konkrétny bazén a cena, ktorú za ňu zaplatíme.

    ```
    Dĺžka bazéna (m): ____
    Šírka bazéna (m): ____
    Hĺbka bazéna (m): ____
    Hĺbka hladiny od okraja (cm): ____
    Cena za m³ vody v €: _____
    
    Na bazén sa minie ____ litrov vody a bude to stáť ____ €.
    ```

    

7. **Maľovanie** - Sťahuješ sa s rodičmi do nového bytu a dali ti za úlohu vymalovať si izbu. Myslíš si, že nástroj na rýchle počítanie množstva farby by sa hodil aj profesionálnym maliarom, preto vytvoríš program na vypočítanie plochy stien a stropu bez okna a podlahy.

    ```
    Rozmery miestnosti
    Dĺžka (cm): ____
    Šírka (cm): ____
    Výška (cm): ____
    Rozmery okna
    Šírka (cm): ____
    Výška (cm): ____
    Výdatnosť farby (m²/kg): ____
    
    Maľovať budeš plochu ____ m². Kúp ____ kg farby. 
    ```

      

8. **Brzdenie** - V poslednej dobe je na trati viacej nebezpečných zrážok. Rušňovodiči ťa požiadali, aby si zistil ako rýchlo pred prekážkou dokáže vlaková súprava zastaviť pri danej rýchlosti.

    ```
    Vlaková súprava
    - Rýchlosť (km/h): ____
    - Hmotnosť lokomotívy (t): ____
    - Hmotnosť vagóna (t): ____
    - Počet vagónov: ____
    - Počet miest na vagón: ____
    - Zaplnenosť vlaku (%): ____
    - Brzdná sila (N/t): ____
    
    V rýchlosti ____ km/h zabrzdí súprava s hmotnosťou ____ t na vzdialnosť _____ m a bude to trvať ____ s.
    ```



___

### Ⅱ. Podmienky



**Podmienky** sú ako križovatky na ceste. Podľa toho kam chceme ísť, sa rozhodneme, ktorou cestou pôjdeme ďalej. Aby sme sa uistili, že máme ten správny smer (*vetva podmienky*) pýtame sa vždy logickú otázku pomocou už získaných údajov uložených v premenných.



**Cvičenia:**


1. **Heslo** - Tvoj dom na strome už vykradlo pár nezvaných návštevníkov a preto si vymyslel spôsob ako dovoliť návštevu len povoleným osobám, ktoré poznajú tajné heslo. 

    ```
    Stoj! Povedz Heslo!
    > _____
    
    Vstúp, priateľ /   Zmizni kade ľahšie 
    ```
    

    
2. **Najväčšie číslo** - Získaj tri čísla a zisti, ktoré z nich je najväčšie.

    ```
    1.číslo: ____
    2.číslo: ____
    3.číslo: ____
    
    Najväčie je ____.číslo a to je ____.
    ```

    

3. **Vhodné oblečenie** - Módny poradcovia vyšli z módy a ich prácu prebrali počítače. Na základe počasia a príležitosti odporúčajú vhodný outfit. Vymysli pár tipov pre rôzne situácie a začni radiť.

    ```
    Ako je vonku?: _____
    Kam ideš?: ____
    
    Určite si nezabudni _______ a tiež si vezmi _______.
    ```

    

4. **Pokazený rozpis** -  Podnik spracujúci rudu dostal časový rozpis trvania jednotlivých krokov vylepšeného technologického procesu. Činnosti zvyčajne trvajú dlhšie ako hodinu, nehodí sa im teda mať časy napísané iba ako údaj v minútach. Tvojou úlohou je rozpísať minúty na dni, hodiny, minúty pre jednoduchšie čítanie rozpisu. Vynechajte nepotrebné časové údaje.

     ```
      Trvanie (min.): ____
      = ___ d. ____ hod. ___ min
     ```

      

5. **Hovoriaca kalkulačka** - Výpočty neboli nikdy väčšia zábava, teda aspoň s kalkulačkou, ktorá namiesto čudných matematických znamienok hovorí ľudskou rečou. Vytvorte kalkulačku, ktorá si vypýta dve čísla a vie ich sčítať alebo odčítať.

     ```
     Som hovorica kalkulačka a rada počítam!
     Povedz mi prvé číslo: ____
     Potrebujem ďašie číslo: ____
     Chceš ich sčítať alebo odčítať: ____ (sčítať / odčítať)
     
     Výsledok tvojho príkladu: ____ plus/mínus _____ je ________. 
     ```

     

6. **Kvadratická rovnica** - Pre zadané koeficienty `a`, `b`, `c` kvadratickej rovnice `ax² + bx + c = 0`  vypočítajte jej korene v obore reálnych čísel a vrchol paraboly daného predpisu.

     *Pozri: [Wikipedia - Kvadratická rovnica](https://sk.wikipedia.org/wiki/Kvadratick%C3%A1_rovnica), [Wikipedia - Kvadratická funkcia](https://sk.wikipedia.org/wiki/Kvadratick%C3%A1_funkcia)*

     ```
     a = ____
     b = ____
     c = ____
     
     ___x² + ___x + ___ = 0
     x₁ = ____
     x₂ = ____
     V[___; ___]
     ```

     

7. **Trojuholníky** 

     *a)* Mýtická bytosť stredoškolskej matematiky, o ktorej je vždy treba zistiť, čo najviac bez rysovania, aj keď chýbajú rozmery. Ak je možné, doplň chýbajúce informácie pre ľubovoľný trojuholník (zadaný ako SSS) ako sú dĺžky strán a výšok, veľkosti uhlov, obsah a obvod. Využite trojuholníkoú nerovnosť, sínus(ovú) vetu, kosínus(ovú) vetu a vzorec na výpočet obsahu trojuholníkov. 

     *b)* Rozšírte vypočet aj pre ostatné vety o trojuholníkoch: SUS, USU, UUS

     *Pozri: [Wikipedia - Trojuholník](https://sk.wikipedia.org/wiki/Trojuholn%C3%ADk)*

     ```
     Zadajte strany ľubovolného trojuholníka:
     a = ___
     b = ___
     c = ___
     
     Strany: a = ___; b = ___; c = ___
     Uhly: 𝛂 = ___°; 𝛃 = ___°; 𝛄 = ___°
     Výšky: v(a) = ___; v(b) = ___; v(c) = ___
     O = ___
     S = ___
     Trojuholník je: ____, _____
     ```

     

___

### Ⅲ. Cykly



Obrovský potenciál počítačov tkvie v bezchybnom neúnavnom vykonávaní presne zadaných inštrukcií. Cykly umožňujú opakovať rovnaký postup ľubovoľný počet krát a tým efektívne odstraňovať rutinnú prácu.




1. **100-krát napíš** - Za vyrušovanie na hodinách sa stalo populárnym trestom ručné prepisovanie mravoučnej vety stokrát. Stalo sa to tak neznesiteľné, že si zhotovil robota, ktorý vie pomocť záškodníkom. Chýbajú mu len príkazy, čo má vlastne robiť.

     ```
     Musím napísať: _____
     Toľkoto krát: ____
     
     ______
     ______
     ...
     ```

     

2. **Hodnotenie** -  Filmový kritici a hodnotitelia reštauracií zapíšu po namáhavom dni číselné skóre k ich recenziam. Pre lepší efekt potrebujú vykresliť hviezdničky namiesto čísla. Pomôž im.

     ```
     Skóre: 5
     
     *****
     ```

     

3. **Pyramída** - Hviezdičky zoskup do tvaru pyramídy zadanej výšky.

     ```
     Výška pyramídy: 4
     
         *
        ***
       *****
      *******
     ```

     

4. **Smaragd** - Na pyramídu pripoj zo spodu ďaľšiu obrátene, aby vznikol smaragd z hviezdičiek.

     ```
     Veľkosť: 5
     
       *
      ***
     *****
      ***
       * 
     ```

     

5. **Duté vnútro** - Nakresli duté pyramídu a smaragd podľa prechádzajúcich úloh.

     ```
     Výška pyramídy: 4
     
         *
        * *
       *   *
      *******
     ```

     

6. **Mriežka slov** - Načítajte veľkosť tabuľky a slovo, ktoré sa v nej bude na každom riadku v stĺpci opakovať. 

     ```
     Počet riakov a stĺpcov: 4
     Opakovať slovo: ano
     
     ano ano ano ano
     ano ano ano ano
     ano ano ano ano
     ano ano ano ano
     ```

     

7. **Rám** - Prvý a posledný riadok a stĺpec bude tvoriť rám pre mriežku slov.

    ```
    Počet riakov a stĺpcov: 4
    Opakovať slovo: ano
    
    ### ### ### ###
    ### ano ano ###
    ### ano ano ###
    ### ### ### ###
    ```

    

8. **Malá násobilka** - K výbave každého žiaka základnej školy patrí tabuľky malej násobilky. Vytvor takúto tabuľku obsahujúcu každý násobok od 1x1 po 10x10, aby si pomohol všetkým malým matematikom.

     ```
       1   2   3   4   5   6   7   8   9  10 
       2   4   6   8  10  12  14  16  18  20 
       3   6   9  12  15  18  21  24  27  30 
       4   8  12  16  20  24  28  32  36  40 
       5  10  15  20  25  30  35  40  45  50 
       6  12  18  24  30  36  42  48  54  60 
       7  14  21  28  35  42  49  56  63  70 
       8  16  24  32  40  48  56  64  72  80 
       9  18  27  36  45  54  63  72  81  90 
      10  20  30  40  50  60  70  80  90 100 
     ```

     

9. **Sporenie** -  Na letnej brigáde si zarobil peniaze, ktoré chceš usporiť. Porovnáš ponuky bánk a hľadáš najvýhodnejší plán. Vytvor si sporiacu kalkulačku, ktorá na základe nemenného počiatčného vkladu, ročnej úrokovej sadzby, typu úročenia a žiadanej konečnej sumy, vypíše vývoj tvojich finančných prostriedkov do budúcnosti.

      ```
      Vklad v €: ____
      Úroková sadzba p.a. v %: _____
      Typ úročenia (jednoduché / zložené): _____
      Žiadaná suma v €:
      
      Rok				Suma         Úrok
          1.	        ______ €    _____ €
          2.	        ______ €    _____ €
      ....
      ```

      

___

### Ⅳ. Náhodné čísla



Pri tvorbe simulácií sú náhodné čísla nepostrádateľné. Umožňujú vniesť variabilitu a rôznorodosť do inak statických scén. Nesmierne poslúžia v hrách, kde dovoľujú modelovať napríklad pravdepodobnosť výskytu monštier, či pokladov.




1. **Hádzanie kockou** - Vytvorte simuláciu hodu kockou. Po stlačení klávesy Enter sa nakreslí kocka s padnutým číslom.

     ```
     HOĎ<ENTER>
     +-------+
     | #   # |
     |   #   |
     | #   # |
     +-------+
     ```

     

2. **Hádaj číslo** - Náhodne vyber číslo s rozsahu medzi 0 a 100 a nechaj hráča hádať dokým neuhádne. Pri tom mu poskytni nápovedy, či je jeho tip priveľa alebo primalo. Zakomponuj rôzne obtiažnosti s možnosťou nastavenia rozsahu alebo maximálnym počtom tipov.

     ```
     Hádaj číslo: 8
     Málo
     Hádaj číslo: 18
     Veľa
     Hádaj číslo: 13
     Výborne. Uhádol si!
     ```

     

3. **Opakovanie násobilky** - Vďaka tvojej tabuľke malej násobilky sa malý školáci mohli naučiť násobiť. Ako dobre to vedia, musíš teraz odtestovať. Vygeneruj dve čísla od 1 do 10 do príkladu na násobenie. Over správnosť žiačikovej odpovede.

     ```
     Koľko je ____ x _____?
     = _____
     Správne - len tak ďalej / Nesprávne - hádaj znovu
     Chceš ďalší príklad?
     ```



_____

### Ⅴ. Reťazce a zoznamy



**Zoznam** (tiež aj Pole) je množina údajov zaznamenaných spolu pod jedným menom. Každý údaj poľa sa nazýva *prvok* a poradie jeho pozície sa nazýva *index*. **Reťazce** sa správajú podobne ako zoznamy, ale ich prvkami sú jednotlivé znaky.




1. **Vymeň písmeno** - Niekto ti posiela správy s diakritikou, ale po ceste sa vždy prekrúti jedno písmeno. Texty obsahujú aj pekné básne, ktoré si chceš vytlačiť a pripnúť na nástenku. Pokazený znak však kazí celkový dojem z diela. Zameň zadané chybné písmeno v celom reťazci.

   ```
   Správa: ________
   Za chybné písmeno: ____
   Vymeň: ____
   
   Opravené!
   __________
   ```

   

2. **Cenzúra** - Prišla tvrdá cenzúra s nariadením, že nikto už nesmie vidieť žiadnu samohlásku. Nahraď každý prečin vo vstupnom texte ľubovoľným iným špeciálnym znakom.

   ```
   Správa: Ja som tvoj kamarat
   Samohlásku nahraď: *
   
   Cenzurované: J* s*m tv*j k*m*r*t
   ```

   

3. **Počítanie slov** - Do redakcie miestnych novín chodia denno denne články, vtipy, poviedky a príbehy zo života od verných čitateľov. Aby mohli byť uverejnené potrebujú sa zmestiť do vyhradeného priestoru. Vypíš počet znakov, slov, viet a normostrán (*=1800 znakov*) pre rýchlejšie spracovanie textov.

   ```
   Článok: _________
   
   Znaky: ___
   Slová: ___
   Vety: ___
   Normostrany: ____
   ```

   

4. **Najdlhšie slovo** - Hra staršia ako ľudstvo samo. Debatný spolok usporiadal súťaž o nájdenie najdlhšieho slova, ktoré sa kedy vyskytlo v historických prejavoch. Zaujali ťa odmeny, ale nechce sa ti prehrabávať knižnicou starých záznamníkov a preto si prácu uľahčíš. Nájdi najdlhšie slovo v reťazci.

   ```
   Rečnícky prejav: ________
   
   Najdlhšie slovo v ňom: _____
   ```

   

5. **Frekvencia písmen** - Dlho do noci čítaš časopisy o umelej inteligencii a fascinuje ťa jej schopnosť rozprávať sa s človekom. Na vytvorenie viet na danú tému potrebuje mať prehľad o percentuálnom výskyte hlások v texte. Spočítaj a vypíš zoznam frekvencie písmen v reťazci.

   ```
   Článok: _______
   
   A: 23.2 %
   B: 11.5 %
   C: 8.9 %
   ...
   Z: 0.3 %
   ```

   

6. **Histogram** - Pri svojom predchádzajúceho pokuse s početnosťou písmen si všimneš, že každé ďaľšie písmeno v zozname sa oveľa menej objavuje ako očakávaš. Vykresli hviezdičky namiesto počtu percent a over si tak svoje pozorovanie graficky.

   ```
   Článok: _______
   
   A: ****
   E: *******
   I: ****
   ...
   X:*
   ```

   

7. **Nákupný košík** - Pri veľkých nákupoch sa často zíde prehľadný zoznam s tým, čo doma treba. Pýtaj si položky s ich cenami až kým sa nerozhodneš, že máš spísané všetko. Zobraz prehľadnú orámovanú tabuľku s údajmi podobne ako na pokladničom bločku (názov tovaru, DPH tovaru, cena tovaru s DPH, celková suma na zaplatenie).

   ```
     Čo kúpiť?: ______
     Cena ______?: _______
     ....
     
     +----------+--------+--------------+
     | Tovar    |  DPH   |  Cena s DPH  |
     +----------+--------+--------------+
     | Chlieb   |  0,20€ |      0,98 €  |
     +----------+--------+--------------+
     |    ...   |  ...   |     ...      |
     +----------+--------+--------------+
     | CELKOM   |  0,20€ |      0,98 €  |
     +----------+--------+--------------+
   ```

   

8. **Akronym** - SMS-ky rapídne zdraželi a napadlo ti, že bude lepšie posielať slovné spojenia ako skratky. Zo zadaných slov vytvor akronym. Vezmi začiatočné písmená každého slova a vytvor sktatku, ktorá bude pozostávať len z týchto písmen.

   ```
   Slovné spojenie: Slovenské národné divadlo
   
   Skratka: SND
   ```

   

9. **Veľa opakovania** - Roboti rozvážajúci pizzu po meste si zaznamenávajú zmenu smeru pre postupné vylepšovanie trás na lokality k častým zákazníkom. Keďže sa firme darí, prešli roboti už toľko, že sa im všetky záznamy o ich cestách nezmestia do pamäti. Všimneš si, že si značia každý krok a to vedie k častému opakovaniu. Nahraď postupnosť za sebou idúceho písmena, počtom výskytu a písmenom.  

   *Pozri: [Wikipedia - Run-length encoding](https://cs.wikipedia.org/wiki/Run-length_encoding)*

   ```
   Cesta robota: NNNNNNSSSSSSSSSSSWWWWNNN
   
   Skomprimované: 6N11S4W3N
   ```



____

### Ⅵ. Súbory



**Súbor** je zoskupením súvisiacich údajov, ktoré sú uložené na disku počítača. Oproti načítavaniu vstupu z klávesnice majú výhodu hlavne pri spracovaní a uchovaní veľkého množstva dát. Súbory sa dajú: *vytvoriť* / *vymazať*, *otvoriť / zatvoriť*, *čítať* / *zapisovať*. Podľa typu uchovávaných údajov (označované *príponou*)  súbory rozdeľujeme na:

* **Textové súbory ** - .txt, .csv, .html, .py

* **Obrazové súbory** - .bmp, .png, .jpg, .gif, .svg, .pdf

* **Zvukové súbory** - .wav, .mp3, .midi

* **Video súbory** - .avi, .mp4, .mkv

* **Spustiteľné súbory** - .exe, .elf

V tejto kapitole budeme pre jednoduchosť pracovať s textovými súbormi:




1. **Prepisovanie** - Pri prepisovaní dlhých textov na vstup programu sa často mýliš a príde ti to zbytočne zdĺhavé. Načítaj články u zadaní z predchádajúcej kapitoly zo súboru, ktorého názov si na začiatku vypýtaš. Pri úlohe "veľa opakovania" ulož záznam o ceste robota do nového súboru.

   

2. **Turistika** - Na víkend sa črtajú ideálne podmienky na horskú turistiku. Nenecháš nič na náhodu a pripravíš si detailný plán s výškovým profilom trasy. Na každých desať metrov trasy si do súboru poznačíš aktuálnu nadmorskú výšku. Zisti celkové stúpanie a klesanie počas celého výletu spolu s najvyššou a najnižšou nadmorskou výškou. Vypíš aj celkovú dĺžku túry v kilometroch a trvanie prechodu horami v hodinách.

   * *Vzorový obsah súboru (trasa.txt)*

     ```
     348
     351
     362
     369
     376
     379
     384
     395
     401
     396
     383
     381
     367
     361
     ```

   * *Turistika*:

     ```
     Výškový profil trasy je v súbore: ______
     
     Trasa: 0.140 km - 0 h 21 min
     Stúpanie: 53 m
     Klesanie: 40 m
     Najnižšie miesto trasy: 361 m
     Najvyššie miesto trasy: 401 m
     ```

   

3. **Vedomostný kvíz** - Bifľovanie ti vôbec nepríde ako zábava. Keby existoval spôsob, ktorým si opakovanie poznatkov spríjemniť. Včera si zo smútku nad vidinou takto premárneho času pri jedení čokolády a čipsov pozeral kvízovú reláciu. Prišlo ti to neuveriteľne poučné. Polož náhodnú otázku s možnostami zo súboru kvízových otázok a bodovo ohodnoť správnu odpoveď. Všetky kvízové otázky s možnosťami sa však nezmestia do pamäti programu, preto vždy vyber náhodnu otázku priamo zo súboru.

   - *Obsah súboru (kviz.txt):*

     ```
     Otázka: V ktorom roku sa začala Francúzska revolúcia?
     A: 1763
     B: 1813
     C: 1789
     D: 1654
     Odpoveď: C
     Otázka: Al₂O₃ je?
     A: hydroxid vápenatý
     B: oxid hlinitý
     C: hydroxid sodný
     Odpoveď: B
     ```

   - *Kvíz:*

     ```
     Súbor s kvízovými otázkami: kviz.txt
     Kvízové otázky pripravené.
     Ideme na to!
     
     V ktorom roku sa začala Francúzska revolúcia?
     A: 1763
     B: 1813
     C: 1789
     D: 1654
     Aká je správna odpoveď?: C
     Správne! Máš 1 bodov. / Nabudúce si to lepšie premysli. Skúsime niečo iné.
     ```

     

4. **Narodeniny** - Darčeky k narodeninám zvykneš kupovať na poslednú chvílu. Potrebuješ mať prehľad aspoň na mesiac dopredu, kto bude mať narodeniny, aby si stihol vybrať niečo výnimočné. Zo súboru načítaj ľudí, ktorí majú sviatok v požadovaný mesiac v roku.

   * *Obsah súboru (narodeniny.csv):*

     ```
     Jožko Mrkvička, 15.3.2002
     Katka Krátka, 2.7.1993
     Martinko Klingáč, 12.11.1995
     Iveta Novotná, 27.2.2001
     ...
     ```

   * *Oslavy:*

     ```
     Zobraz narodeniny pre mesiac v roku: 3.2019
     
     Narodeniny: Marec 2019
     15.3. - Jožko Mrkvička - 17 rokov
     ```

   

5. **Pripomienky v kalendári** - Po čase zistíš, že jednoduchšie by bolo, ak by sa ti týždeň pred kamarátovými narodeninami objavila pripomienka v tvojom osobnom elektronickom kalendári. Máš veľa kontaktov, nechceš ich však všetky prepisovať ručne. Zistiš, že zoznam narodenín môžeš do kalendárovej aplikácie vložiť vo formáte *iCalendar (.ics)*. Preveď súbor s menami a dátumami narodenia do tejto podoby.

   *Pozri:  [iCalendar - súborový formát](https://cs.wikipedia.org/wiki/ICalendar), [iCalendar - podrobný popis [EN]](https://icalendar.org/RFC-Specifications/iCalendar-RFC-5545/)*

   * *Pripomienky (narodeniny.ics)*

     ```
     BEGIN:VCALENDAR
     PRODID:Programatorsky kruzok
     VERSION:2.0
     ...
     BEGIN:VEVENT
     DTSTAMP:20190811T100534Z
     UID:1
     SUMMARY:Jožko Mrkvička narodeniny
     CATEGORIES:Narodeniny
     RRULE:FREQ=YEARLY
     DTSTART;VALUE=DATE:20020315
     DTEND;VALUE=DATE:20020316
     TRANSP:TRANSPARENT
     BEGIN:VALARM
     DESCRIPTION:
     ACTION:DISPLAY
     TRIGGER:-P7D
     END:VALARM
     END:VEVENT
     ...
     END:VCALENDAR
     ```

     

6. **Cestovné poriadky** - Z celoštátneho rýchlika prestupujú v okresných mestách cestujúci na miestne autobusy.  Podľa času odchodu a trvania cesty zisti, ktorý autobus stihnú a vypíš najbližší spoj s najmenším čakaním medzi vlakom a autobusom. Daj pozor, pretože prvý časový údaj v riadku s odchodmi autobusu je v skutočnosti trvanie cesty vlakom, kým sa dostaneš do stanice, odkiaľ odchádza ten autobus.

   * *Obsah súboru (cp.csv)*:

      ```
      vlak,9:15,10:45,12:15,14:30,16:15,18:20
      bus,1:00,11:00,13:00,15:00,17:00
      bus,1:45,9:30,12:08,16:33
      ...
      ```
      
   * *Cestovné poriadky:*

      ```
      Čas: 10:00
      Trvanie cesty vlakom: 1:00
      
      Najbližší spoje (vlak, autobus):
      12:15 - 13:15, 15:00 -
      ```
      
      

9. **Spisovateľ** - Každý nemôže mať doma vlastného Hviezdoslava. Nebolo by ale úžastné, keby si mohol tvoriť básne alebo prózu s podobným štýlom ako jeden z velikánov literatúry? Vzrušujúcejšie by bolo naučiť počítač umeleckému cíteniu. Najprv musíš zhromaždiť, čo najväčší počet ukážok tvorby autora, a tým zhromaždiť pravdepodobnosti následnosti *n-gramov* (písmen, slabík, slov) do *Markovovho reťazca*. Potom náhodne vygeneruj nový text v štýle autora. Žiaľ, vytvorené myšlienky zrejme nebudú dávať poväčšinou významovo zmysel.

   *Pozri: [Diela slovenskej literatúry](https://zlatyfond.sme.sk/), [Anglické texty](hhttps://archive.org/search.php?query=subject%3A%22Literature%22), [Markovov reťazec](https://cs.wikipedia.org/wiki/Markov%C5%AFv_%C5%99et%C4%9Bzec), [Stavové automaty vizuálne[EN]](http://setosa.io/ev/markov-chains/), [Tvorba slov pravdepodobnosťou - str.7[EN]](http://math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)*

   ```
   Chcem písať ako: Dostojevskij
   Dĺžka n-gramu: 2
   Počet znakov výsledného textu: 100 
   
   Spracúvam korpus tvorby autora ...
   Spočítavam maticu prechodových stavov ...
   Generujem originálny text ...
   Ani v tmi, že páliciu neď si predtým opohľadíka do do nia nehľadík, hľadal nediva ulic
   ```



____

### Ⅶ. Funkcie

**Funkcia** je pomenovaná časť programu, ktorá vykonáva špecifickú činnosť. Hovorí sa im preto tiež *procedúry* alebo *podprogramy*. Predstavuje súvislú časť kód, obsahujúcu sled na seba nadväzujúcich príkazov, tvoriacich jeden logický celok.  Takto umožňuje zložitejší program rozdeliť na viacero samostatných častí. 



1. **Vraky** - V šírich vodách Atlantiku sa stále ukrýka nepreberné bohatstvo vo vrakoch potopených lodí. V tejto minhre bude tvojou úlohou odkryť tajomstvo skrývajúce sa pod hladinou, nájdením parníku vytvoreného na náhodnej pozícii. Do programu napíš funkciu `vzdialenost(x, y)`, ktorá na základe zadaných súradníc vypočíta ako ďaleko si od vraku.

   ```
   Sonar hlási potopený parník na dohľad!
   Tvoje súradnice?: ___,___
   Od vraku si _____ námorných míľ.
   ...
   Našiel si vrak. Dobrá práca!
   ```

   

2. **Lietadlo** - Pilotov v kokpite lietadlo by počas letu zaujímalo, ako ďaleko sú ešte od prístatia. Zo zemepisných súradníc aktuálnej polohy a súradníc cieľa vypočíataj vo funkcii `letime(x, y)` najkratšiu vzdialenosť medzi týmito bodmi na sférickom povrchu zemegule.

   *Pozri: [Ortodróma[EN]](https://en.wikipedia.org/wiki/Great-circle_distance), [Príklad](https://www.aldebaran.cz/~brichnac/skola/ortodroma.pdf), [Kalkulačka](http://boulter.com/gps/distance/)*

   ```
   Pozícia: 42.990967 -71.463767
   Cieľ: 48.53682 -13.855231
   
   Vzdialenosť: 4416.21 km
   ```

   

3. **Cézarová šifra** - Pri tvojich cestách po lodných pokladoch ťa odpočúvajú piráti, ktorí ťa chcú predbehnúť a obohatiť sa. Na utajenie svojej polohy a správ s pevninou musíš svoje informácie šifrovať. Funkcia `sifruj(sprava, kluc)` zašifruje text správy tak, že posunie každé písmeno abecedy podľa písmena `kluc`, čiže napríklad správa "ABC" sa kľúčom "B" zmení na "BCD". Funkcia `desifruj(sifra, kluc)` bude fungovať spätne.  Pre lepšiu bezpečnosť podporuj aj dlhšie kľúče. Každé písmeno bude vyjadrovať posun od začiatku abecedy písmena, s ktorým sa stretne. Potom správa "AVE CEZAR" s kľúčom "BCD" bude "BXH DGCBT".

    

3. **Pascalov trojuholník** - Vytvorte funkciu `pascalov_trojuholnik(n)`, ktorá vypíšte súčtovú pyramídu s *n* riadkami, ktorá má po okrajoch jednotky a nasledujúce riadky sa tvoria ako súčet dvoch čísel v predchádzajúcom riadku.

   ```
   Počet riadkov: 5
   
       1
      1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1 
   ```

   

4. **Bublikové triedenie** - Pre prehľadnosť údajov je užitočné vedieť ich utriediť podľa rôznych kritérií. Napíš program, ktorý vypíše študentov zo súboru zoradených podľa zadaného názvu stĺpčeka vzostupne.  Na začiatok použi algoritmus bublinkového triedenia, neskôr proces zefektívni využitím algoritmom triedenia zlučovaním alebo rýchlym triedením.

   - *Obsah súboru (ziaci.csv):*

     ```
     meno, priezvisko, vek, datum narodenia, bydlisko, priemer, trieda
     Milan, Peterka, 15, 2004-09-18, Bratislava, 1.6, I.B.
     ...
     ```
   
     
   
6. **Štatistika** - Pre investora je dôležité poznať podmienky trhu a potenciálnu konkurenciu predtým, než si naplánuje stratégiu investovania. Rozbiehaš realitnú kanceláriu a skôr než nastaviš ceny pre konkrétne byty, zisti v akom vzťahu je výmera bytu k jeho cene v lokalite. Pre každú štatistickú funkciu si napíš zodpovedajúcu procedúru. Údaje o bytoch načítaj zo súboru.

   *Pozri: [Wikipedia - Štatistika](https://sk.wikipedia.org/wiki/Matematick%C3%A1_%C5%A1tatistika)*

   ```
   Súbor s bytmi v lokalite: ______
   
   					:	Cena (€):	Výmera(m^2)	:
   Priemer 			: 			:				:
   Medián				:			:				:
   Modus				:			:				:
   Smerodajná odchýlka :			:				:
   ```

   

7. **Rímske čísla** - Od archeológov si dostal dlhý zoznam rímskych čísel, ktoré boli nájdené v novobjavených podzemených historických pamiatkach. Tažko sa v nich dá vyznať a je na tebe, aby si ich premenil na "normálne" arabské čísla. Pre zhrnutie ti poslali aj zoznam pravidiel prevodu týchto číselných systémov. Napíš funkciu `rimske_na_arabske(rimske)`, ktorá premení rímske na arabské číslo.

   ```
   I = 1
   V = 5
   X = 10
   L = 50
   C = 100
   D = 500
   M = 1000
   ```

   

8. **Základný tvar zlomku** - Zlomky sú vhodné na presné výpočty s častami z celku. Vytvor jednoduchú kalkulačku, ktorá umožňuje dva zlomky sčítať, odčítať, násobiť a deliť. Výsledok vždy zjednoduš na základný tvar (*Euklidov algoritmus pre NSD a NSN*).

   ```
   Kalkulačka zlomkov
   a = 3/4
   b = 1/2
   Vypočítaj (+, -, *, /): +
   
   Výsledok:
   3/4 + 1/2 = 5/4
   ```

   

9. **Hra Poklad** - Povráva sa, že na strašidelnom hrade v Karpatoch je bludisko so siedmimi tajomnými komnatami. Každá má meno a je v nej truhlica s pokladom. Mapa bludiska je náhodne poskladaná, uložená v pamäti počítača, ale nie je nakreslená na obrazovke. Hráč musí zistiť, ako sú komnaty navzájom pospájané. Na začiatku hry sa ocitne v náhodne vybranej komnate. Jeho úlohou je zhromaždiť všetky truhlice v jednej komnate, pričom môže vykonať iba ohraničený počet krokov.

   * *Komnaty v mriežke s uloženým pokladom:*
     1. Purpurová a pekelná - Drahokamy
     2. Červená a čudná - Žuvačky
     3. Sivá a studená - Nanuky
     4. Žltá a žeravá - Zlatky
     5. Čierna a čarodejná - Smeti
     6. Hnedá a hrozivá - Kalkulačky
     7. Zelená a záhadná - Medeňáky
   * *Vzorová časť hrania hry:*

   ```
   Počítač rozumie týmto príkazom
   S, V, J, Z   : Pohyb na sever, východ, juh, západ
   ZDVIHNI		 : Zdvihne truhlicu
   POLOZ		 : Položí truhlicu
   KDE			 : Informuje o polohe truhlíc
   SOS			 : Vypíše pravidlá hry
   
   Si v 4.komnate
   Je žltá a žeravá
   Sú v nej: ZLATKY
   Čo chceš robiť?
   ? ZDVIHNI
   Zdvihol si truhlicu, v ktorej sú zlatky.
   
   Ešte stále si 4.komnate
   Čo chceš robiť?
   ? Z
   ...
   ```

   

10. **Databáza** - Na školu za siedmimi horami a dolinami si objednali počítač na uloženie a prehliadanie záznamov o študentoch. Keďže rok, čo rok odchádzajú maturanti a prichádzajú prváci, potrebujú tabuľky i upravovať. Napíš databázový systém, ktorý bude umožňovať vytvárať a mazať tabuľky, kde každá bude vo vlastnom csv súbore. Budú sa dať vkladať a mazať aj riadky, či upravovať jednotlivé políčka. Ulož do databázy napríklad aj informácie o knihách zo školskej knižnice.

    *Pre nápady na rozšírenie pozri: [Postavme si databázu[EN]](https://cstack.github.io/db_tutorial/)*

    * *Ukážka možností systému:*

       ```
       DATABÁZA> NOVÁ TABUĽKA žiaci: meno, priezvisko, dátum narodenia
       DATABÁZA> TABUĽKY
       žiaci
       DATABÁZA> OTVOR TABUĽKU žiaci
       ŽIACI> VLOŽ Ružena, Kvetinková, 1998-11-15
       ŽIACI> ZOBRAZ
         +----+---------+-------------+-----------------+
         | id |  meno   |  priezvisko | dátum narodenia |
         +----+---------+-------------+-----------------+
         | 1  |  Ružena | Kvetinková  |  1998-11-15     |
         +----+---------+-------------+-----------------+
       ŽIACI> UPRAV 1 NASTAV priezvisko: Sedmokrásková
       ŽIACI> ZOBRAZ: ZORAĎ PODĽA priezvisko
       ...
       ŽIACI> ZOBRAZ: HĽADAJ PODĽA priezvisko: Sedmokrásková
       ...
       ŽIACI> ZMAŽ 1
       ŽIACI> ZMAŽ TABUĽKU žiaci
       DATABÁZA> SKONČI
       ```

    

11. **Kalkulačka** - Moderné vedecké kalkulačky sú takmer zázrakom. Buď tým, že sa mimo akademickej pôdy skoro vôbec nepoužívajú, alebo samotnou zložitosťou ich fungovania. Dokážu rozlíšiť, či má prednosť násobenie alebo sčítanie, zatiaľ čo vezmú do úvahy zátvorky. Nemôže byť pre nich nič jednoduchšie ako prijsť na to, čo je číslo a čo operátor v dlhom posuvnom texte displeja. Vytvor program kalkuačky, ktorá sa bude správať ako vrecková vedecká kalkulačka (s infixovým zápisom).

    *Pozri: [Algoritmus posunovacej stanice[EN]](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)*

    ```
    > 5 * (1589 - 2 * 74) / 2 + (33 * 8)
    > 3866.5
    > ...
    ```

    

12. **Turingov stroj** - Turingov stroj dokáže simulovať chod ľubovoľného programu. Pozostáva z nekonečnej pásky rozdelenej na políčka, po ktorých chodí čítacia/zapisovacia hlava podľa zadaných inštrukcií. Načítaj príkazy pre turingov stroj zo súboru a každú sekundu zobraz aktuálny stav pásky a pozíciu hlavy.

    *Pozri: [Simulátor Turingovho stroja[EN]](https://turingmachinesimulator.com/)*
    
    * Formát príkazu
    
      ```
      [súčasný stav], [prečítaj symbol], [zapíš symbol], [pohyb hlavy], [nový stav]
      ```
    
      ```
      Špeciálna značka:
      _ = Prázdne políčko
      
      Pohyb hlavy:
      < = doľava
      > = doprava
      - = žiaden
      ```
    
    * Inštrukcie pre simulátor Turingovho stroja počítajúceho binárne čísla nahor.
    
      ```
      A, _, 0, -, B
      B, 0, 1, -, C
      B, 1, 0, <, B
      B, _, 1, -, C
      C, _, _, <, B
      C, 0, 0, >, C
      C, 1, 1, >, C
      ```
    
    * Simulácia:
    
      ```
      0
      ^
      1
      ^
      1
       ^
      1
      ^
       0
      ^
      10
      ^
      ...
      ```
    
    

___

### Zdroje a literatúra

< https://testovac.ksp.sk/tasks/ >, Korešpondenčný seminár programovania, Trojsten o.z., FMFI UK

< http://input.sk/ >,  RNDr. Andrej Blaho, PhD., FMFI UK

< http://www.programovanie.kromsat.sk/prog-b/index.htm >, Ing. Mária Hedvigová, SPŠE Prešov

TATCHELLOVÁ, Judy, BENNETT, Bill. *Skúsiš to s mikropočítačom? : poznávame a programujeme. Časť 1., Ako porozumieť mikropočítaču*. Bratislava : Mladé letá. 1990. 142 s. ISBN 80-06-00107-3.

WATTSOVÁ, Lisa, WATERS, Gaby. *Skúsiš programovať? : basic a strojový kód*. Bratislava : Mladé letá. 1991. 150 s. ISBN 80-06-00178-2.

TALLES, Matt. 2014. *Idiots Guide: Beginning Programming*. Dorling Kindersley, 2014. 416 p. ISBN 978-16-1564-505-3.

SUMMERFIELD, Mark. *Python 3 : Výukový kurz*. Brno : Computer Press. 2013. 584 s. ISBN 978-80-251-2737-7

SHIFFMAN, Daniel. *The Nature of Code: Simulating Natural Systems with Processing*. 2012. 520 p. ISBN 978-0985930806. URL: < https://natureofcode.com/book/ >

SWEIGART, Al.  *Invent Your Own Computer Games with Python*. No Starch Press. 2016. 376 p. ISBN 978-1593277956. URL: < http://inventwithpython.com/ >
