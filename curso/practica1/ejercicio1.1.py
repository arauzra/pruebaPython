#diferencia con el resto de videos de soyDalto

video_de_dalto = 1.5
video_mas_rapido_otro = 2.5
video_mas_lento_otro = 7

diferencia_rapido = (video_mas_rapido_otro - video_de_dalto)  * 100 / video_mas_rapido_otro
print(f"el video de dalto dura un {diferencia_rapido:.2f}% menos" 
      f" que el video mas rapido de otros cursos")
diferencia_lento = (video_mas_lento_otro - video_de_dalto) * 100 / video_mas_lento_otro 
print(f"el video de dalto dura un {diferencia_lento:.2f}% menos"
      f" que el video mas lento de otros cursos")

promedio_videos = (video_de_dalto + video_mas_rapido_otro 
                   + video_mas_lento_otro) / 3
print(f"El promedio de duración de los videos es de:"
      f" {promedio_videos:.2f} horas")


#diferencia del material en crudo de los cursos y sus versiones finales

material_en_crudo_cursos = 5
material_en_crudo_este = 3.5

diferencia_crudo_cursos = (
      (material_en_crudo_cursos - promedio_videos) * (100) / (material_en_crudo_cursos)
      )
print(f"Los videos promedio de otros cursos eliminan un"
      f" {diferencia_crudo_cursos:.2f}% de tiempo vacio")


diferencia_crudo_este = (
      (material_en_crudo_este - video_de_dalto) * 100 / material_en_crudo_este
)
print(f"el video de dalto elimina un {diferencia_crudo_este:.2f}% de tiempo vacio")

#comparacion de los cursos en 10 horas

equivalencia_10horas_dalto = (promedio_videos * 10) / video_de_dalto
print(f"ver 10 horas del curso de dalto equivale a ver {equivalencia_10horas_dalto:.2f}"
      f" horas de otro curso")

equivalencia_10horas_otro = (video_de_dalto * 10) / promedio_videos
print(f"ver 10 horas de otro curso equivale a ver {equivalencia_10horas_otro:.2f}"
      f" horas del curso de Dalto")