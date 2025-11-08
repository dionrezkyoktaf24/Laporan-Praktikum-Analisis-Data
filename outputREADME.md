Informasi Dataset:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 28 entries, 0 to 27
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Nama    28 non-null     object
 1   Mapel   28 non-null     object
 2   Nilai   28 non-null     int64 
dtypes: int64(1), object(2)
memory usage: 804.0+ bytes


5 Data Pertama:
   Nama             Mapel  Nilai
0   Ade  Bahasa Indonesia     87
1  Bara        Matematika     90
2  Aira  Bahasa Indonesia     88
3  Badi    Bahasa Inggris     78
4  Cyla    Bahasa Inggris     90


Statistik Deskriptif:
           Nilai
count  28.000000
mean   85.071429
std     8.985291
min    60.000000
25%    80.000000
50%    86.500000
75%    90.000000
max    98.000000


Statistik Nilai:
Rata-rata: 85.07142857142857
Median: 86.5
Modus: 90


Nilai Matematika:
      Nama       Mapel  Nilai
1     Bara  Matematika     90
5   Khansa  Matematika     98
7      Dwi  Matematika     70
23    Fara  Matematika     85


Nilai Bahasa Inggris:
     Nama           Mapel  Nilai
3    Badi  Bahasa Inggris     78
4    Cyla  Bahasa Inggris     90
6    Maya  Bahasa Inggris     85
27  Ahmad  Bahasa Inggris     95


Nilai Bahasa Indonesia:
     Nama             Mapel  Nilai
0     Ade  Bahasa Indonesia     87
2    Aira  Bahasa Indonesia     88
12   Agus  Bahasa Indonesia     87
13  Gilam  Bahasa Indonesia     75
25   Fani  Bahasa Indonesia     70
26   Lani  Bahasa Indonesia     60


Nilai Produktif:
      Nama      Mapel  Nilai
10    Mala  Produktif     80
15  Faizal  Produktif     80
16   Hanif  Produktif     90
17  Danish  Produktif     85
18  Darian  Produktif     85


Nilai Fisika:
      Nama   Mapel  Nilai
8     Raka  Fisika     95
9    Rasya  Fisika     90
11   Sania  Fisika     86
14    Rudi  Fisika     75
19  Evelyn  Fisika     90
20   Raina  Fisika     95
21     Ade  Fisika     90
22   Rasya  Fisika     85
24    Ryan  Fisika     98


Nilai Maksimum dan Minimum per Mata Pelajaran:
                  max  min
Mapel
Bahasa Indonesia   88   60
Bahasa Inggris     95   78
Fisika             98   75
Matematika         98   70
Produktif          90   80


![alt text](boxplot_nilai.png)
![alt text](distribusi_nilai.png)
![alt text](rata_rata_nilai.png)