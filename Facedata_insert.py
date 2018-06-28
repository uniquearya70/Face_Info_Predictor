#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:54:40 2018

@author: arpitansh
"""

from mysql.connector import MySQLConnection, Error
from Face_Details_dbconfig import read_db_config

def insert_Face_Details(face_id, gender,age,emotion,emotion_percentage):
    query = "INSERT INTO FaceData(face_id, gender,age,emotion,emotion_percentage) " \
            "VALUES(%s,%s,%s,%s,%s)"
    args = (face_id, gender,age,emotion,emotion_percentage)
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config) 
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found') 
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
        
    print('Face Data transfered into Database')
