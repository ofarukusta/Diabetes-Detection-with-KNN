import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# Outcome = 1 Diyabet
# Outcome = 0 Sağlıklı
data = pd.read_csv("diabetes.csv")
data.head()

seker_hastalari = data[data.Outcome == 1]
saglikli_insanlar = data[data.Outcome == 0]

plt.scatter(saglikli_insanlar.Age, saglikli_insanlar.Glucose, color="green", label="sağlıklı", alpha = 0.4)
plt.scatter(seker_hastalari.Age, seker_hastalari.Glucose, color="red", label="diabet hastası", alpha = 0.4)
plt.xlabel("Age")
plt.ylabel("Glucose")
plt.legend()
plt.show()

# glukoza bağlı örnek grafik çizimi


"""
0 çıktısı sağlıklı insanı 1 çıktısı diyabet insanı temsil etmektedir.

veri bilimi kütüphanelerimizi ve eğitim için gerekli olan kütüphanelerimizi indirdik
"""



# x ve y eksenlerini belirleyelim
y = data.Outcome.values
x_ham_veri = data.drop(["Outcome"],axis=1)   
# Outcome sütununu(dependent variable) çıkarıp sadece independent variables bırakıyoruz
# Çüknü KNN algoritması x değerleri içerisinde gruplandırma yapacak..


# normalization yapıyoruz - x_ham_veri içerisindeki değerleri sadece 0 ve 1 arasında olacak şekilde hepsini güncelliyoruz
# Eğer bu şekilde normalization yapmazsak yüksek rakamlar küçük rakamları ezer ve KNN algoritmasını yanıltabilir!
x = (x_ham_veri - np.min(x_ham_veri))/(np.max(x_ham_veri)-np.min(x_ham_veri))

# önce
print("Normalization öncesi ham veriler:\n")
print(x_ham_veri.head())


# sonra 
print("\n\n\nNormalization sonrası yapay zekaya eğitim için vereceğimiz veriler:\n")
print(x.head())
    


"""
eğitim ve test datalarımızı belirlememiz lazım
split metodu ile ayırma işlemi yapacağız
"""

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3,random_state=1)
"""
 %70 eğitim, %30  test olarak seçim yaptık (en iyi oranı belirlemek için belirli aralıklarla deneme yapılabilir)
"""
knn = KNeighborsClassifier(n_neighbors = 5) # n_neighbors = k
knn.fit(x_train,y_train)
prediction = knn.predict(x_test)
print("K=5 için Test verilerimizin doğrulama testi sonucu ", knn.score(x_test, y_test))

sayac = 1
for k in range(1,11):
    knn_yeni = KNeighborsClassifier(n_neighbors = k)
    knn_yeni.fit(x_train,y_train)
    print(sayac, "  ", "Doğruluk oranı: %", knn_yeni.score(x_test,y_test)*100)
    sayac += 1
    

#Optimum K değerini küçük bir döngü ile öğrenebiliriz

# Yeni bir hasta tahmini için:

 

from sklearn.preprocessing import MinMaxScaler

# normalization yapıyoruz - daha hızlı normalization yapabilmek için MinMax  scaler kullandık
sc = MinMaxScaler()
sc.fit_transform(x_ham_veri)

new_prediction = knn.predict(sc.transform(np.array([[6,148,72,35,0,33.6,0.627,50]]))) # hasta bir insanın değerlerini girdik, sonucun 1 çıkması gerekiyor
new_prediction[0]

print(new_prediction) #yapay zekanın tahminini ekrana yazdırdık