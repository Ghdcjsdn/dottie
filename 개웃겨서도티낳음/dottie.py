import pygame
import random
import sys
import time
import os  # 경로 관련

# Pygame 초기화
pygame.init()
pygame.mixer.init()

# 화면 설정
font = pygame.font.Font(os.path.join("fonts", "[KIM]WILDgag-Bold.ttf"), 36)
pygame.display.set_caption("도티를 낳아버림")
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 이미지 경로
flag_width, flag_height = 120, 80
blue_flag_down_img = pygame.image.load(os.path.join("images", "기본.png"))
blue_flag_up_img = pygame.image.load(os.path.join("images", "낳음.png"))
white_flag_down_img = pygame.image.load(os.path.join("images", "기본.png"))
white_flag_up_img = pygame.image.load(os.path.join("images", "유산.jpg"))

blue_flag_down = pygame.transform.scale(blue_flag_down_img, (flag_width, flag_height))
blue_flag_up = pygame.transform.scale(blue_flag_up_img, (flag_width, flag_height))
white_flag_down = pygame.transform.scale(white_flag_down_img, (flag_width, flag_height))
white_flag_up = pygame.transform.scale(white_flag_up_img, (flag_width, flag_height))

# 사운드 로드
pygame.mixer.music.load(os.path.join("sounds", "[도티 낳음 공모전] 개웃겨서 도티 목소리로 노래만듦.mp3"))
pygame.mixer.music.play(-1)

sound_blue = pygame.mixer.Sound(os.path.join("sounds", "짜잇호.mp3"))
sound_white = pygame.mixer.Sound(os.path.join("sounds", "호잇짜.mp3"))
sound_blue_press = pygame.mixer.Sound(os.path.join("sounds", "짜잇호.mp3"))
sound_white_press = pygame.mixer.Sound(os.path.join("sounds", "호잇짜.mp3"))
sound_correct = pygame.mixer.Sound(os.path.join("sounds", "O.mp3"))
sound_wrong = pygame.mixer.Sound(os.path.join("sounds", "X.mp3"))

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)

# 깃발 위치
flag_y_default = 320
flag_y_up = 180

# 이미지 위치
blue_x = 180
white_x = 500

# 명령 목록
COMMANDS = [
    ("도티 낳아", "left"),
    ("도티 유산", "right"),
    ("둘 다 올려", "up"),
    ("아무것도 하지 마", "s"),
]


def draw_scene(blue_up, white_up, message, score, lives):
    screen.fill((240, 240, 255))
    
    # 깃발 이미지 선택
    blue_img = blue_flag_up if blue_up else blue_flag_down
    white_img = white_flag_up if white_up else white_flag_down

    # 위치 지정
    blue_y = flag_y_up if blue_up else flag_y_default
    white_y = flag_y_up if white_up else flag_y_default

    screen.blit(blue_img, (blue_x, blue_y))
    screen.blit(white_img, (white_x, white_y))

    # 점수, 목숨, 명령
    score_text = font.render(f"점수: {score}", True, BLACK)
    lives_text = font.render(f"목숨: {lives}", True, RED)
    screen.blit(score_text, (30, 30))
    screen.blit(lives_text, (30, 80))

    cmd_text = font.render(message, True, BLACK)
    screen.blit(cmd_text, (WIDTH//2 - cmd_text.get_width()//2, 150))

    pygame.display.flip()

def show_message(message, duration=0.8):
    """검은 화면에 메시지 표시 + 키 입력 무시"""
    start = time.time()
    while time.time() - start < duration:
        screen.fill(BLACK)
        text = font.render(message, True, WHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 30))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(60)

def game_over_screen(score):
    show_message(f"게임 종료! 총 점수: {score}", 2)

def main():
    screen.fill(BLACK)
    msg = "도티 낳음은 오른쪽! 도티 유산은 왼쪽!"
    text = font.render(msg, True, WHITE)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 50))
    pygame.display.flip()
    pygame.time.wait(2000)  # 안내 메시지 2초

    # 3,2,1 카운트다운
    for i in range(3, 0, -1):
        screen.fill(BLACK)
        count_text = font.render(str(i), True, WHITE)
        screen.blit(count_text, (WIDTH//2 - count_text.get_width()//2, HEIGHT//2 - 30))
        pygame.display.flip()
        pygame.time.wait(1000)
    running = True
    while running:  # 게임 무한 반복
        score = 0
        lives = 3
        round_num = 0
        time_limit = 0.8
        chapter_speed_increase = 0.15

        while lives > 0:
            
            round_num += 1
            cmd_text, cmd_key = random.choice(COMMANDS)

            # 명령 효과음
            if cmd_text == "도티 낳아":
                sound_blue.play()
            elif cmd_text == "도티 유산":
                sound_white.play()

            draw_scene(False, False, f"{round_num}라운드!", score, lives)
            pygame.time.wait(700)

            # 10라운드마다 챕터 표시 및 속도 증가
            # 10라운드마다 챕터 표시 및 속도 증가
            
            start = time.time()
            pressed = None
            key_pressed = False
            blue_up, white_up = False, False

            while time.time() - start < time_limit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.name(event.key).lower()
                        if key == "q":
                            pygame.quit()
                            sys.exit()
                        pressed = key
                        key_pressed = True

                        # 깃발 올리기
                        if key == "left":   
                            blue_up = True
                            sound_blue_press.play()
                        elif key == "right":
                            white_up = True
                            sound_white_press.play()
                        elif key == "up":
                            blue_up = True
                            white_up = True
                            sound_blue_press.play()
                            sound_white_press.play()

                draw_scene(blue_up, white_up, cmd_text, score, lives)
                clock.tick(60)
            if round_num % 10 == 0 and round_num != 1:
                chapter = round_num // 10
                show_message(f"챕터 {chapter}", 1.5)
                time_limit -= chapter_speed_increase

            # 정답 판정
            if cmd_key == "s":
                correct = not key_pressed
            elif cmd_key == "up":
                correct = pressed == "up"
            else:
                correct = pressed == cmd_key

            if correct:
                score += 10
                sound_correct.play()
                show_message("정답!", 0.8)
            else:
                lives -= 1
                sound_wrong.play()
                show_message("오답!", 0.8)

        game_over_screen(score)

if __name__ == "__main__":
    main()
