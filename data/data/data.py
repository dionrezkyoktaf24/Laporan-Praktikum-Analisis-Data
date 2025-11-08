# ==============================================
# Analisis Nilai Siswa
# by Dion 🧠
# ==============================================

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Gunakan backend non-interaktif agar tidak macet
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Membaca File CSV
# -------------------------------
file_path = r'C:\Users\MSII\OneDrive\Documents\Drive Besar SMK TELKOM\XI\data\nilai_siswa.csv'
data = pd.read_csv(file_path)

print("Informasi Dataset:")
data.info()
print("\n")

print("5 Data Pertama:")
print(data.head())
print("\n")

print("Statistik Deskriptif:")
print(data.describe())
print("\n")

# -------------------------------
# 2. Statistik Umum Nilai
# -------------------------------
print("Statistik Nilai:")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])
print("\n")

# -------------------------------
# 3. Filter Data per Mapel
# -------------------------------
print("Nilai Matematika:")
print(data[data['Mapel'] == 'Matematika'])
print("\n")

print("Nilai Bahasa Inggris:")
print(data[data['Mapel'] == 'Bahasa Inggris'])
print("\n")

print("Nilai Bahasa Indonesia:")
print(data[data['Mapel'] == 'Bahasa Indonesia'])
print("\n")

print("Nilai Produktif:")
print(data[data['Mapel'] == 'Produktif'])
print("\n")

print("Nilai Fisika:")
print(data[data['Mapel'] == 'Fisika'])
print("\n")

# -------------------------------
# 4. Nilai Maksimum & Minimum
# -------------------------------
print("Nilai Maksimum dan Minimum per Mata Pelajaran:")
nilai_extrem = data.groupby('Mapel')['Nilai'].agg(['max', 'min'])
print(nilai_extrem)
print("\n")

# -------------------------------
# 5. Grafik Batang Rata-Rata Nilai
# -------------------------------
print("Membuat Grafik Batang Rata-Rata Nilai...")
rata = data.groupby('Mapel')['Nilai'].mean()

plt.figure(figsize=(10, 6))
rata.plot(kind='bar', color=['skyblue', 'lightgreen', 'coral', 'gold', 'violet'])
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('rata_rata_nilai.png')
plt.close()
print("✅ Grafik batang disimpan sebagai 'rata_rata_nilai.png'\n")

# -------------------------------
# 6. Boxplot Sebaran Nilai
# -------------------------------
print("Membuat Diagram Boxplot Sebaran Nilai...")
plt.figure(figsize=(10, 6))
sns.boxplot(x='Mapel', y='Nilai', data=data, palette='Set2')
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('boxplot_nilai.png')
plt.close()
print("✅ Boxplot disimpan sebagai 'boxplot_nilai.png'\n")

# -------------------------------
# 7. (Opsional) Distribusi Nilai
# -------------------------------
print("Membuat Diagram Distribusi Nilai...")
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='Nilai', hue='Mapel', multiple='stack', kde=True)
plt.title('Distribusi Nilai Siswa per Mapel')
plt.xlabel('Nilai')
plt.ylabel('Jumlah Siswa')
plt.tight_layout()
plt.savefig('distribusi_nilai.png')
plt.close()
print("✅ Diagram distribusi disimpan sebagai 'distribusi_nilai.png'\n")

# -------------------------------
# 8. Selesai
# -------------------------------
print("🎉 Analisis selesai! Semua grafik telah disimpan di folder ini.")
print("File yang dihasilkan:")
print("- rata_rata_nilai.png")
print("- boxplot_nilai.png")
print("- distribusi_nilai.png")
