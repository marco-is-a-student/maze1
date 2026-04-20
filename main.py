def on_overlap_tile(sprite, location):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles0,
    on_overlap_tile)

mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . 3 . . . 3 3 3 3 3 . . . .
        . . 3 3 . . . . . . . 3 . . . .
        . . 3 . . . . . . . . 3 . . . .
        . 3 . 3 3 . . . . . . 3 . . . .
        . 3 3 3 3 3 . . . . . 3 . . . .
        . 3 . . . 3 . . . . . 3 . . . .
        . 3 . . 3 . . . . . . 3 . . . .
        . . 3 3 . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.player)
controller.move_sprite(mySprite)
tiles.set_current_tilemap(tilemap("""
    level1
    """))
tiles.place_on_random_tile(mySprite, assets.tile("""
    myTile
    """))
scene.camera_follow_sprite(mySprite)