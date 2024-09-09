import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Установка параметров окна
height = 750
width = 750
FPS = 60
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Загрузка изображений куба
cube_list = [
    pygame.image.load('game_cube/one.png').convert_alpha(),
    pygame.image.load('game_cube/two.png').convert_alpha(),
    pygame.image.load('game_cube/three.png').convert_alpha(),
    pygame.image.load('game_cube/four.png').convert_alpha(),
    pygame.image.load('game_cube/five.png').convert_alpha(),
    pygame.image.load('game_cube/six.png').convert_alpha()
]

# Переменные для управления состоянием игры
angle = 0  # Угол вращения куба
running = True  # Флаг для основного цикла игры
i = 0  # Индекс текущего изображения куба
down_bottom = 100  # Начальная позиция куба по вертикали
down_boolean = False  # Флаг, указывающий, падает ли куб
vobor_boolean = False  # Флаг, указывающий, выбрано ли новое изображение
rotate_boolean = True  # Флаг, указывающий, вращается ли куб
going_up = False  # Флаг, указывающий, поднимается ли куб

while running:
    window.fill((0, 0, 0))  # Очистка окна
    clock.tick(FPS)  # Установка FPS

    # Логика падения куба
    if down_boolean:
        down_bottom += 30  # Перемещение куба вниз

    # Проверка достижения нижней границы
    if down_bottom >= height + 120 and down_boolean:
        down_boolean = False  # Остановка падения
        vobor_boolean = True  # Подготовка к выбору нового изображения
        going_up = True  # Начало подъема куба
        rotate_boolean = False  # Остановка вращения
        rotated_sur = pygame.transform.rotate(sur, 0)  # Сброс вращения

    # Логика подъема куба
    if going_up:
        down_bottom -= 10  # Перемещение куба вверх
        if down_bottom <= 100:  # Проверка достижения верхней границы
            down_bottom = 100  # Установка куба на верхнюю границу
            time.sleep(2)  # Задержка перед новым падением
            going_up = False  # Остановка подъема
            vobor_boolean = False  # Сброс состояния выбора изображения
            rotate_boolean = True  # Возобновление вращения

    # Выбор нового изображения куба
    if vobor_boolean:
        sur = random.choice(cube_list)  # Случайный выбор изображения из списка

    # Логика вращения куба
    if rotate_boolean:
        i += 1  # Увеличение индекса изображения
        if i == 6:
            i = 0  # Сброс индекса при достижении конца списка
        else:
            time.sleep(0.1)  # Небольшая задержка для эффекта вращения
        sur = cube_list[i]  # Обновление текущего изображения куба
        rotated_sur = pygame.transform.rotate(sur, angle)  # Вращение изображения
        angle += 9  # Увеличение угла вращения

    # Центрирование куба по середине окна
    rect = rotated_sur.get_rect(center=(width // 2, down_bottom))

    # Отрисовка куба на экране
    window.blit(rotated_sur, rect.topleft)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Выход из игры при закрытии окна
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not down_boolean and not going_up:
                down_boolean = True  # Запуск процесса падения при нажатии пробела

    # Обновление окна
    pygame.display.update()

# Завершение Pygame
pygame.quit()