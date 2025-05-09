from faker import Faker
import pandas as pd
import random
import numpy as np
from datetime import datetime
import os

def guardar_csv(df, nombre_archivo, carpeta):
    os.makedirs(carpeta, exist_ok=True)
    ruta = f"{carpeta}/{nombre_archivo}.csv"
    df.to_csv(ruta, index=False)


def guardar_csv_procesado(df, nombre_archivo):
    guardar_csv(df, nombre_archivo, carpeta="data/processed")


######## RESERVAS ######

def save_clean_reservations(df):
    df.to_csv("data/processed/reservations_clean.csv", index=False)


##### ITINERARIOS ####

def guardar_itinerarios(df_raw, df_clean):
    df_raw.to_csv("data/raw/itineraries_raw.csv", index=False)
    df_clean.to_csv("data/processed/itineraries_clean.csv", index=False)

def guardar_itinerary_days(df_raw, df_clean):
    df_raw.to_csv("data/raw/itinerary_days_raw.csv", index=False)
    df_clean.to_csv("data/processed/itinerary_days_clean.csv", index=False)

def guardar_day_activities(df_raw, df_clean):
    df_raw.to_csv("data/raw/day_activities_raw.csv", index=False)
    df_clean.to_csv("data/processed/day_activities_clean.csv", index=False)
