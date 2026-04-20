scene.onOverlapTile(SpriteKind.Player, assets.tile`transparency16`, function (sprite, location) {
    game.gameOver(true)
})
let mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
tiles.setCurrentTilemap(tilemap`level1`)
tiles.placeOnRandomTile(mySprite, assets.tile`myTile`)
scene.cameraFollowSprite(mySprite)
