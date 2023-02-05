class Texto:
    def __init__(self, text: str, pygame, screen, left, top, width, height, font_size: int = 28) -> None:
        self.text = text
        self.pygame = pygame
        self.screen = screen
        self.text_rect = self.pygame.Rect(left, top, width, height)
        self.font_size = font_size
        self.font = self.pygame.font.Font(None, self.font_size)


    def create_wrapped_text_surface(self, text, 
                                text_surface,
                                font_color=(255, 255, 255)):
        pos = [20,350]
        self.font = self.pygame.font.Font(None, self.font_size)
        words = [word.split(' ') for word in text]
        space = self.font.size(' ')[0]
        max_width = 50
        x,y = pos
        for line in words:
            for word in line:
                word_surface = self.font.render(word, 0, font_color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                text_surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
    
        return text_surface
