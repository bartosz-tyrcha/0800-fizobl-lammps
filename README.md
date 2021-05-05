# 0800-fizobl-lammps

## Podstawy Fizyki Obliczeniowej (0800-fizobl)

### Projekt I.
### Bartosz Tyrcha



1. Wstęp

Celem projektu było przeprowadzenie symulacji dynamiki molekularnej
dla układu składającego się z pojedynczej molekuły NaCl w wodnym roztworze,
przy pomocy programu Lammps. 

Wynikiem symulacji w programie Lammps jest plik *out.dcd*.

Korzystając z pliku out.dcd oraz programu do wizualizacji VMD wygenerowana
została grafika przedstawiająca pojedynczą "ramkę" z symulacji układu 
(plik *nacl.dat.tga*).

Przy użyciu programu PLUMED na podstawie pliku *out.dcd* wygenerowany został 
plik *COLVAR-driver*, który zawiera wartości odległości pomiędzy atomami Na i Cl 
oraz liczby koordynacyjnej dla każdego kroku czasowego symulacji.

Na podstawie pliku *COLVAR-driver* zostały wygenerowane histogramy, wykresy 
energii swobodnej oraz wykresy zależności od czasu dla odległości Na-Cl, 
a także dla liczby koordynacyjnej, przy użyciu języka Python 
(skrypty *plot_histogram.py*, *plot_histogram_cord.py*, *plot_change_in_time.py*).



2. Odległość pomiędzy Na-Cl

Zależność odległości pomiędzy Na-Cl od czasu przedstawia wykres 
*dist_in_time.png*. Można zauważyć, że początkowo odległość ta wynosiła około 
0.3 nm, jednakże po niedługim czasie gwałtownie wzrosła. Przez większość czasu 
odległość Na i Cl oscylowała pomiędzy około 0.5 - 0.9 nm.

Utworzony histogram dla odległości zawarty jest w pliku *histogram_dist.png*.
Na jego podstawie można zauważyć, że najbardziej prawdopodobna odległość
pomiędzy Na i Cl w czasie trwania symulacji to około 0.55 nm. Mniej 
prawdopodobne lecz również częste były odległości z zakresu 0.7 - 0.8 nm. Można 
również zauważyć, że układ niechętnie przebywa w stanach gdzie odległości Na-Cl 
są około 0.4 nm.

Wykres energii swobodnej dla odległości Na-Cl zawarty jest w pliku 
*free_energy_dist.png*, na jego podstawie można zauważyć barierę występującą dla 
bliskich odległości Na-Cl (poniżej 0.3 nm). Jest ona związana 
z blisko-zasięgowym odpychaniem się atomów. Kolejna bariera znajduje się 
w okolicy 0.4 nm i jest to tzw. bariera dysocjacyjna. Pomiędzy pierwszą a drugą
barierą znajduje się minimum lokalne, które można powiązać ze stanem związanym
cząsteczki NaCl. Dla odległości znajdujących się za barierą dysocjacyjną 
znajduje się szeroki obszar kolejnego minimum lokalnego, można go powiązać 
ze zdysocjowanym stanem układu Na i Cl.



3. Liczba koordynacyjna

Zależność liczby koordynacyjnej od czasu przedstawia wykres w pliku 
*cord_in_time.png*, na jego podstawie można zauważyć, że w chili początkowej 
symulacji jej wartość wynosiła około 3. Następnie wartość ta szybko wzrosła
i przez większość czasu symulacji oscylowała w granicach 5 - 7.

Wygenerowany histogram dla liczby koordynacyjnej zawarty jest w pliku 
*histogram_cord.png*. Można zauważyć, że najbardziej prawdopodobną wartością 
liczby koordynacyjnej jest około 6. Natomiast drugą najbardziej prawdopodobną 
wartością jest w przybliżeniu 5.

Plik *free_energy_cord.png* przedstawia wykres energii swobodnej dla liczby 
koordynacyjnej. Można zauważyć na nim dla położone blisko siebie i oddzielone 
płytką barierą minima zlokalizowane w pobliżu wartości 5 oraz 6. Dla wartości 
liczby koordynacyjnej bliskich 4 można zauważyć kolejne, wysoko położone 
względem poprzednich, minimum lokalne. Oddzielone jest ono barierą, której 
najwyższy punkt znajduje się w okolicy wartości 4.5 dla liczby koordynacyjnej.





