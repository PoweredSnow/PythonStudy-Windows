class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        # 难度设置
        self.difficulty_list = [
            self.difficulty_easy(), self.difficulty_normal(),
            self.difficulty_hard()]
        self.difficulty = 0
        self.difficulty_option = self.difficulty_list[0]
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.alien_speeds = [0.1, 0.3, 0.5]
        self.alien_points = [50, 100, 150]
        self.score_scales = [1.5, 2.0, 2.5]
        self.initialize_dynamic_settings()

    def difficulty_update(self):
        """难度更新"""
        self.difficulty_option = self.difficulty_list[self.difficulty % 3]

    def difficulty_easy(self):
        # 飞船设置
        self.ship_limit = 4
        # 外星人设置
        self.fleet_drop_speed = 10
        # 加快游戏节奏的速度。
        self.speedup_scale = 1.1

    def difficulty_normal(self):
        self.ship_limit = 3
        self.fleet_drop_speed = 15
        self.speedup_scale = 1.3

    def difficulty_hard(self):
        self.ship_limit = 2
        self.fleet_drop_speed = 20
        self.speedup_scale = 1.5

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置。"""
        difficulty = self.difficulty % 3
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = self.alien_speeds[difficulty]
        # fleet_direction 为 1 表示向右移，为 -1 表示向左移。
        self.fleet_direction = 1
        # 记分
        self.alien_points = [50, 100, 150]
        self.alien_point = self.alien_points[difficulty]

    def increse_speed(self):
        """提高速度设置"""
        difficulty = self.difficulty % 3
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points[difficulty] = int(
            self.alien_points[difficulty] * self.score_scales[difficulty])
        self.alien_point = self.alien_points[difficulty]
