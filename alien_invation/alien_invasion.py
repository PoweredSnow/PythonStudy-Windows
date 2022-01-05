import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # 全屏模式
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # 创建一个用于存储游戏统计信息的实例。
        # 并创建记分牌。
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        # self 指向的是当前 AlienInvasion 实例。
        # 这个参数让 Ship 能够访问游戏资源，如对象 screen。
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # 创建按钮。
        self.play_button = Button(self, "Play", 540, 260)
        self.settings_button = Button(self, "Settings", 540, 410)
        self.return_button = Button(self, "Return", 540, 410)
        self.difficulty_buttons = [
            Button(self, "Easy", 540, 260),
            Button(self, "Medium", 540, 260),
            Button(self, "Hard", 540, 260)]
        self.difficulty_button = self.difficulty_buttons[0]

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件。"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_click_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _start_game(self):
        """重置游戏统计信息。"""
        if not self.stats.game_active:
            # 重置游戏设置。
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.stats.game_active = True
            # 清空余下的外星人和子弹。
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人，并将飞船放到屏幕底端的中央。
            self._create_fleet()
            self.ship.center_ship()
            # 隐藏鼠标光标。
            pygame.mouse.set_visible(False)

    def _settings_screen(self):
        """游戏设置页面。"""
        self.stats.settings_active = True
        self.stats.main_active = False
        self._screen_fill()
        self.difficulty_button.draw_button()
        self.return_button.draw_button()

    def _main_screen(self):
        """游戏主页面"""
        self.stats.main_active = True
        self.stats.settings_active = False
        self._screen_fill()
        self.play_button.draw_button()
        self.settings_button.draw_button()

    def _difficulty_update(self):
        """难度更新"""
        self.settings.difficulty += 1
        self.difficulty_button = self.difficulty_buttons[self.settings.difficulty % 3]
        self.settings.difficulty_update()

    def _check_click_button(self, mouse_pos):
        """在玩家单击按钮时作出响应。"""
        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        settings_button_clicked = self.settings_button.rect.collidepoint(
            mouse_pos)
        difficulty_button_clicked = self.difficulty_button.rect.collidepoint(
            mouse_pos)
        return_button_clicked = self.return_button.rect.collidepoint(mouse_pos)
        if play_button_clicked and not self.stats.settings_active:
            self._start_game()
        elif settings_button_clicked and not self.stats.settings_active:
            self._settings_screen()
        elif difficulty_button_clicked:
            self._difficulty_update()
        elif return_button_clicked:
            self._main_screen()

    def _check_keydown_events(self, event):
        """响应按键。"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        """按键松开。"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组 bullets 中。"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹。"""
        # 更新子弹的位置
        self.bullets.update()
        # 删除消失的子弹
        # 使用 for 循环遍历列表时，列表长度必须在整个循环中保持不变。
        # 所以必须遍历编组的副本
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人碰撞。"""
        # 删除发生碰撞的子弹和外星人。
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            # 删除现有的子弹并新建一群外星人，并创建一群新的外星人。
            self.bullets.empty()
            self._create_fleet()
            self.settings.increse_speed()
            # 提高等级。
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """
        检查是否有外星人位于屏幕边缘。
        更新外星人群中所有外星人的位置。
        """
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞船之间的碰撞。
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检查是否有外星人到达了屏幕底端。
        self._check_aliens_bottom()

    def _create_fleet(self):
        """创建外星人群。"""
        # 创建一个外星人并计算一行可容纳多少个外星人。
        # 外星人的间距为外星人宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # 计算屏幕可容纳多少行外星人。
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # 创建外星人群。
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行。"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施。"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端。"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理。
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向。"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """响应飞船被外星人撞到。"""
        if self.stats.ships_left > 0:
            # 将 ship_left 减 1 并更新记分牌。
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # 清空余下的外星人和子弹。
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人，并将飞船放到屏幕底端的中央。
            self._create_fleet()
            self.ship.center_ship()
            # 暂停。
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _screen_fill(self):
        """将屏幕填充为背景色。"""
        self.screen.fill(self.settings.bg_color)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕。"""
        self._screen_fill()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # 显示得分。
        self.sb.show_score()
        # 如果游戏处于非活动状态，就绘制 主屏幕。
        if not self.stats.game_active:
            if self.stats.main_active:
                self._main_screen()
            if self.stats.settings_active:
                self._settings_screen()
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()
