class GameStats:
    """跟踪游戏的统计信息。"""

    def __init__(self, ai_game):
        """初始化统计信息。"""
        self.settings = ai_game.settings
        self.ship_limit = [4, 3, 2]
        self.reset_stats()
        # 游戏刚启动时处于非活动状态。
        self.game_active = False
        self.settings_active = False
        self.main_active = True
        # 任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息。"""
        self.ships_left = self.ship_limit[self.settings.difficulty % 3]
        self.score = 0
        self.level = 1
