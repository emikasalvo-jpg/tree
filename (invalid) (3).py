from pydub import AudioSegment
from pydub.playback import play
import time

# Загрузите звук двигателя
engine_sound = AudioSegment.from_file("engine_sound.mp3") # Замените на имя вашего файла

def simulate_engine_rpm(rpm):
    # Примерно определяем продолжительность звука в секундах (10 секунд выполнения)
    duration = 10
    num_loops = duration * (rpm / 6000)  # Пропорция для воспроизведения в зависимости от RPM
    
    print(f"Симуляция двигателя на {rpm} RPM")
    
    # Увеличение громкости на основе RPM
    sound = engine_sound + (rpm / 6000 * 10)  # Измените максимальные уровни по своему усмотрению
    play(sound)

    # Запуск циклического воспроизведения
    for _ in range(int(num_loops)):
        play(sound)
        time.sleep(1)  # Пауза между воспроизведениями

# Пример использования
simulate_engine_rpm(3000)  # Замените на нужные вам обороты