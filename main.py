from pipeline import pipeline_places, pipeline_reservations, pipeline_itineraries

if __name__ == "__main__":
    print("▶ Ejecutando pipeline_places...")
    pipeline_places.run()

    print("▶ Ejecutando pipeline_reservations...")
    pipeline_reservations.run()

    print("▶ Ejecutando pipeline_itineraries...")
    pipeline_itineraries.run()

    print("✅ Todos los pipelines se han ejecutado correctamente.")

