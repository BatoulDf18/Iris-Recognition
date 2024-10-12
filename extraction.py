# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 05:42:57 2024

@author: Radja
"""
import numpy as np
import cv2
import zipfile
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def extractions():
    # Définition des chemins de stockage des fichiers extraits
    path_key_points = "./point_cle/"
    path_descripteurs = "./descripteurs/"
    path_images = "./images/"
    path_database = "./database/"

    # Vérification et création des répertoires s'ils n'existent pas
    if not os.path.exists(path_images):  
        os.mkdir(path_images)
    if not os.path.exists(path_descripteurs): 
        os.mkdir(path_descripteurs)
    if not os.path.exists(path_key_points):  
        os.mkdir(path_key_points)

    # Fonction pour extraire les images
    def extraction_des_images(path_database, path_images):
        list_zips = os.listdir(path_database)
        list_zips = [x for x in list_zips if ".zip" in x]
        for fichier in list_zips:
            path_to_zip_file = path_database + fichier
            with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
                zip_ref.extractall(path_images)

    # Fonction pour extraire et sauvegarder les points clés
    def points_cle_extraction(key_points, img):
        paths_f = path_key_points + str(img.split('.')[0]) + ".csv"
        columns = ["point1", "point2", "size", "angle", "response", "octave", "id"]
        data = []
        for point in key_points:
            temp = {
                "point1": point.pt[0],
                "point2": point.pt[1],
                "size": point.size,
                "angle": point.angle,
                "response": point.response,
                "octave": point.octave,
                "id": point.class_id
            }
            data.append(temp)
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(paths_f, index=False)

    # Fonction pour sauvegarder les descripteurs dans un fichier CSV
    def desc(descripteurs, img):
        paths_f = path_descripteurs + str(img.split('.')[0]) + ".csv"
        df = pd.DataFrame(descripteurs)
        df.to_csv(paths_f, index=False)

    # Extraction des images depuis la base et sauvegarde des key points et descripteurs dans des fichiers CSV
    sift = cv2.SIFT_create()
    extraction_des_images(path_database, path_images)
    list_images = os.listdir(path_images)

    def process_image(pic):
        img = cv2.imread(path_images + pic)
    
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (500, 500))
        gray = cv2.GaussianBlur(gray, (9, 9), 1)
        gray = cv2.equalizeHist(gray)
        kernel = np.ones((5,5),np.uint8)
        gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        kernel = np.ones((5,5),np.uint8)
        gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        key_points, descripteurs = sift.detectAndCompute(gray, None)
        gray = cv2.drawKeypoints(gray, key_points, None)

        points_cle_extraction(key_points, pic)
        desc(descripteurs, pic)

    # Utilisation de ThreadPoolExecutor pour exécuter les opérations en parallèle
    with ThreadPoolExecutor() as executor:
        executor.map(process_image, list_images)



