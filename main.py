import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from prettytable import PrettyTable

tbJudul = PrettyTable()
tbJudul.header = False
tbJudul.align = "l"
tbJudul.field_names = [""]
tbJudul.add_row(["Hello, "])
tbJudul.add_row(["Selamat Datang di Dashboard IMDB"])
tbJudul.add_row([">NIM  : 2111601296"])
tbJudul.add_row([">Nama : Reza Ariftiarno"])
print(tbJudul)


# Fungsi Menu 
def menu():
    print("MENU")
    print("[1] Genre")
    print("[2] Color")
    print("[3] Bahasa")
    print("[4] Negara")
    print("[5] Total Film")
    print("[6] Bar Chart Rating")
    print("[7] Resume Gross dan Duration")
    print("[8] Query (Language dan Genre)")
menu()
df = pd.read_csv('imdb.csv')
universalInput = input("Input Pilihan: ")

def genre():
    if universalInput == "1":
        print("Jenis Genre terbagi ke dalam 17 Genre, yaitu: ")
        genre = df['Genre'].values
        genre2 = np.unique(genre)
        print(genre2)
genre()

def color():
    if universalInput == "2":
        print("Jenis Warna terbagi ke dalam 2 Jenis Warna, yaitu: ")
        color = df['Color/B&W'].values
        color2 = np.unique(color)
        print(color2)
color()

def language():
    if universalInput == "3":
        df['Language'] = df['Language'].astype(str)
        language = df['Language'].values
        language2 = np.unique(language)
        print(f"Dataset IMDB saat ini terdiri dari {len(language2)} Bahasa")
language()

def country():
    if universalInput == "4":
        df['Country'] = df['Country'].astype(str)
        country = df['Country'].values
        country2 = np.unique(country)
        print(f"Terdapat {len(country2)} Negara dalam Dataset IMDB")
country()

def movieCount():
    if universalInput == "5":
        movieCount = df['Title'].values
        print(f"Dataset IMDB saat ini memiliki {len(movieCount)} Film")
movieCount()

def chart():
    if universalInput == "6":
        chart = df['Rating'].astype(str)
        plt.title('Film berdasarkan Rating')
        plt.hist(chart, 20, color="blue", edgecolor = 'black')
        plt.ylabel('Title')
        plt.show()
chart()

def randg():
    if universalInput == "7":
        grossRaw = df['Gross Revenue']
        gSum = grossRaw.sum()
        gMax = grossRaw.max()
        gMin = grossRaw.min()
        durationRaw = df['Duration (min)']
        dSum = durationRaw.sum()
        dMax = durationRaw.max()
        dMin = durationRaw.min()
        dLen = len(durationRaw)
        print("Gross Revenue Resume")
        print("=====================")
        print(f"Total       : $ {gSum}")
        print(f"Rata-rata   : $ {gSum/len(grossRaw)}")
        print(f"Terendah    : $ {gMin}")
        print(f"Tertinggi   : $ {gMax}")
        print("")
        print("Duration Resume")
        print("=====================")
        print(f"Total       : $ {dSum} Menit")
        print(f"Rata-rata   : $ {dSum/dLen} Menit")
        print(f"Terendah    : $ {dMin} Menit")
        print(f"Tertinggi   : $ {dMax} Menit")
randg()

def query():
    if universalInput == "8":
        inputBahasa = input("Input Bahasa yang dicari: (Spasi untuk kembali ke menu) ")
        if inputBahasa == ' ':
            menu()
        else:
            bahasaDf = df[df.Language == inputBahasa]
            inputGenre = input("Genre ? ")
            genreDf = bahasaDf[bahasaDf.Genre == inputGenre]
            durationRaw = genreDf['Duration (min)']
            dSum = durationRaw.sum()
            dMin = durationRaw.min()
            dMax = durationRaw.max()
            grossRaw = genreDf['Gross Revenue']
            gSum = grossRaw.sum()
            gMax = grossRaw.max()
            gMin = grossRaw.min()
            tampil = genreDf.head()
            print(tampil)
            print(f"Total Film Genre {inputGenre} dan {inputBahasa} adalah: {len(genreDf)} Film")
            print(f"Total Durasi        : {dSum} Menit")
            print(f"Rata-rata Durasi    : {dSum/len(durationRaw)} Menit")
            print(f"Durasi Terendah     : {dMin} Menit, Lead Actor: ")
            print(f"Durasi Tertinggi    : {dMax} Menit, Lead Actor: ")
            print("")
            print(f"Total Gross Revenue        : $ {gSum}")
            print(f"Rata-rata Gross Revenue    : $ {gSum/len(grossRaw)} Menit")
            print(f"Gross Revenue Terendah     : $ {gMin}, Lead Actor: ")
            print(f"Gross Revenue Tertinggi    : $ {gMax}, Lead Actor: ")
            query()
query()
