import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

from sklearn.metrics import accuracy_score, f1_score, precision_score, confusion_matrix

from sklearn.model_selection import train_test_split

import tensorflow as tf

#CNN
import tensorflow as tf
from keras import layers, models
from keras.models import Sequential
from keras.layers import Flatten, Conv2D, Dense, MaxPool2D, Dropout
from keras.preprocessing.image import ImageDataGenerator


SIZE = 256
dataset = []
label = []

#dataset
train_dir = 'C:/Users/User/Documents/research/researchArea/implementation/dataset/anticlinal/training/'
test_dir = 'C:/Users/User/Documents/research/researchArea/implementation/dataset/anticlinal/test/'

#
irregular_curved = os.listdir(train_dir + 'irregular_curved/')
for i, image_name in enumerate(irregular_curved):
    image = Image.open(train_dir + 'irregular_curved/' + image_name).convert('RGB')
    image = image.resize((SIZE, SIZE))
    dataset.append(np.array(image))
    label.append(0)


ins = os.listdir(train_dir + 'irregular_curved_to_nearly_straight/')
for i, image_name in enumerate(ins):
    image = Image.open(train_dir + 'irregular_curved_to_nearly_straight/' + image_name).convert('RGB')
    image = image.resize((SIZE, SIZE))
    dataset.append(np.array(image))
    label.append(1)

o = os.listdir(train_dir + 'omega/')
for i, image_name in enumerate(o):
    image = Image.open(train_dir + 'omega/' + image_name).convert('RGB')
    image = image.resize((SIZE, SIZE))
    dataset.append(np.array(image))
    label.append(2)

s = os.listdir(train_dir + 's/')
for i, image_name in enumerate(s):
    image = Image.open(train_dir + 's/' + image_name).convert('RGB')
    image = image.resize((SIZE, SIZE))
    dataset.append(np.array(image))
    label.append(3)

st = os.listdir(train_dir + 'straight/')
for i, image_name in enumerate(st):
    image = Image.open(train_dir + 'straight/' + image_name).convert('RGB')
    image = image.resize((SIZE, SIZE))
    dataset.append(np.array(image))
    label.append(4)

u = os.listdir(train_dir + 'u/')
for i, image_name in enumerate(u):
    image = Image.open(train_dir + 'u/' + image_name).convert('RGB')
    image = image.resize((SIZE, SIZE))
    dataset.append(np.array(image))
    label.append(5)
    
u_to_omega = os.listdir(train_dir + 'u_to_omega/')
for i, image_name in enumerate(u_to_omega):
    image = Image.open(train_dir + 'u_to_omega/' + image_name).convert('RGB')
    image = image.resize((SIZE, SIZE))
    dataset.append(np.array(image))
    label.append(6)

#
dataset = np.array(dataset)
label = np.array(label)

#split dataset
X_train, X_test, y_train, y_test = train_test_split(dataset, label, test_size=0.2, random_state=42)

#
image_shape = (224, 224, 3)
batch_size = 64
epochs = 100
class_num = 6
base_learning_rate = 0.0001

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)))
model.add(layers.Conv2D(32, (3, 3), activation='relu', ))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(class_num))

model.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
          loss=tf.keras.losses.binary_crossentropy,
          metrics=['accuracy'])
model.summary()

#
from tensorflow.keras.callbacks import EarlyStopping
callbacks = [
             EarlyStopping(patience=2)
]
#
history = model.fit(X_train, y_train, epochs=epochs, validation_data=(X_test, y_test), callbacks=callbacks)

#

scores = model.evaluate(X_test, y_test, verbose=0)
print('test_score: ', scores)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

val_loss = history.history['val_loss']
loss = history.history['loss']

#
model.save('final_edition_cnn.h5')

#
scores = model.evaluate(X_test, y_test, verbose=0)
print('test_score: ', scores)

#
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

val_loss = history.history['val_loss']
loss = history.history['loss']

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.ylabel('Accuracy')
plt.ylim([min(plt.ylim()),1])
plt.title('Training and Validation Accuracy')

plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.ylabel('Cross Entropy')
plt.ylim([0,1.0])
plt.title('Training and Validation Loss')
plt.xlabel('epoch')
plt.show()