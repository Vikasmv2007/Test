import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interactive Calculator - Pygame")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
LIGHT_CORAL = (240, 128, 128)

# Fonts
font_large = pygame.font.Font(None, 36)
font_medium = pygame.font.Font(None, 28)
font_small = pygame.font.Font(None, 20)

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

class Button:
    """Button class for interactive elements."""
    def __init__(self, x, y, width, height, text, color, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.hovered = False

    def draw(self, surface):
        color = tuple(min(c + 30, 255) for c in self.color) if self.hovered else self.color
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        text_surf = font_medium.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def update_hover(self, pos):
        self.hovered = self.rect.collidepoint(pos)

class InputBox:
    """Input box for text entry."""
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = False
        self.color_inactive = GRAY
        self.color_active = LIGHT_BLUE
        self.color = self.color_inactive

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    return self.text
                else:
                    self.text += event.unicode
        return None

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        text_surf = font_medium.render(self.text, True, BLACK)
        surface.blit(text_surf, (self.rect.x + 5, self.rect.y + 5))

class Calculator:
    def __init__(self):
        self.mode = "main_menu"  # main_menu, basic, scientific, file
        self.result = ""
        self.input_boxes = {}
        self.buttons = {}
        self.create_main_menu_buttons()

    def create_main_menu_buttons(self):
        self.buttons = {
            "basic": Button(100, 200, 400, 80, "1. Basic Calculator", LIGHT_GREEN),
            "scientific": Button(100, 320, 400, 80, "2. Scientific Calculator", LIGHT_BLUE),
            "file": Button(100, 440, 400, 80, "3. File Mode", LIGHT_CORAL),
            "quit": Button(100, 560, 400, 80, "4. Quit", GRAY),
        }

    def create_basic_mode_buttons(self):
        self.buttons = {}
        self.input_boxes = {
            "num1": InputBox(100, 120, 400, 40),
            "num2": InputBox(100, 200, 400, 40),
        }
        
        button_data = [
            ("1", 100, 280, 80, 60, LIGHT_GREEN),
            ("2", 190, 280, 80, 60, LIGHT_GREEN),
            ("3", 280, 280, 80, 60, LIGHT_GREEN),
            ("4", 370, 280, 80, 60, LIGHT_GREEN),
            ("5", 460, 280, 80, 60, LIGHT_GREEN),
            ("6", 100, 360, 80, 60, LIGHT_GREEN),
            ("Clear", 190, 360, 170, 60, DARK_GRAY),
            ("Back", 370, 360, 170, 60, LIGHT_CORAL),
        ]
        
        for text, x, y, w, h, color in button_data:
            self.buttons[text] = Button(x, y, w, h, text, color)

    def create_scientific_mode_buttons(self):
        self.buttons = {}
        self.input_boxes = {
            "num": InputBox(100, 120, 400, 40),
        }
        
        button_data = [
            ("√", 50, 200, 70, 60, LIGHT_BLUE),
            ("sin", 130, 200, 70, 60, LIGHT_BLUE),
            ("cos", 210, 200, 70, 60, LIGHT_BLUE),
            ("tan", 290, 200, 70, 60, LIGHT_BLUE),
            ("log", 370, 200, 70, 60, LIGHT_BLUE),
            ("ln", 450, 200, 70, 60, LIGHT_BLUE),
            ("e^x", 50, 280, 70, 60, LIGHT_BLUE),
            ("x!", 130, 280, 70, 60, LIGHT_BLUE),
            ("|x|", 210, 280, 70, 60, LIGHT_BLUE),
            ("sin⁻¹", 290, 280, 70, 60, LIGHT_BLUE),
            ("cos⁻¹", 370, 280, 70, 60, LIGHT_BLUE),
            ("tan⁻¹", 450, 280, 70, 60, LIGHT_BLUE),
            ("Clear", 100, 380, 150, 60, DARK_GRAY),
            ("Back", 350, 380, 150, 60, LIGHT_CORAL),
        ]
        
        for text, x, y, w, h, color in button_data:
            self.buttons[text] = Button(x, y, w, h, text, color)

    def create_file_mode_buttons(self):
        self.buttons = {}
        self.input_boxes = {
            "input_file": InputBox(100, 120, 400, 40),
            "output_file": InputBox(100, 200, 400, 40),
        }
        
        button_data = [
            ("Read & Process", 100, 280, 400, 60, LIGHT_GREEN),
            ("Back", 100, 380, 400, 60, LIGHT_CORAL),
        ]
        
        for text, x, y, w, h, color in button_data:
            self.buttons[text] = Button(x, y, w, h, text, color)

    def perform_basic_operation(self, num1, num2, choice):
        try:
            num1, num2 = float(num1), float(num2)
            if choice == '1':
                return f"{num1} + {num2} = {num1 + num2}"
            elif choice == '2':
                return f"{num1} - {num2} = {num1 - num2}"
            elif choice == '3':
                return f"{num1} * {num2} = {num1 * num2}"
            elif choice == '4':
                if num2 != 0:
                    return f"{num1} / {num2} = {num1 / num2}"
                else:
                    return "Error: Division by zero!"
            elif choice == '5':
                if num2 != 0:
                    return f"{num1} % {num2} = {num1 % num2}"
                else:
                    return "Error: Modulo by zero!"
            elif choice == '6':
                return f"{num1} ** {num2} = {num1 ** num2}"
        except ValueError:
            return "Error: Invalid input!"
        return "Error: Unknown operation!"

    def perform_scientific_operation(self, num, choice):
        try:
            num = float(num)
            if choice == '√':
                return f"√{num} = {math.sqrt(num)}"
            elif choice == 'sin':
                return f"sin({num}°) = {math.sin(math.radians(num))}"
            elif choice == 'cos':
                return f"cos({num}°) = {math.cos(math.radians(num))}"
            elif choice == 'tan':
                return f"tan({num}°) = {math.tan(math.radians(num))}"
            elif choice == 'log':
                return f"log₁₀({num}) = {math.log10(num)}"
            elif choice == 'ln':
                return f"ln({num}) = {math.log(num)}"
            elif choice == 'e^x':
                return f"e^{num} = {math.exp(num)}"
            elif choice == 'x!':
                return f"{num}! = {math.factorial(int(num))}"
            elif choice == '|x|':
                return f"|{num}| = {abs(num)}"
            elif choice == 'sin⁻¹':
                return f"sin⁻¹({num}) = {math.degrees(math.asin(num))}°"
            elif choice == 'cos⁻¹':
                return f"cos⁻¹({num}) = {math.degrees(math.acos(num))}°"
            elif choice == 'tan⁻¹':
                return f"tan⁻¹({num}) = {math.degrees(math.atan(num))}°"
        except (ValueError, OverflowError):
            return "Error: Invalid input or calculation!"
        return "Error: Unknown operation!"

    def draw_main_menu(self, surface):
        surface.fill(WHITE)
        title = font_large.render("Calculator - Select Mode", True, BLACK)
        surface.blit(title, (120, 100))
        
        for button in self.buttons.values():
            button.draw(surface)

    def draw_basic_mode(self, surface):
        surface.fill(WHITE)
        title = font_large.render("Basic Calculator", True, BLACK)
        surface.blit(title, (150, 20))
        
        # Labels
        label1 = font_medium.render("Number 1:", True, BLACK)
        label2 = font_medium.render("Number 2:", True, BLACK)
        surface.blit(label1, (100, 90))
        surface.blit(label2, (100, 170))
        
        # Input boxes
        self.input_boxes["num1"].draw(surface)
        self.input_boxes["num2"].draw(surface)
        
        # Operations
        op_label = font_medium.render("Operations: 1=Add, 2=Sub, 3=Mul, 4=Div, 5=Mod, 6=Power", True, BLACK)
        surface.blit(op_label, (20, 250))
        
        # Buttons
        for button in self.buttons.values():
            button.draw(surface)
        
        # Result
        if self.result:
            result_surf = font_small.render(self.result, True, BLACK)
            surface.blit(result_surf, (50, 480))

    def draw_scientific_mode(self, surface):
        surface.fill(WHITE)
        title = font_large.render("Scientific Calculator", True, BLACK)
        surface.blit(title, (120, 20))
        
        label = font_medium.render("Enter Number:", True, BLACK)
        surface.blit(label, (100, 90))
        
        self.input_boxes["num"].draw(surface)
        
        for button in self.buttons.values():
            button.draw(surface)
        
        if self.result:
            result_surf = font_small.render(self.result, True, BLACK)
            surface.blit(result_surf, (50, 480))

    def draw_file_mode(self, surface):
        surface.fill(WHITE)
        title = font_large.render("File Mode", True, BLACK)
        surface.blit(title, (200, 20))
        
        label1 = font_medium.render("Input File:", True, BLACK)
        label2 = font_medium.render("Output File:", True, BLACK)
        surface.blit(label1, (100, 90))
        surface.blit(label2, (100, 170))
        
        self.input_boxes["input_file"].draw(surface)
        self.input_boxes["output_file"].draw(surface)
        
        for button in self.buttons.values():
            button.draw(surface)
        
        if self.result:
            result_surf = font_small.render(self.result, True, BLACK)
            surface.blit(result_surf, (50, 320))

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        
        # Update button hover states
        for button in self.buttons.values():
            button.update_hover(mouse_pos)
        
        # Input boxes
        for input_box in self.input_boxes.values():
            input_box.handle_event(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.mode == "main_menu":
                if self.buttons["basic"].is_clicked(mouse_pos):
                    self.mode = "basic"
                    self.create_basic_mode_buttons()
                elif self.buttons["scientific"].is_clicked(mouse_pos):
                    self.mode = "scientific"
                    self.create_scientific_mode_buttons()
                elif self.buttons["file"].is_clicked(mouse_pos):
                    self.mode = "file"
                    self.create_file_mode_buttons()
                elif self.buttons["quit"].is_clicked(mouse_pos):
                    return False
            
            elif self.mode == "basic":
                if "Back" in self.buttons and self.buttons["Back"].is_clicked(mouse_pos):
                    self.mode = "main_menu"
                    self.create_main_menu_buttons()
                    self.result = ""
                elif "Clear" in self.buttons and self.buttons["Clear"].is_clicked(mouse_pos):
                    self.input_boxes["num1"].text = ""
                    self.input_boxes["num2"].text = ""
                    self.result = ""
                else:
                    for op in ['1', '2', '3', '4', '5', '6']:
                        if op in self.buttons and self.buttons[op].is_clicked(mouse_pos):
                            num1 = self.input_boxes["num1"].text
                            num2 = self.input_boxes["num2"].text
                            if num1 and num2:
                                self.result = self.perform_basic_operation(num1, num2, op)
            
            elif self.mode == "scientific":
                if "Back" in self.buttons and self.buttons["Back"].is_clicked(mouse_pos):
                    self.mode = "main_menu"
                    self.create_main_menu_buttons()
                    self.result = ""
                elif "Clear" in self.buttons and self.buttons["Clear"].is_clicked(mouse_pos):
                    self.input_boxes["num"].text = ""
                    self.result = ""
                else:
                    for op in ['√', 'sin', 'cos', 'tan', 'log', 'ln', 'e^x', 'x!', '|x|', 'sin⁻¹', 'cos⁻¹', 'tan⁻¹']:
                        if op in self.buttons and self.buttons[op].is_clicked(mouse_pos):
                            num = self.input_boxes["num"].text
                            if num:
                                self.result = self.perform_scientific_operation(num, op)
            
            elif self.mode == "file":
                if "Back" in self.buttons and self.buttons["Back"].is_clicked(mouse_pos):
                    self.mode = "main_menu"
                    self.create_main_menu_buttons()
                    self.result = ""
                elif "Read & Process" in self.buttons and self.buttons["Read & Process"].is_clicked(mouse_pos):
                    self.process_file()
        
        return True

    def process_file(self):
        input_file = self.input_boxes["input_file"].text or "input.txt"
        output_file = self.input_boxes["output_file"].text or "output.txt"
        
        try:
            with open(input_file, 'r') as f:
                num1 = f.readline().strip()
                num2 = f.readline().strip()
                choice = f.readline().strip()
            
            result = self.perform_basic_operation(num1, num2, choice)
            with open(output_file, 'a') as f:
                f.write(result + "\n")
            
            self.result = f"Processed! Result: {result}"
        except FileNotFoundError:
            self.result = f"Error: File not found!"
        except Exception as e:
            self.result = f"Error: {str(e)}"

    def draw(self, surface):
        if self.mode == "main_menu":
            self.draw_main_menu(surface)
        elif self.mode == "basic":
            self.draw_basic_mode(surface)
        elif self.mode == "scientific":
            self.draw_scientific_mode(surface)
        elif self.mode == "file":
            self.draw_file_mode(surface)

def main():
    calc = Calculator()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                running = calc.handle_event(event)
        
        calc.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
