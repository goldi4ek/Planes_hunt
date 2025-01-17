from game import *


class Menu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Z-Plane Hunt')
        self.menuscreen = pygame.display.set_mode(settings.RESOLUTION, flags=pygame.SCALED)
        self.bg = pygame.transform.scale(pygame.image.load('assets/menu/background.png').convert_alpha(), [720, 480])

        # -------------------------------------------sounds----------------------------------------
        self.is_muted = None
        self.music_volume = 0.3
        self.easy_mode_music = pygame.mixer.Sound('assets/sounds/Hatsune Miku - Ievan Polkka (mp3store.cc).mp3')
        self.normal_mode_music = pygame.mixer.Sound('assets/sounds/undertale_050. Metal Crusher.mp3')
        self.hard_mode_music = pygame.mixer.Sound(
                    'assets/sounds/Daniel_Tidwell_-_At_Dooms_Gate_DOOM_E1M1_(musmore.com).mp3')
        # self.bg_music = self.normal_mode_music
        # self.bg_music.set_volume(self.music_volume)
        self.bg_music = self.change_music(self.normal_mode_music)
        self.click = pygame.mixer.Sound('assets/sounds/click.mp3')
        self.click.set_volume(0.1)
        self.bg_music.play()

        # -------------------------------------------init menu----------------------------------------
        self.start_button = pygame.transform.scale(
            pygame.image.load('assets/menu/button_StartGame.png').convert_alpha(),
            [256, 83])
        self.start_button_rect = self.start_button.get_rect(topleft=(232, 50))
        self.settings_button = pygame.transform.scale(
            pygame.image.load('assets/menu/button_Settings.png').convert_alpha(),
            [204, 57])
        self.settings_button_rect = self.settings_button.get_rect(topleft=(258, 260))
        self.exit_button = pygame.transform.scale(pygame.image.load('assets/menu/button_Exit.png').convert_alpha(),
                                                  [204, 57])
        self.exit_button_rect = self.exit_button.get_rect(topleft=(258, 360))

        # -------------------------------------------init settings----------------------------------------
        self.easymode_button = pygame.transform.scale(
            pygame.image.load('assets/menu/button_Easymode.png').convert_alpha(),
            [204, 57])
        self.easymode_button_rect = self.easymode_button.get_rect(topleft=(258, 40))

        self.normalmode_button = pygame.transform.scale(
            pygame.image.load('assets/menu/button_Normalmode.png').convert_alpha(),
            [204, 57])
        self.normalmode_button_rect = self.normalmode_button.get_rect(topleft=(258, 120))

        self.hardmode_button = pygame.transform.scale(
            pygame.image.load('assets/menu/button_Hardmode.png').convert_alpha(),
            [204, 57])
        self.hardmode_button_rect = self.hardmode_button.get_rect(topleft=(258, 200))

        self.mute_button = pygame.transform.scale(
            pygame.image.load('assets/menu/button_on-off_music.png').convert_alpha(),
            [204, 57])
        self.mute_button_rect = self.mute_button.get_rect(topleft=(16, 360))

        self.back_button = pygame.transform.scale(pygame.image.load('assets/menu/button_Back.png').convert_alpha(),
                                                  [204, 57])
        self.back_button_rect = self.back_button.get_rect(topleft=(500, 360))

        pygame.font.init()
        self.menu_font = pygame.font.Font('assets/fonts/arial.ttf', 30)

    def play_music(self, game):
        if not self.is_muted:
            self.bg_music.stop()
            if game.game_mode == -1:
                self.bg_music = self.change_music(self.easy_mode_music)
            elif game.game_mode == 0:
                self.bg_music = self.change_music(self.normal_mode_music)
            elif game.game_mode == 1:
                self.bg_music = self.change_music(self.hard_mode_music)
        self.bg_music.play()

    def change_music(self, new_music):
        music = new_music
        music.set_volume(self.music_volume)
        return music

    def draw_menu(self, game):
        self.menuscreen.blit(self.bg, (0, 0))
        self.menuscreen.blit(self.start_button, self.start_button_rect)
        self.menuscreen.blit(self.settings_button, self.settings_button_rect)
        self.menuscreen.blit(self.exit_button, self.exit_button_rect)
        if game.max_score > 0:
            max_score_text = self.menu_font.render(f"Your best score: {game.max_score}", True, "White")
            self.menuscreen.blit(max_score_text, (230, 180))

    def draw_settings(self):
        self.menuscreen.blit(self.bg, (0, 0))
        self.menuscreen.blit(self.easymode_button, self.easymode_button_rect)
        self.menuscreen.blit(self.normalmode_button, self.normalmode_button_rect)
        self.menuscreen.blit(self.hardmode_button, self.hardmode_button_rect)
        self.menuscreen.blit(self.mute_button, self.mute_button_rect)
        self.menuscreen.blit(self.back_button, self.back_button_rect)

    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def settings(self, game):
        pygame.mouse.set_visible(1)
        self.draw_settings()
        settings_running = True
        while settings_running:
            mouse = pygame.mouse.get_pos()
            if self.easymode_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.click.play()
                game.game_mode = -1

            elif self.normalmode_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.click.play()
                game.game_mode = 0

            elif self.hardmode_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.click.play()
                game.game_mode = 1

            elif self.mute_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.click.play()
                if self.is_muted:
                    self.is_muted = False
                else:
                    self.bg_music.stop()
                    self.is_muted = True

            elif self.back_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.click.play()
                self.menu(game)
                settings_running = False

            self.check_events()
            pygame.display.update()

    def menu(self, game):
        pygame.mouse.set_visible(1)
        self.draw_menu(game)
        menu_running = True
        while menu_running:
            mouse = pygame.mouse.get_pos()
            if self.start_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.click.play()
                self.play_music(game)
                pygame.mouse.set_visible(0)
                menu_running = False
                game.run(self)

            elif self.settings_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.click.play()
                menu_running = False
                self.settings(game)

            elif self.exit_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.click.play()
                pygame.quit()
                sys.exit()

            self.check_events()
            pygame.display.update()
