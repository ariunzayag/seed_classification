from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_score
from sklearn.datasets import make_classification
from yellowbrick.cluster import KElbowVisualizer, SilhouetteVisualizer

from sklearn.model_selection import train_test_split

import os
import cv2
import glob
from PIL import Image
import numpy as np
from numpy import unique
from numpy import where
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from matplotlib import pyplot
import pandas as pd
import seaborn as sns
from sklearn.utils import shuffle
import matplotlib.image as mpimg
import skimage.io as io
from skimage.util import img_as_float

#read dataset
# dataset = os.listdir("/home/users/zaya/workpsace/biology_classification/unsupervised_data/gray/")
# print(type(dataset))

# img_array = np.array(dataset)
# print(type(img_array))

img_list = []
directory = "/home/users/zaya/workpsace/biology_classification/unsupervised_data/gray/*.*"

#convert list to vector
for i in glob.glob(directory):
    img = cv2.imread(i, 0)
    convert = img_as_float(img)
    img_list.append(convert)

print(type(img_list))    

#convert 3d array to 2d 
nsamples = np.asarray(img_list).reshape(len(img_list),-1)

#normalized data
scaler = MinMaxScaler()
data_scale = scaler.fit_transform(nsamples)

#shuffle data
df = np.vstack(data_scale)
df = shuffle(df, random_state=42)

#train data
km = KMeans(n_clusters = 4, random_state = 0).fit(df)

groups = {}
for file, cluster in zip(dataset,km.labels_):
    if cluster not in groups.keys():
        print(cluster)
        groups[cluster] = []
        groups[cluster].append(file)
    else:
        groups[cluster].append(file)
        
#view cluster image       
def view_cluster(cluster):
    plt.figure(figsize = (25,25));
    files = groups[cluster]
    #only show 30 images at a time
    if len(files) > 10:
        print(f"Clipping cluster size from {len(files)} to 30")
        files = files[:9]
    # plot each image in the cluster
    for index, file in enumerate(files):
        plt.subplot(10,10,index+1);
        img = load_img(file)
        img = np.array(img)
        plt.imshow(img)
        plt.axis('off')