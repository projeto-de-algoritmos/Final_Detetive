from components.texto import Texto

class MainPage:
    def __init__(self, 
                 pygame, 
                 screen, 
                 background_image_path: str = "assets/Interrogation_room.png", 
                 text: str='Bem vindo!',
                 portrait_path: str = "assets/None.png") -> None:
        self.pygame = pygame
        self.screen = screen 

        self.portrait_image = self.pygame.image.load(portrait_path)
        self.portrait_image = self.pygame.transform.scale(self.portrait_image, (200, 200))

        self.text_box = self.pygame.Rect(0, self.screen.get_height() - 150, 500, 150)
        self.color_box = self.pygame.Surface((self.text_box.width, self.text_box.height))
        self.color_box.fill((88, 90, 219))
        self.color_box.set_alpha(95) 

        self.background_image = self.pygame.image.load(background_image_path)

        text_padding = 10
        self.text = Texto(
            text, 
            self.pygame,
            self.screen, 
            self.text_box.left + text_padding, 
            self.text_box.top + text_padding, 
            self.text_box.width - 2 * text_padding, 
            self.text_box.height - 2 * text_padding,
            font_size=22)
        self.text_enter = Texto(
            "Aperte enter para continuar", 
            self.pygame,
            self.screen, 
            self.text_box.left + 360, 
            self.text_box.top +  140, 
            self.text_box.width - 2 * text_padding, 
            self.text_box.height - 2 * text_padding,
            font_size=15)


    def update(self) -> None:
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.portrait_image, (150, 150))
        
        self.screen.blit(self.color_box, self.text_box)
        
        text_image = self.text.create_wrapped_text_surface(self.text.text,self.text.font.render(self.text.text, True, (255, 255, 255)) )
        self.screen.blit(text_image, self.text.text_rect)

        text_enter = self.text_enter.create_wrapped_text_surface(self.text_enter.text,self.text_enter.font.render(self.text_enter.text, True, (255, 255, 255)) )
        self.screen.blit(text_enter, self.text_enter.text_rect)
