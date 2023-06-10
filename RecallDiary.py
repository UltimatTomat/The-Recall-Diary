import pygame
import sys
import datetime

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 400))
icon = pygame.image.load("Icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("The Recall Diary")

clock = pygame.time.Clock()

black = (0, 0, 0)
gray = (44, 44, 44)
red = (255, 0, 0)
white = (255, 255, 255)
colour_active = (98, 90, 216)
colour_passive = (114, 41, 171)

base_font = pygame.font.Font(None, 32)

write = pygame.image.load("Buttons/Write.png").convert_alpha()
write_pressed = pygame.image.load("Buttons/WritePressed.png").convert_alpha()
write_rect = write.get_rect(center = (220, 150))
search = pygame.image.load("Buttons/Search.png").convert_alpha()
search_pressed = pygame.image.load("Buttons/SearchPressed.png").convert_alpha()
search_rect = search.get_rect(center = (580, 150))

background = pygame.image.load("Backgrounds/Background1.png").convert_alpha()
background_rect = background.get_rect(topleft = (25, 25))
background_overlay = pygame.image.load("Backgrounds/Background3.png").convert_alpha()
background_overlay_rect = background_overlay.get_rect(bottomleft = (0, 400))
cancel = pygame.image.load("Buttons/Cancel.png").convert_alpha()
cancel_pressed = pygame.image.load("Buttons/CancelPressed.png").convert_alpha()
cancel_rect = cancel.get_rect(center = (500, 300))

message_text = base_font.render("What did you do today?", True, white)
input_rect = pygame.Rect(50, 90, 140, 32)
typer = pygame.Rect(0, 0, 2, 20)
submit = pygame.image.load("Buttons/Submit.png").convert_alpha()
submit_pressed = pygame.image.load("Buttons/SubmitPressed.png").convert_alpha()
submit_rect = submit.get_rect(center = (300, 300))

result_box = pygame.image.load("Backgrounds/Background2.png").convert_alpha()
result_box_rect = result_box.get_rect(center = (400, 167))
message_2_text = base_font.render("Date:", True, white)
input_rect_2 = pygame.Rect(120, 46, 128, 32)
search_2 = pygame.image.load("Buttons/Search2.png").convert_alpha()
search_2_pressed = pygame.image.load("Buttons/Search2Pressed.png").convert_alpha()
search_2_rect = search_2.get_rect(center = (300, 300))
search_2_mode = search_2

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
active = False
active2 = False
colour = colour_passive
submit_mode = submit
write_mode = write
search_mode = search
cancel_mode = cancel
lines = 1
current_line = 0
result_lines = 1
message = ["", "", "", ""]
message2 = ""
result_text = ""
search_2_tick = 0
submit_tick  = 0
search_2_available = True
submit_available = True
stage = 1

def daysBetween(current_date, date_then):
    return (current_date - date_then).days

while True:
    if stage == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if write_rect.collidepoint(pygame.mouse.get_pos()):
            write_mode = write_pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    stage = 2
        else:
            write_mode = write
        
        if search_rect.collidepoint(pygame.mouse.get_pos()):
            search_mode = search_pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    stage = 3
        else:
            search_mode = search
        
        screen.fill(gray)
        screen.blit(background, background_rect)
        screen.blit(background_overlay, background_overlay_rect)
        screen.blit(write_mode, write_rect)
        screen.blit(search_mode, search_rect)
        
    elif stage == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        if len(message[current_line]) == 0 and current_line > 0:
                            current_line -= 1
                            lines -= 1
                            input_rect.h = 32 * lines
                        else:
                            message[current_line] = message[current_line][:-1]
                    elif event.key == pygame.K_RETURN:
                        if current_line < 3:
                            current_line += 1
                        if lines < 4:
                            lines += 1
                        input_rect.h = 32 * lines
                    else:
                        message[current_line] += event.unicode

                        if text_surface1.get_width() > 690 or text_surface2.get_width() > 690 or text_surface3.get_width() > 690 or text_surface4.get_width() > 690:
                            if current_line < 3:
                                extra_char = message[current_line][-2]
                                message[current_line] = message[current_line][:-2]
                            else:
                                message[current_line] = message[current_line][:-1]

                            if current_line < 3:
                                current_line += 1
                            if lines < 4:
                                lines += 1

                            input_rect.h = 32 * lines

                            if current_line < 3:
                                message[current_line] += extra_char + event.unicode

        if submit_rect.collidepoint(pygame.mouse.get_pos()):
            submit_mode = submit_pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0] and submit_available:
                    if len(message[0]) > 0:
                        lines_w_content = 1
                        if len(message[1]) > 0:
                            lines_w_content = 2
                            if len(message[2]) > 0:
                                lines_w_content = 3
                                if len(message[3]) > 0:
                                    lines_w_content = 4

                    current_RecallDiary = open("RecallDiary.txt").readlines()
                    new_RecallDiary = []
                    another_new_RecallDiary = []

                    if len(current_RecallDiary) == 0:
                        with open("RecallDiary.txt", "a") as txt:
                            txt.write(f"[{current_date}]")
                            for x in range(lines_w_content):
                                txt.write(f"\n{message[x]}")
                    elif f"[{current_date}]\n" in current_RecallDiary:
                        for x in range(current_RecallDiary.index(f"[{current_date}]\n")):
                            new_RecallDiary.append(current_RecallDiary[x])
                        with open("RecallDiary.txt", "w") as txt:
                            for x in new_RecallDiary:
                                txt.write(x)
                        with open("RecallDiary.txt", "a") as txt:
                            txt.write(f"[{current_date}]")
                            for x in range(lines_w_content):
                                txt.write(f"\n{message[x]}")
                    else:
                        with open("RecallDiary.txt", "a") as txt:
                            txt.write(f"\n[{current_date}]")
                            for x in range(lines_w_content):
                                txt.write(f"\n{message[x]}")

                        current_RecallDiary = open("RecallDiary.txt").readlines()
                        for x in current_RecallDiary:
                            if x.startswith("["):
                                another_new_RecallDiary.append(x)

                        date_then = another_new_RecallDiary[-2][:-2]
                        date_then = date_then[1:]
                        current_date_new = current_date.split("-")
                        date_then = date_then.split("-")
                        current_date_new = datetime.date(int(current_date_new[0]), int(current_date_new[1]), int(current_date_new[2]))
                        date_then = datetime.date(int(date_then[0]), int(date_then[1]), int(date_then[2]))
                        empty_days = daysBetween(current_date_new, date_then)
                        if empty_days > 1:
                            for x in range(current_RecallDiary.index(f"[{current_date}]\n")):
                                new_RecallDiary.append(current_RecallDiary[x])
                            with open("RecallDiary.txt", "w") as txt:
                                for x in new_RecallDiary:
                                    txt.write(x)
                            with open("RecallDiary.txt", "a") as txt:
                                first = True
                                for x in range(empty_days - 1, 0, -1):
                                    if first:
                                        txt.write(f"[{current_date_new - datetime.timedelta(days=x)}]\n...")
                                        first = False
                                    else:
                                        txt.write(f"\n[{current_date_new - datetime.timedelta(days=x)}]\n...")
                            with open("RecallDiary.txt", "a") as txt:
                                txt.write(f"\n[{current_date}]")
                                for x in range(lines_w_content):
                                    txt.write(f"\n{message[x]}")
                            
                    submit_available = False
                    active = False
                    lines = 1
                    current_line = 0
                    input_rect.h = 32
                    message = ["", "", "", ""]
        else:
            submit_mode = submit

        if submit_available == False:
            submit_tick += 1
        if submit_tick > 20:
            submit_available = True
            submit_tick = 0
            
        if cancel_rect.collidepoint(pygame.mouse.get_pos()):
            cancel_mode = cancel_pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    active = False
                    lines = 1
                    current_line = 0
                    input_rect.h = 32
                    message = ["", "", "", ""]
                    stage = 1
        else:
            cancel_mode = cancel

        text_surface1 = base_font.render(message[0], True, white)
        text_surface2 = base_font.render(message[1], True, white)
        text_surface3 = base_font.render(message[2], True, white)
        text_surface4 = base_font.render(message[3], True, white)
        input_rect.w = max(250, max(text_surface1.get_width(), text_surface2.get_width(), text_surface3.get_width(), text_surface4.get_width()) + 12)
        if current_line == 0:
            typer.topright = (text_surface1.get_width() + 58, input_rect.y + 5)
        elif current_line == 1:
            typer.topright = (text_surface2.get_width() + 58, input_rect.y + 37)
        elif current_line == 2:
            typer.topright = (text_surface3.get_width() + 58, input_rect.y + 69)
        else:
            typer.topright = (text_surface4.get_width() + 58, input_rect.y + 101)

        if active:
            colour = colour_active
        else:
            colour = colour_passive

        screen.fill(gray)
        screen.blit(background, background_rect)
        screen.blit(message_text, (50, 50))
        screen.blit(text_surface1, (input_rect.x + 5, input_rect.y + 5))
        screen.blit(text_surface2, (input_rect.x + 5, input_rect.y + 37))
        screen.blit(text_surface3, (input_rect.x + 5, input_rect.y + 69))
        screen.blit(text_surface4, (input_rect.x + 5, input_rect.y + 101))
        pygame.draw.rect(screen, colour, input_rect, 2)
        if active:
            pygame.draw.rect(screen, red, typer)
        screen.blit(submit_mode, submit_rect)
        screen.blit(cancel_mode, cancel_rect)
        
    elif stage == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_2.collidepoint(event.pos):
                    active2 = True
                else:
                    active2 = False
                    
            if event.type == pygame.KEYDOWN:
                if active2:
                    if event.key == pygame.K_BACKSPACE:
                        if len(message2) != 0:
                            message2 = message2[:-1]
                    else:
                        if len(message2) < 10:
                            message2 += event.unicode
            
        if search_2_rect.collidepoint(pygame.mouse.get_pos()):
            search_2_mode = search_2_pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0] and search_2_available:
                    result_text_surface_line1 = base_font.render("", True, white)
                    result_text_surface_line2 = base_font.render("", True, white)
                    result_text_surface_line3 = base_font.render("", True, white)
                    result_text_surface_line4 = base_font.render("", True, white)
                    current_RecallDiary = open("RecallDiary.txt").readlines()
                    if f"[{message2}]\n" in current_RecallDiary:
                        result_start = current_RecallDiary.index(f"[{message2}]\n") + 1
                        index = result_start
                        result_lines = 0
                        while True:
                            try:
                                if current_RecallDiary[index].startswith("["):
                                    break
                                else:
                                    index += 1
                                    result_lines += 1
                            except:
                                break
                        if result_lines > 1:
                            result_text = []
                            for x in range(result_start, result_start + result_lines):
                                result_text.append(current_RecallDiary[x])
                            for x in range(len(result_text)):
                                if result_text[x].endswith("\n"):
                                    result_text[x] = result_text[x][:-1]
                            result_text_surface_line1 = base_font.render(result_text[0], True, white)
                            result_text_surface_line2 = base_font.render(result_text[1], True, white)
                            if result_lines > 2:
                                result_text_surface_line3 = base_font.render(result_text[2], True, white)
                            if result_lines > 3:
                                result_text_surface_line4 = base_font.render(result_text[3], True, white)
                        else:
                            result_text = current_RecallDiary[result_start]  
                    else:
                        result_lines = 1
                        result_text = "Date not found..."
                    search_2_available = False
        else:
            search_2_mode = search_2
        
        if cancel_rect.collidepoint(pygame.mouse.get_pos()):
            cancel_mode = cancel_pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    active2 = False
                    message2 = ""
                    result_text = ""
                    result_lines = 1
                    result_text_surface_line1 = base_font.render("", True, white)
                    result_text_surface_line2 = base_font.render("", True, white)
                    result_text_surface_line3 = base_font.render("", True, white)
                    result_text_surface_line4 = base_font.render("", True, white)
                    stage = 1
        else:
            cancel_mode = cancel

        if search_2_available == False:
            search_2_tick += 1
        if search_2_tick > 20:
            search_2_available = True
            search_2_tick = 0
        
        text_surface_date = base_font.render(message2, True, white)
        typer.topright = (text_surface_date.get_width() + 128, input_rect_2.y + 5)
        
        if active2:
            colour = colour_active
        else:
            colour = colour_passive
        
        if result_lines == 1:
            result_text_surface = base_font.render(result_text, True, white)
    
        screen.fill(gray)
        screen.blit(background, background_rect)
        screen.blit(result_box, result_box_rect)
        screen.blit(search_2_mode, search_2_rect)
        screen.blit(cancel_mode, cancel_rect)
        screen.blit(message_2_text, (50, 50))
        pygame.draw.rect(screen, colour, input_rect_2, 2)
        if active2:
            pygame.draw.rect(screen, red, typer)
        screen.blit(text_surface_date, (input_rect_2.x + 5, input_rect_2.y + 5))
        if result_lines > 1:
            screen.blit(result_text_surface_line1, (result_box_rect.left + 12, result_box_rect.top +  15))
            screen.blit(result_text_surface_line2, (result_box_rect.left + 12, result_box_rect.top + 47))
            screen.blit(result_text_surface_line3, (result_box_rect.left + 12, result_box_rect.top + 79))
            screen.blit(result_text_surface_line4, (result_box_rect.left + 12, result_box_rect.top + 111))
        else:
            screen.blit(result_text_surface, (result_box_rect.left + 12, result_box_rect.top + 15))

    pygame.display.update()
    clock.tick(60)