class Button:
    def __init__(self, text: str, pygame, screen, button_padding: int = 100, button_height: int = 40, button_width: int = 130, font_size: int = 28) -> None:
        self.text = text
        self.pygame = pygame
        self.screen = screen
        self.button_padding = button_padding
        self.button_height = button_height
        self.button_width = button_width
        self.button = self.pygame.Rect(self.button_padding, self.button_height, self.button_width, self.button_height)

        self.font_size = font_size
        font =  self.pygame.font.Font(None, self.font_size)
        self.font = font.render(self.text, True, (255, 255, 255))
    
    def update(self) -> None:
        self.pygame.draw.rect(self.screen, (73, 75, 222), self.button)
        self.screen.blit(self.font, (self.button.left + self.button_width // 2 - self.font.get_width() // 2, self.button.top + self.button_height // 2 - self.font.get_height() // 2))

    def action(self) -> None:
        print(f"Button {self.text} clicked")
