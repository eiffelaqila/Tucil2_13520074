import math
import numpy as np

def isLeft(p1, p2, p3):
    """
    Mengembalikan true jika p3 terletak di kiri garis p1-p2 dan false jika tidak
    berdasarkan persamaan determinan
    """
    return (np.linalg.det(np.array([[p1[0], p1[1], 1], [p2[0], p2[1], 1], [p3[0], p3[1], 1]])) > 0)

def distance(p1, p2, p3):
    """
    Menghitung jarak p3 dengan garis p1-p2
    """
    return math.dist(p1, p3) + math.dist(p2, p3)

def leftSide(p1, p2, list_of_points):
    """
    Mengembalikan list yang berisi point-point yang 
    terletak di kiri garis p1-p2
    """
    leftSide = []
    for i in range(len(list_of_points)):
        if (isLeft(p1, p2, list_of_points[i])):
            leftSide.append(list_of_points[i])
    
    return leftSide

def findFarthest(p1, p2, list_of_points):
    """
    Mengembalikan point yang letaknya paling jauh dari garis p1-p2
    jika terdapat point dengan jarak yang sama, mengembalikan point dengan
    besar sudut paling besar
    """
    max_distance = 0
    max_index = 0
    max_angle = 0
    for i in range (len(list_of_points)):
        currDistance = distance(p1,p2,list_of_points[i])
        currAngle = angle(p1, p2, list_of_points[i])
        if (currDistance > max_distance):
            max_distance = currDistance
            max_index = i
            max_angle = currAngle
        elif ((currDistance == max_distance) and (currAngle > max_angle)):
            max_distance = currDistance
            max_index = i
            max_angle = currAngle
    return list_of_points[max_index]

def angle(p1, p2, p3):
    """
    Mengembalikan besar sudut p3-p1-p2
    """
    ang = math.degrees(math.atan2(p3[1]-p1[1], p3[0]-p1[0]) - math.atan2(p2[1]-p1[1], p2[0]-p1[0]))
    if ang < 0:
        return ang+360
    else:
        return ang

def FindHull(p1,p2,list_of_points,list_of_hull):
    """
    Implementasi Algoritma Divide and Conquer untuk mencari solusi Convex Hull
    """

    if (len(list_of_points) == 0):  # Basis
        # List kosong
        return list_of_hull
    else:   # Rekurens
        # Menentukan titik terjauh dari garis p1-p2
        max_point = findFarthest(p1, p2, list_of_points)
        list_of_hull.append(max_point)

        list_of_points.remove(max_point)

        # Memanggil kembali fungsi FindHull
        # Mencari solusi di kiri p1-max_point
        list_of_hull = FindHull(p1, max_point, leftSide(p1, max_point, list_of_points), list_of_hull)
        # Mencari solusi di kiri max_point-p2
        list_of_hull = FindHull(max_point, p2, leftSide(max_point, p2, list_of_points), list_of_hull)
        return list_of_hull

def ConvexHull(list_of_points):
    """
    Fungsi utama untuk menentukan ConvexHull

    Mengembalikan pasangan titik pembentuk convex hull
    """
    # Inisialisasi
    list_of_hull = []   # Kumpulan titik-titik pembentuk convex hull
    tuple_of_hull = []  # Kumpulan pasangan titik pembentuk convex hull

    # Mengurutkan list of points berdasarkan absis
    list_of_points = sorted(list_of_points.tolist())

    # Menentukan titik minimum (p1) dan maksimum (pn)
    p1 = list_of_points[0]
    pn = list_of_points[len(list_of_points)-1]
    list_of_hull.append(p1)
    list_of_hull.append(pn)

    # Memanggil fungsi FindHull untuk mencari solusi di atas dan bawah garis
    list_of_hull = FindHull(p1, pn, leftSide(p1,pn,list_of_points), list_of_hull)
    list_of_hull = FindHull(pn, p1, leftSide(pn,p1,list_of_points), list_of_hull)

    # Mengurutkan list of hull
    mid_x = sum(p[0] for p in list_of_hull)/len(list_of_hull)
    mid_y = sum(p[1] for p in list_of_hull)/len(list_of_hull)
    list_of_hull.sort(key = lambda p: math.atan2(p[0] - mid_x, p[1] - mid_y))

    # Membuat tuple of hull
    for j in range(0,len(list_of_hull)):
        if(j == len(list_of_hull)-1):
            tuple_of_hull.append([list_of_hull[j],list_of_hull[0]])
        else:
            tuple_of_hull.append([list_of_hull[j],list_of_hull[j+1]])

    return tuple_of_hull