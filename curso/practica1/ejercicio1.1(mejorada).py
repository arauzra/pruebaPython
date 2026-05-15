# diferencia con el resto de videos de soyDalto

video_de_dalto = 1.5
video_mas_rapido_otro = 2.5
video_mas_lento_otro = 7


# función general
def porcentaje_menos(base, comparado):
    return (base - comparado) / base * 100


# 1. Dalto vs más rápido (respecto al otro video)
diferencia_rapido = porcentaje_menos(video_mas_rapido_otro, video_de_dalto)
print(
    f"El video de Dalto dura un {abs(diferencia_rapido):.2f}% menos "
    f"que el video más rápido de otros cursos"
)

# 2. Dalto vs más lento
diferencia_lento = porcentaje_menos(video_mas_lento_otro, video_de_dalto)
print(
    f"El video de Dalto dura un {abs(diferencia_lento):.2f}% menos "
    f"que el video más lento de otros cursos"
)


# promedio SOLO competencia
promedio_videos = (video_mas_rapido_otro + video_mas_lento_otro) / 2
print(f"El promedio de duración de los videos es de: {promedio_videos:.2f} horas")



# 3. reducción de tiempo vacío (respecto al material en crudo)
material_en_crudo_cursos = 5
material_en_crudo_este = 3.5

reduccion_promedio = porcentaje_menos(material_en_crudo_cursos, promedio_videos)
print(
    f"Los videos promedio de otros cursos eliminan un "
    f"{abs(reduccion_promedio):.2f}% de tiempo vacío"
)

reduccion_dalto = porcentaje_menos(material_en_crudo_este, video_de_dalto)
print(
    f"El video de Dalto elimina un {abs(reduccion_dalto):.2f}% de tiempo vacío"
)


# 4. equivalencias en 10 horas
equivalencia_dalto = (promedio_videos * 10) / video_de_dalto
print(
    f"Ver 10 horas del curso de Dalto equivale a ver "
    f"{equivalencia_dalto:.2f} horas de otro curso"
)

equivalencia_otro = (video_de_dalto * 10) / promedio_videos
print(
    f"Ver 10 horas de otro curso equivale a ver "
    f"{equivalencia_otro:.2f} horas del curso de Dalto"
)