# Diabetes-Detection-with-KNN

                    #K-NN -> K- Nearest Neighbours ( En Yakın Komşu Algoritması)
KNN sınıflandırma algoritmalarından birisidir. Daha önce elde edilen noktalara bakarak yeni bir noktanın hangi grupta olacağını bulmak için kullanılır   

![image](https://user-images.githubusercontent.com/110857814/219017952-dad5cca3-3c30-4707-bce2-d613948f0705.png)





X ve Y ekseninde eldeki verileri kategorilendirir ve yeni gelen veriyi bu kategorilere atayarak sınıflandırma yapar. Bu sınıflandırma geçmişteki bilgi birikimi kullanılarak yapılır.

 KNN modeli yeni noktanın hangi grupta olduğunu bulurken Öklid Uzaklık Formülünü kullanır. Bu formül matematiksel olarak aşağıdaki gibidir.
 ![image](https://user-images.githubusercontent.com/110857814/219017983-9f425b05-e206-4105-8af9-81bb99a405fe.png)

                        
 Hesaplama yapılmadan önce veri setine göre konum alınırken, K değeri el ile girilmesi gerekmektedir. Verilen K değeri veri setinde esas alınacak olan değer ne ise(mesela yaş değeri) o çevrede K kadar değer ele alır. Mesela K=4 dersek o çevredeki en yakın 4 veriyi(geçmişte sonucu bilinen veriyi(dataset)) ele alarak Öklid uzaklığı hesaplamasını yapar.

                                                      #K-NN ile Şeker Hastalığı Tespiti
 Veri seti Hindistan’da yaşayan 768 Kadın hasta üzerinden alınan verileri kapsamaktadır. Veri seti içerisinde; Yaş, Vücut Kitle İndeksi, Glukoz değeri, Cilt Kalınlığı, İnsülin değer, Diyabet soy ağacı işlevi gibi değerler ele alınmıştır.


 
