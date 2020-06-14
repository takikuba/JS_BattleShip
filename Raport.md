# BattleShip game raport. #
* * * 

Projekt w prosty sposób realizuję założenia projektowe:
+ Nie pozwala na ustawienie statku w niewłaściwy sposób.
+ Wymusza rozpoczęcie gry przed oddaniem strzału.
+ Wyświetla określone komunikaty.
+ Odpowiednio reaguje na przeprowadzone testy.
+ Kolorystyka odpowiedznia z założeniami.

#### Projekt zostawia miejsce na dalszy rozwój, w przyszłości planuje rozwój AI i wprowadzenie poziomów trudności.

Wykorzystane mechanizmy zostały opisane w dokumentacji.
W pliku Const.py znajdują się listy i stałe na których operuje program.

---
**Ciekawostki z tkintera:**
- [Messagebox](https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L12) - Prosty mechanizmu nowego okna zawierającego informację. Możemy go wykorzystać jako np. showwarning lub showinfo.
A prosta rozbudowa daje możliwośc pobrania odpowedzi z przycisków okna.
- [Place in grid](https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L410) - upraszcza rozmieszczenie elementów.
---

W kodzie unikałem występowania redundancji kodu przez co występuje więcej funkcji opowiedzialnych za przeprowadzenie małych działań jak np: [placeShip1](https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L251) lub [placeShip3](https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L273)

*Projekt BattleShip pozwolił na zapoznanie się z biblioteką Tkintera na trochę wyższym poziomie. Prosta gra pozwoliła na zapoznanie się z mechanizmami tej bibioteki jak i języka Python, takimi jak:*

* Wyrażenia lambda: 
* * https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L409
* * https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L421
* * https://github.com/takikuba/JS_BattleShip/blob/6e6c90f8064931a81c4a60cce9b18fc30054ab08/src/Game.py#L403
* List comprehensions:
* * https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L354
* * https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L372
* * https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L317

* Klasa:
* * https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L7

* Zmienne globalne:
* * https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L334
* * https://github.com/takikuba/JS_BattleShip/blob/cc565aac88ba11cb5ed4bdbe9874b6e2815937cd/src/Game.py#L168
* Całość projektu:
* * https://github.com/takikuba/JS_BattleShip