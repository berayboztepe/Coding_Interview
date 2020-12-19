import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


#mnist datasetini yükledik(hazırda var)
fashion_mnist = tf.keras.datasets.fashion_mnist

#train için 60k veri, test için 10k veri var. Bunları ayırdık
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

#labellarımız bunlardır. Görüntüler ise 28x28 piksellik bir matristir.
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(train_images.shape)#60k resim, her biri 28x28 pikseldir.

print(len(train_labels))#60k etiket var. Her resim için bir etiket

print(train_labels)#her bir etiket 0-9 arasında bir tam sayıdır. 0 ise t-shirt, 1 ise pantolon vb.

print(test_images.shape)#10k resim, her biri 28x28 pikseldir. Test dizisi

print(test_labels)#10k etiket var.

#önce verileri işlememiz gerekir. ilk resme baktığımız zaman piksel değeri 0-255 arasındadır.

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()


#Sinir ağı modeline beslemeden önce scale etmemiz gerekir. Bunun için resim değerlerini 255'e bölmemiz gerekir. Test için de train için de
train_images = train_images / 255.0
test_images = test_images / 255.0


#Verileri doğrulamak için ilk 25 görüntüyü ve her görüntünün sınıf adına bakalım.

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])

plt.show()


#modeli oluşturmak için önce modelin katmanları yapılandırılmalı, sonra ise model derlenmeli

#Derin öğrenmenin çoğu, basit katmanları birbirine zincirlemekten oluşur.

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),#görüntülerin formatını iki boyutlu diziden tek boyuta biçimlendirdik (28x28 = 784 piksel)
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
    #daha sonra layers.Dense ile 2 farklı katman(yoğun şekilde bağlı sinir ağları) oluşturduk. ilk katman 128 nörona sahip
    #İkinci katmanda  ise 10 uzunluğunda bir logits dizisi döndürür. Yani her düğüm, geçerli 10 sınıftan birine ait olduğunu gösteren puan içerir
])

#sonra model derlenir. Kayıp işlevi=Modelin eğitim sırasında ne kadar doğru olduğunu ölçer. azaldıkça doğruluk artar
#optimizer=model, gördüğü verilere ve kayıp işlevine göre nasıl güncellenir.
#merikler=eğitim ve test adımlarını incelemek için kullanılır.

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])#bu modelde incelemek için doğru şekilde sınıflandırılan görüntülerin oranını kullandık

#modeli eğitelim
#train_img ve train_labels'i eğitip test_img'e göre test_labels'ın doğruluğuna bakacağız.

model.fit(train_images, train_labels, epochs=10)#model 10 kere eğitildi ve eğitildikçe doğruluk oranı 0.9080'e çıktı. Yaklaşık %91

#model test veri kümesinde nasıl performans gösteriyor? doğruluğunu değerlendirelim
#Test Accuracy =  0.8787999749183655 çıkan değer bu
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print("\nTest Accuracy = ", test_acc)

#test acc ile train acc arasındaki fark aşırı uyumu temsil eder.
# Aşırı uyum, bir makine öğrenimi modeli yeni, daha önce görülmemiş girdilerde eğitim verilerinde olduğundan daha kötü performans gösterdiğinde gerçekleşir.
# Aşırı uyarlanmış bir model, eğitim veri setindeki gürültüyü ve ayrıntıları, modelin performansını yeni veriler üzerinde olumsuz olarak etkileyecek bir noktaya kadar "ezberler".

#tahmin yapalım
#logitleri daha kolay yorumlanması olan olasılıklara dönüştürmek için softmax katmanı ekledik
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(test_images)

#ilk değerin tahminine baktığımızda 10 sayılık dizi gelir. 10 labeldan hangisine daha yakın olduğunu gösterir.
print(predictions[0])
#hangisinin en yüksek olduğunu görmek için:
print(np.argmax(predictions[0]))#cevap 9'dur. Yani, ilk modelin ankle boot olduğunu söyler bize. Bundan emindir.

print(test_labels[0])#diye bakarsak bu tahminin doğru olduğunu gösterir bize.

#ilk 10 sınıfın tahminine bakıp bunun grafiğini çizelim

def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label=np.argmax(predictions_array)

    if predicted_label == true_label:
        color='blue'
    else:
        color='red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                         100 * np.max(predictions_array),
                                         class_names[true_label]),
               color=color)
def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color='#777777')
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

#tahminleri doğrulayalım

i=0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,1)
plot_value_array(i, predictions[i], test_labels)
plt.show()

#kral bunu yanlış buluyo ya. Sneakers'a sandal diyo
i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()

#şimdi ise birkaç görüntüye birden bakalım
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()


#tek bir görüntü hakkında tahmin yapmak için eğitimli modeli kullanalım

img=test_images[1]

#tek bir resim kullanıyor bile olsak kerasla tahmin yapmak için onu bir listeye atmamız gerekir.
img = (np.expand_dims(img, 0))
#bu görüntü için doğru etiketi tahmin edelim
predictions_single = probability_model.predict(img)
print(predictions_single)#dizinin 2. indeksi en iyi sonucu verdi

plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()
