# 그림 구현 후, 게임 최종본(완성도 높이기)
import random
import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1000  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 마우스 커서 이미지 로드
cursor_image = pygame.image.load("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/커서.png")
cursor_image = pygame.transform.scale(cursor_image, (200, 200))

# 마우스 커서 설정
pygame.mouse.set_visible(False)

# 게임 제목
pygame.font.init()
font = pygame.font.SysFont('Maplestory Bold', 100)

# 화면 타이틀 설정
pygame.display.set_caption("Number Baseball Game")

# 아이콘 설정
icon_image = pygame.image.load("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/야구공.png")
pygame.display.set_icon(icon_image)

# FPS
clock = pygame.time.Clock()

# 커서 이미지 로드
cursor_image = pygame.image.load("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/커서.png")
# 커서 이미지 크기 조절
cursor_image = pygame.transform.scale(cursor_image, (50, 50))  # 원하는 크기로 조절

# 효과음 로드 및 설정
pygame.mixer.init()
click_sound = pygame.mixer.Sound("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/클릭 사운드.mp3")

# 배경 이미지 불러오기
background_img = pygame.image.load("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/야구장.jpg")
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

about_background_img=pygame.image.load("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/about배경.jpg")
about_background_img = pygame.transform.scale(about_background_img, (screen_width, screen_height))

# 숫자 입력 상자(UI 요소) 추가
input_rect = pygame.Rect(screen_width // 2 - 100, screen_height - 200, 200, 50)
input_font = pygame.font.SysFont(None, 40)
input_text = ""

class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def add_img(self, address):
        if address[-3:] == "png":
            self.image = pygame.image.load(address).convert_alpha()
        else:
            self.image = pygame.image.load(address)

    def change_size(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

    def show(self):
        screen.blit(self.image, (self.x, self.y))

    # 마우스를 클릭했을 때의 효과를 기능하게 하는 함수
    def is_clicked(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.rect.width and self.y <= mouse_y <= self.y + self.rect.height
        click_sound.play()

# 배경에 start 버튼 객체 생성
start = Object()
start.add_img("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/start.png")
start.change_size(200, 100)
start.x = screen_width - round(screen_width / 3) - round(start.rect.width / 2)
start.y = screen_height - start.rect.height - 80

# 배경에 about 버튼 객체 생성
about = Object()
about.add_img("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/about.png")
about.change_size(200, 100)
about.x = round(screen_width / 3) - round(about.rect.width / 2)
about.y = screen_height - about.rect.height - 80

# back 버튼 객체 생성
back = Object()
back.add_img("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/back.png")
back.change_size(150,70)
back.x = (screen_width - back.rect.width) // 2
back.y = screen_height - about.rect.height - 2

# 게임 화면에서의 back 버튼 객체 생성
back2 = Object()
back2.add_img("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/back1.png")
back2.change_size(100, 50)
back2.x = round(screen_width / 2 - round(about.rect.width / 2)) + 470
back2.y = screen_height - about.rect.height - 520

# 공 객체 생성
ball = Object()
ball.add_img("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/야구공.png")
ball.change_size(170, 170)
ball.x = round(screen_width / 4 - round(about.rect.width / 2))
ball.y = 50

# records 객체 생성
records = Object()
records.add_img("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/records.png")
records.change_size(420, 380)
records.x = round(screen_width / 5 - round(about.rect.width / 2))
records.y = 250

# result 객체 생성
result = Object()
result.add_img("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/result.png")
result.change_size(400, 370)
result.x = 550
result.y = 290

# menu 객체 생성
menu = Object()
menu.add_img("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/menu.png")

# homerun 객체 생성
homerun = Object()
homerun.add_img("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/홈런맨.png")
homerun.change_size(150, 150)


# 게임 룰 화면을 표시하는 함수
def show_game_rules():
    screen.fill((255, 255, 255))
    screen.blit(about_background_img, (0, 0))

    font = pygame.font.SysFont('Maplestory Bold', 100)
    rules_text1 = "Game Rules"
    rules_surface = font.render(rules_text1, True, (0, 0, 0))
    text_x = (screen_width - rules_surface.get_width()) // 2
    text_y = 50
    screen.blit(rules_surface, (text_x, 50))

    font = pygame.font.SysFont('hancomgothic', 30)
    additional_text = [
        "1. 0~9까지 서로 다른 숫자 세 자리를 맞춰야 한다",
        "2. 숫자와 위치가 전부 다르면 OUT",
        "3. 숫자는 맞고 위치가 다르면 BALL",
        "4. 숫자와 위치가 전부 맞으면 STRIKE",
        "!기회는 10번!"
    ]
    line_height = 80
    current_y = text_y + rules_surface.get_height() + 80

    for text in additional_text:
        text_surface = font.render(text, True, (0, 0, 0))
        text_x = (screen_width - text_surface.get_width()) // 2
        screen.blit(text_surface, (text_x, current_y))
        current_y += line_height

    back.show()

    pygame.display.update()

# 로직함수
def process_game_result(input_number, rn):
    s_cnt, b_cnt, o_cnt = 0, 0, 0

    for i in range(3):
        for j in range(3):
            if input_number[i] == str(rn[j]) and i == j:
                s_cnt += 1
            elif input_number[i] == str(rn[j]) and i != j:
                b_cnt += 1

    o_cnt = 3 - (s_cnt + b_cnt)

    if s_cnt == 0 and b_cnt == 0 and o_cnt == 3:
        result_text = "Out"
    else:
        result_text = f"{s_cnt} Strike, {b_cnt} Ball"

    return result_text, s_cnt, b_cnt, o_cnt

# 게임에서 졌을 때의 화면을 표시하는 함수
def lose_screen():
    screen.fill((255, 255, 255))
    screen.blit(about_background_img, (0, 0))

    font = pygame.font.SysFont('Maplestory Bold', 100)
    font1 = pygame.font.SysFont('Maplestory Bold', 50)
    lose_text1 = "You Lose"
    lose_text2 = "Try Again!"
    lose_text3 = "Answer is " + "".join(rn)
    
    rules_surface = font.render(lose_text1, True, (0, 0, 0))
    screen.blit(rules_surface, ((screen_width - rules_surface.get_width()) // 2, 150))
    rules_surface = font1.render(lose_text2, True, (0, 0, 0))
    screen.blit(rules_surface, ((screen_width - rules_surface.get_width()) // 2, 230))
    rules_surface = font1.render(lose_text3, True, (0, 0, 0))
    screen.blit(rules_surface, ((screen_width - rules_surface.get_width()) // 2, 310))

    back.change_size(150, 50)
    back.x = (screen_width - back.rect.width) // 2 - 400
    back.y = screen_height - about.rect.height + 20
    back.show()

    menu.change_size(150, 50)
    menu.x = 820
    menu.y = screen_height - about.rect.height + 20
    menu.show()

# 게임에서 이겼을 때 화면을 표시하는 함수
def win_screen():
    screen.fill((255, 255, 255))
    screen.blit(about_background_img, (0, 0))

    font = pygame.font.SysFont('Maplestory Bold', 100)
    font1 = pygame.font.SysFont('Maplestory Bold', 50)
    win_text1 = "You Win"
    win_text2 = "Home Run!"
    rules_surface = font.render(win_text1, True, (0, 0, 0))
    screen.blit(rules_surface, ((screen_width - rules_surface.get_width()) // 2, 150))
    rules_surface = font1.render(win_text2, True, (0, 0, 0))
    screen.blit(rules_surface, ((screen_width - rules_surface.get_width()) // 2, 230))
    homerun.x = (screen_width - rules_surface.get_width()) // 2
    homerun.y = 300
    homerun.show()

    back.change_size(150, 50)
    back.x = (screen_width - back.rect.width) // 2 - 400
    back.y = screen_height - about.rect.height + 20
    back.show()

    menu.change_size(150, 50)
    menu.x = 820
    menu.y = screen_height - about.rect.height + 20
    menu.show()


# 이벤트 루프
running = True # 게임 실행 여부를 나타내는 변수
show_game = False
in_about_screen = False # about 클릭 시의 화면 표시 여부를 나타내는 변수
show_rules = False  # 게임 룰 화면을 보여줄지 여부를 저장하는 변수
in_lose_screen = False  # 패배 화면 표시 여부를 나타내는 변수
in_win_screen = False # 승리 화면 표시 여부를 나타내는 변수

# 아래에 있는 'ball_objects' 리스트를 생성하여 3개의 공 객체 담기
ball_objects = []

# 시도 횟수를 저장하는 변수
attempts_count = 0

for i in [150, 410, 670]:
    ball_instance = Object()
    ball_instance.add_img("C:/Users/SM-PC/Desktop/코딧/2023여름방학프로젝트/야구공.png")
    ball_instance.change_size(170, 170)
    ball_instance.x = i
    ball_instance.y = 500
    ball_objects.append(ball_instance)
    
# 공 객체 생성 시 이미지 위에 그릴 숫자 표시용 폰트 설정
number_font = pygame.font.SysFont('Maplestory Bold', 100)
    
# records에 들어갈 기록
attempts = []
rn = []

while len(rn) < 3:
    num = random.randint(0, 9)  # 0부터 9까지의 무작위 정수 생성
    num_str = str(num)  # 정수를 문자열로 변환
    if num_str not in rn:  # 중복되지 않는 경우에만 리스트에 추가
        rn.append(num_str)

# 남은 중복을 피하며 숫자를 추가
while len(rn) < 3:
    num = random.randint(0, 9)
    num_str = str(num)
    if num_str not in rn:
        rn.append(num_str)

print(rn)  # 생성된 세 개의 숫자 출력

# 이벤트 루프 내부에서 게임 결과 메시지를 표시할 위치 지정
result_font = pygame.font.SysFont('Maplestory Bold', 50)
result_x = 500
result_y = 450
show_result = False
#show_records = True

while running:
    dt = clock.tick(60)

    # for 루프가 한 번 돌 때마다 게임에서 숫자 입력을 받음
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        # 키보드 이벤트 처리 (숫자 입력)
        elif event.type == pygame.KEYDOWN and show_game:
            
            # 숫자만 입력하고 최대 3자리까지 허용
            if event.unicode.isnumeric() and len(input_text) < 3:
                if event.unicode not in input_text:
                    
                    input_text += event.unicode
                    show_result = False

            if event.key >= pygame.K_0 and event.key <= pygame.K_9 and len(input_text) < 3:
                digit = event.key - pygame.K_0
                digit_str = str(digit)
                if digit_str not in input_text:
                    input_text += digit_str
                    show_result = False

            # 백스페이스 키가 눌렸을 때
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]  # 마지막 문자 제거
                show_result = False

            # 엔터 키로 숫자 입력 완료
            elif event.key == pygame.K_RETURN and len(input_text) == 3:
                # 시도 횟수 증가
                attempts_count += 1

                # 시도 횟수가 10번일 경우, 게임 패배 화면으로 전환
                if attempts_count == 11:
                    pygame.time.delay(500)
                    in_lose_screen = True # 패배 화면 상태로 설정
                    pygame.display.update()  # 화면을 업데이트
                    attempts_count = 0 # 게임 초기화
                    break # 숫자 입력받는 for문에서 빠져나옴
                
                # 입력된 숫자를 처리하는 로직 추가
                input_number = input_text
                result_text, s_cnt, b_cnt, o_cnt = process_game_result(input_number, rn)

                # 정답을 맞춘 시도를 기록에 추가
                attempts.append(f"{attempts_count}. {input_number} : {result_text}")

                # 게임 결과를 화면에 표시
                if s_cnt == 0 and b_cnt == 0:
                    result_text = "Out"
                elif s_cnt==3:
                    result_text = "WIN!"
                    show_result = True
                else:
                    result_text = f"{s_cnt} Strike    {b_cnt} Ball"

                result_surface = result_font.render(result_text, True, (0, 0, 0))
                result_x = result.x + (result.rect.width - result_surface.get_width()) // 2
                result_y = result.y + (result.rect.height - result_surface.get_height()) // 2-20
                screen.blit(result_surface, (result_x, result_y))
                                
                pygame.display.update()

                # 스트라이크가 세 개일 경우 WIN! 띄우고 프로그램 종료
                if s_cnt == 3 and event.key == pygame.K_RETURN:
                    pygame.time.delay(500)  # 결과 표시를 위한 시간 지연
                    running = True  # 프로그램 일단 유지
                    in_win_screen = True
                    pygame.display.update()  # 화면을 업데이트
                    attempts_count = 0  # 게임 초기화
                    break  # 숫자 입력받는 for문에서 빠져나옴


                # 이미지 위에 숫자 표시
                number_surface = number_font.render(str(input_number), True, (0,0,0))
                show_result = True
                input_text = ""  # 입력 초기화


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if start.is_clicked(mouse_x, mouse_y):
                    show_game = True
                    screen.fill((255, 255, 255))
                    screen.blit(background_img, (0, 0))
                    show_player12 = True  # 플레이어 선택 화면을 보여주기 위한 플래그 설정
                    click_sound.play()  # 마우스 클릭 시 소리 재생

                elif about.is_clicked(mouse_x, mouse_y):
                    in_about_screen = True
                    show_game = False
                    click_sound.play()

                elif back.is_clicked(mouse_x, mouse_y):
                    in_about_screen = False
                    show_game = False
                    click_sound.play()

                # menu 버튼을 눌렀을 때
                elif menu.is_clicked(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                    rn = [str(random.randrange(0, 10, 1)) for _ in range(3)]
                    # 게임 시작 화면
                    in_win_screen = False
                    in_lose_screen = False
                    in_about_screen = False
                    show_game = False
                    input_text = ""
                    result_text = ""
                    attempts = []
                    attempts_count = 0
                    click_sound.play()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and in_about_screen:
                in_about_screen = False
                
    if not in_lose_screen:
        if not in_win_screen:
            # 게임 시작 화면
            if not in_about_screen and not show_game:
                screen.blit(background_img, (0, 0))
                start.show()
                about.show()

                start_text = font.render("Number Baseball Game", True, (0, 0, 0))
                text_width, text_height = font.size("Number Baseball Game")
                text_x = (screen_width - text_width) // 2
                text_y = (screen_height - text_height) // 10
                screen.blit(start_text, (text_x, text_y))

            # about 버튼을 눌렀을 때 (in_about_screen = True)
            elif in_about_screen:
                show_game_rules()
                pygame.display.flip()

            # start 버튼을 눌렀을 때 (game 진행 화면) (show_game = True, in_about_screen = False)
            elif show_game:
                screen.fill((255, 255, 255))
                screen.blit(background_img, (0, 0))
                menu.change_size(90, 30)
                menu.x = 15
                menu.y = screen_height - about.rect.height - 530
                menu.show()
                if menu.is_clicked(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                    rn = [str(random.randrange(0, 10, 1)) for _ in range(3)]
                    attempts = []
                    input_text = ""
                    result_text = ""
                    attempts_count = 0

                # 입력된 숫자를 화면에 그려줄 위치와 크기 설정
                number_x = 220
                number_y = 100
                number_width = 260
                number_height = 170
                # 공 세개를 화면 상단에 그림
                for i in [150, 410, 670]:
                    ball.x = i
                    ball.show()
                # 입력받은 숫자들을 공 위에 그림
                for j in range(len(input_text)):
                    number_surface = number_font.render(input_text[j], True, (0, 0, 0))
                    screen.blit(number_surface, (number_x + j * number_width, number_y))

                records.show()
                result.show()

            if show_result:
                result_surface = result_font.render(result_text, True, (0, 0, 0))
                screen.blit(result_surface, (result_x, result_y))

            # records 객체에 시도 기록 표시
            if attempts:
                records_font = pygame.font.SysFont(None, 30)
                records_surface = records_font.render("", True, (0, 0, 0))
                records_x = records.x + (records.rect.width - records_surface.get_width()) // 2 - 120
                records_y = records.y + (records.rect.height - records_surface.get_height()) // 2 + 210

                # 시도 기록을 일정 간격을 두고 표시
                line_height = 30  # 각 줄의 높이
                max_display_lines = 10  # 최대 표시할 줄 수

                for i in range(max(len(attempts) - max_display_lines, 0), len(attempts)):
                    attempts_surface = records_font.render(attempts[i], True, (0, 0, 0))
                    screen.blit(attempts_surface, (records_x, records_y + (i - max_display_lines) * line_height))

        else:
            win_screen()

            # 승리 화면에서 back 버튼을 누르면 다시 게임 화면으로 돌아가기
            if back.is_clicked(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                in_win_screen = False
                show_game = True

            # 승리 화면에서 menu 버튼을 누르면 게임 초기화
            if menu.is_clicked(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                rn = [str(random.randrange(0, 10, 1)) for _ in range(3)]
                show_result = False
                attempts = []
                input_text = ""
                result_text = ""

    else:
        lose_screen()

        # 패배 화면에서 back 버튼을 누르면 다시 게임 화면으로 돌아가기
        if back.is_clicked(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            in_lose_screen = False
            show_game = True

        # 패배 화면에서 menu 버튼을 누르면 게임 초기화
        if menu.is_clicked(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            rn = [str(random.randrange(0, 10, 1)) for _ in range(3)]
            show_result = False
            attempts = []
            input_text = ""
            result_text = ""


    # 현재 마우스 커서 위치 얻기
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # 마우스 커서 이미지를 그리기
    screen.blit(cursor_image, (mouse_x, mouse_y))
    pygame.display.update()

# pygame 종료
pygame.quit()
