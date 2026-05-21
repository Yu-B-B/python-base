import pygame
import random
import sys

# 初始化
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello World")

# 颜色常量
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

# 字符集（支持中文）
chars = "宝贝"

class Char:
    def __init__(self, x, y, speed, font_size):
        self.x = x
        self.y = y
        self.speed = speed
        self.font = pygame.font.SysFont('SimHei', font_size)  # 字体对象一次创建
        self.char = random.choice(chars)

    def update(self):
        self.y += self.speed
        if self.y > height:
            self.y = 0
            self.x = random.randint(0, width)
            self.char = random.choice(chars)

    def draw(self, surface):
        text = self.font.render(self.char, True, WHITE)
        surface.blit(text, (self.x, self.y))

def draw_heart(surface, x, y, size):
    """
    绘制一个简单的心形（近似）
    x, y: 心形外接矩形的左上角坐标
    size: 心形的宽度/高度
    """
    # 心形由两个半圆和一个倒三角组成
    radius = size // 3
    center_left = (x + radius, y + radius)
    center_right = (x + size - radius, y + radius)
    # 上半部分两个圆
    pygame.draw.circle(surface, RED, center_left, radius)
    pygame.draw.circle(surface, RED, center_right, radius)
    # 下半部分倒三角（覆盖两个圆的底部形成心尖）
    points = [
        (x, y + radius),                     # 左顶点
        (x + size // 2, y + size),           # 心尖
        (x + size, y + radius)               # 右顶点
    ]
    pygame.draw.polygon(surface, RED, points)

def create_char_particles(num=100):
    """生成字符雨粒子列表"""
    particles = []
    for _ in range(num):
        x = random.randint(0, width)
        y = random.randint(-height, 0)
        speed = random.randint(1, 3)
        font_size = random.randint(16, 24)
        particles.append(Char(x, y, speed, font_size))
    return particles

# 游戏状态常量
STATE_COUNTDOWN = 0
STATE_SHOW_HEART = 1

# 创建粒子系统
chars_list = create_char_particles(100)

clock = pygame.time.Clock()

# 预创建字体（避免每帧重新创建）
countdown_font = pygame.font.SysFont('SimHei', 50)
message_font = pygame.font.SysFont('SimHei', 30)

# 倒计时相关
countdown_numbers = ['3', '2', '1']
current_countdown_index = 0
countdown_start_time = pygame.time.get_ticks()  # 当前数字开始显示的时间
countdown_duration = 1000  # 每个数字显示1秒

# 心形相关
show_heart = False
heart_x = width // 2
heart_y = height // 2
heart_size = 0
max_heart_size = 150
heart_start_time = 0
heart_animation_duration = 1000  # 1秒内从0放大到最大

# 状态机
current_state = STATE_COUNTDOWN

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 更新字符雨（所有状态下都更新）
    for char in chars_list:
        char.update()

    # 状态逻辑
    now = pygame.time.get_ticks()
    if current_state == STATE_COUNTDOWN:
        # 检查是否需要切换到下一个数字
        elapsed = now - countdown_start_time
        if elapsed >= countdown_duration:
            current_countdown_index += 1
            if current_countdown_index < len(countdown_numbers):
                # 显示下一个数字
                countdown_start_time = now
            else:
                # 倒计时结束，切换到心形状态
                current_state = STATE_SHOW_HEART
                show_heart = True
                heart_size = 0
                heart_start_time = now
    else:  # STATE_SHOW_HEART
        # 心形放大动画
        if show_heart and heart_size < max_heart_size:
            elapsed = now - heart_start_time
            progress = min(1.0, elapsed / heart_animation_duration)
            heart_size = int(progress * max_heart_size)
        # 心形达到最大后不再变化（但保持显示）

    # 绘制
    screen.fill(BLACK)

    # 绘制字符雨
    for char in chars_list:
        char.draw(screen)

    # 根据状态绘制额外内容
    if current_state == STATE_COUNTDOWN:
        # 绘制倒计时数字
        if current_countdown_index < len(countdown_numbers):
            number = countdown_numbers[current_countdown_index]
            text = countdown_font.render(number, True, WHITE)
            text_rect = text.get_rect(center=(width//2, height//2))
            screen.blit(text, text_rect)
    else:  # STATE_SHOW_HEART
        if show_heart:
            # 绘制心形
            heart_left = heart_x - heart_size // 2
            heart_top = heart_y - heart_size // 2
            draw_heart(screen, heart_left, heart_top, heart_size)
            # 绘制文字
            msg = "彭女士 520快乐"
            text = message_font.render(msg, True, WHITE)
            text_rect = text.get_rect(center=(heart_x, heart_y + heart_size//2 + 30))
            screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()