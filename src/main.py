from myConvexHull import ConvexHull
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Mencetak datasets yang tersedia
    print("Datasets yang tersedia:")
    print("1. Iris")
    print("2. Wine")
    print("3. Breast Cancer")

    # Memilih dataset
    pilihanDataset = int(input("Masukkan pilihan datasets (dalam nomor): "))

    if (pilihanDataset == 1):
        data = datasets.load_iris()
    elif (pilihanDataset == 2):
        data = datasets.load_wine()
    else:
        data = datasets.load_breast_cancer()
    
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    
    # Memilih kolom
    print("Daftar kolom yang tersedia:")
    for i in range(len(data.feature_names)):
        print(str(i+1) + ". " + str(data.feature_names[i]))

    X = int(input("Masukan atribut-x: "))
    Y = int(input("Masukan atribut-y: "))

    #visualisasi hasil ConvexHull
    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title(data.feature_names[X-1] + ' vs ' + data.feature_names[Y-1])
    plt.xlabel(data.feature_names[X-1])
    plt.ylabel(data.feature_names[Y-1])
    
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[X-1,Y-1]].values
        hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    
        for j in range(len(hull)):
            plt.plot([hull[j][0][0],hull[j][1][0]], [hull[j][0][1],hull[j][1][1]], colors[i])

    plt.legend()
    plt.show()