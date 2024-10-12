# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 05:46:08 2024

@author: Radja
"""
import os
import cv2
import pandas as pd
import numpy as np

# Définition des chemins pour le stockage des fichiers extraits
chemin_images = "./images/"
chemin_descripteurs = "./descripteurs/"
chemin_point_cle = "./point_cle/"
chemin_results = "./results/"

# Création des répertoires s'ils n'existent pas
if not os.path.exists(chemin_point_cle):
    os.mkdir(chemin_point_cle)
if not os.path.exists(chemin_descripteurs):
    os.mkdir(chemin_descripteurs)
if not os.path.exists(chemin_images):
    os.mkdir(chemin_images)
if not os.path.exists(chemin_results):
    os.mkdir(chemin_results)


# Fonction pour récupérer les descripteurs à partir des fichiers CSV
def get_descripteurs(chemin):
    data = pd.read_csv(chemin_descripteurs + chemin.split(".")[0] + ".csv")
    return np.array(data.values, dtype="float32")


# Fonction pour récupérer les points clés à partir des fichiers CSV
def hold_gp(chemin):
    data = pd.read_csv(chemin_point_cle + chemin.split(".")[0] + ".csv")
    keypoint = []
    for i in range(len(data)):
        dic = data.iloc[i]
        temp = cv2.KeyPoint(x=float(dic["point1"]),
                            y=float(dic["point2"]),
                            angle=dic["angle"],
                            size=dic["size"],
                            octave=int(dic["octave"]),
                            response=dic['response'],
                            class_id=int(dic["id"]))
        keypoint.append(temp)
    return keypoint


# Création d'un objet SIFT
sift = cv2.SIFT_create()

# Création d'un objet BFMatcher pour comparer les descripteurs
Eucl = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)


# Fonction pour comparer les descripteurs d'une nouvelle image avec ceux de la base de données
def verification(des1):
    list_images = os.listdir(chemin_images)
    for img in list_images:
        print(img)
        des2 = get_descripteurs(img)
        matches = Eucl.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)
        score = len(matches) / min(len(des1), len(des2))
        if score > 0.9:
            return 100 * score, img, matches
    return 0, "", []


# Fonction pour dessiner les points clés sur une image
def point_clef(img, keys, chemin):
    img= cv2.resize(img, (500, 500))
    img = cv2.drawKeypoints(img, keys, None)
    
    cv2.imwrite(chemin, img)


# Fonction pour dessiner les correspondances entre deux images
def correspondance(img1, img2, kp1, kp2, matches):
    end = min(100, len(matches))
    matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:end], None, flags=2)
    matching_result = cv2.resize(matching_result, (400, 400))
    cv2.imwrite(chemin_results + 'matching.png', matching_result)


# Fonction principale appelée par l'interface
def lancer(url):
    img = cv2.imread(url)
    img = cv2.resize(img, (500, 500))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (500, 500))
    gray = cv2.GaussianBlur(gray, (9, 9), 1)
    gray = cv2.equalizeHist(gray)
    kernel = np.ones((5,5),np.uint8)
    gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((5,5),np.uint8)
    gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    sift = cv2.SIFT_create()
    key1, des1 = sift.detectAndCompute(gray, None)
    score, img_path, matches = verification(des1)

    if score:
        code = int(img_path.split("_")[0][:-1])
        img2 = cv2.imread(chemin_images + img_path)
        key2 = hold_gp(img_path)
        cv2.imwrite(chemin_results + "real.png", img)
        point_clef(img, key1, chemin_results + "processed.png")
        img2= cv2.resize(img2, (500, 500))
        point_clef(img2, key2, chemin_results + "bdd.png")
        correspondance(img, img2, key1, key2, matches)
        return True, code, score
    else:
        return False, 0, 0





