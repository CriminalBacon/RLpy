class Tile:
    """
    A tile on a map.  It may or may not be blocked, and may or may not block sight
    By keeping blocked_sight and blocked separate, we can have a tile that can been seen-through,
    but not crossed (lava pit), or vice versa (dark room)
    """

    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # By default, if a tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight

        self.explored = False

