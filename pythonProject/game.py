# Katarina Selewski hnp8pf and Hannah Duong faw4bh

# Our game is called Mothman. The player plays as a journalist and searches for mothman. The map is layed out in a
# grid-like system of tiles, whcih you will see when you play/look at the code. There are different endings as well as
# a "lose" option if you fail. NOTE: The game does not restart after you fail or get an ending. You will need to exit and
# rerun it to play again. Also, read the Google Docs attached to Gradescope for information about how to get each
# ending and for a little more information on ending 3.

# Our three mandatory aspects are implemented as follows:
# 1) The user controls the character with WASD and can press space to use a camera. THe user can also take certain actions when prompted.
# 2) If the timer hits zero, the game will end and the player will lose (because the story follows a journalist that
# is about to be fired, so they must find mothman before the next day).
# 3) Many graphics and images are used throughout, from different trees to a rock to a shed.

# Our four extra aspects are implemented as follows:
# 1) Sprite animation. The character has 24 total images, for WASD movement and holding the camera.
# 2) Timer. As mentioned, there is a timer that continuously counts to 100. If 100 is reached, the player will lose.
# 3) Collectibles. The key is a collectible that you must collect to progress in endings 1 and 2.
# 4) Different levels/endings. This was approved by a TA during checkpoint 1. Rather than different levels, there are
# different endings you can achieve based on actions taken during the game.

import uvage

#SPRITE IMPLEMENTATION
camera = uvage.Camera(800, 600)
sprite_images = uvage.load_sprite_sheet("movement_cam.png", 1, 24)
sprite = uvage.from_image(400, 320, sprite_images[0])
sprite.scale_by(0.5)
current_frame = 0
sprite_move = False

mothman_images = uvage.load_sprite_sheet("mothman_movement.png", 1, 20)
mothman = uvage.from_image(200, 400, mothman_images[6])
mothman.scale_by(0.5)

#ENVIRONMENT IMAGES
#TREES
trees = uvage.load_sprite_sheet("trees!.png", 1, 10)
tree1 = uvage.from_image(150, 200, trees[0])
tree1.scale_by(0.5)
tree2 = uvage.from_image(650, 125, trees[1])
tree2.scale_by(0.5)
tree3 = uvage.from_image(275, 100, trees[2])
tree3.scale_by(0.5)
tree4 = uvage.from_image(300, 300, trees[5])
tree4.scale_by(0.5)
tree5 = uvage.from_image(300, 300, trees[6])
tree5.scale_by(0.5)

#ROCK
rock = uvage.from_image(300, 350, "rock.png")

#KEY
key = uvage.from_image(550, 300, "key.png")

#STAIRS
stairs = uvage.from_image(400, 350, "stairs.png")
stairs.scale_by(0.8)

#DRAWING EACH TILE. THERE SHOULD BE 16 + SHED
shed = uvage.from_image(400, 150, "shed.png")
shed.scale_by(0.3)
#TILE 1
road = uvage.from_color(0, 450, "dark grey", 1600, 150)
lines = uvage.from_color(0, 450, "white", 1600, 10)
roadspace1 = uvage.from_color(100, 450, "dark grey", 70, 10)
roadspace2 = uvage.from_color(300, 450, "dark grey", 70, 10)
roadspace3 = uvage.from_color(500, 450, "dark grey", 70, 10)
roadspace4 = uvage.from_color(700, 450, "dark grey", 70, 10)
roadspace5 = uvage.from_color(900, 450, "dark grey", 70, 10)
roadspace6 = uvage.from_color(1100, 450, "dark grey", 70, 10)


#USED TO DETERMINE IF KEY HAS BEEN COLLECTED YET
key_aquired = False

#FUNCTIONS FOR DRAWING TILES HERE. THERE SHOULD BE 16 TOTAL
def draw_tile_1():
    """
    This function is designed to draw Tile 1. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    camera.draw(road)
    camera.draw(lines)
    camera.draw(roadspace1)
    camera.draw(roadspace2)
    camera.draw(roadspace3)
    camera.draw(roadspace4)
    if sprite.y <= 125:
        camera.draw(sprite)
        camera.draw(tree3)
        camera.draw(tree2)
        camera.draw(tree1)
    if 125 < sprite.y <= 145:
        camera.draw(tree3)
        camera.draw(sprite)
        camera.draw(tree2)
        camera.draw(tree1)
    if 145 < sprite.y < 225:
        camera.draw(tree2)
        camera.draw(tree3)
        camera.draw(sprite)
        camera.draw(tree1)
    if 225 <= sprite.y <= 650:
        camera.draw(tree1)
        camera.draw(tree2)
        camera.draw(tree3)
        camera.draw(sprite)

def draw_tile_2():
    """
    This function is designed to draw Tile 2. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    camera.draw(road)
    camera.draw(lines)
    camera.draw(roadspace1)
    camera.draw(roadspace2)
    camera.draw(roadspace3)
    camera.draw(roadspace4)
    camera.draw(roadspace5)
    tree3_1 = tree3.copy_at(650, 100)
    tree1_1 = tree1.copy_at (300, 200)
    tree1_2 = tree1.copy_at(125, 150)
    camera.draw(tree3_1)
    camera.draw(tree1_1)
    camera.draw(tree1_2)
    camera.draw(sprite)
    if sprite.y <= 125:
        camera.draw(sprite)
        camera.draw(tree1_2)
        camera.draw(tree1_1)
        camera.draw(tree3_1)
    if 125 < sprite.y <= 175:
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree1_2)
        camera.draw(tree1_1)
    if 175 < sprite.y <= 225:
        camera.draw(tree1_2)
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree1_1)
    if 225 < sprite.y <= 650:
        camera.draw(tree1_1)
        camera.draw(tree1_2)
        camera.draw(tree3_1)
        camera.draw(sprite)

def draw_tile_3():
    """
    This function is designed to draw Tile 3. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    camera.draw(road)
    camera.draw(lines)
    camera.draw(roadspace1)
    camera.draw(roadspace2)
    camera.draw(roadspace3)
    camera.draw(roadspace4)
    camera.draw(roadspace5)
    tree1_1 = tree1.copy_at(150, 150)
    tree3_1 = tree3.copy_at(550, 120)
    tree1_2 = tree1.copy_at(700, 210)
    if sprite.y <= 145:
        camera.draw(sprite)
        camera.draw(tree3_1)
        camera.draw(tree1_2)
        camera.draw(tree1_1)
    if 145 < sprite.y <= 170:
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree1_2)
        camera.draw(tree1_1)
    if 170 < sprite.y <= 235:
        camera.draw(tree1_1)
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree1_2)
    if 235 < sprite.y <= 650:
        camera.draw(tree1_1)
        camera.draw(tree1_2)
        camera.draw(tree3_1)
        camera.draw(sprite)

def draw_tile_4():
    """
    This function is designed to draw Tile 4. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    tree1_1 = tree1.copy_at(125, 125)
    tree5_1 = tree5.copy_at(650, 425)
    tree4_1 = tree4.copy_at(100, 300)
    tree1_2 = tree1.copy_at(210, 425)
    tree2_1 = tree2.copy_at(700, 200)
    rock1 = rock.copy_at(450, 350)
    if sprite.y <= 150:
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(rock1)
        camera.draw(tree5_1)
        camera.draw(tree1_2)
    if 150 < sprite.y <= 225:
        camera.draw(tree1_1)
        camera.draw(sprite)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(rock1)
        camera.draw(tree5_1)
        camera.draw(tree1_2)
    if 225 < sprite.y <= 250:
        camera.draw(tree1_1)
        camera.draw(tree2_1)
        camera.draw(sprite)
        camera.draw(tree4_1)
        camera.draw(rock1)
        camera.draw(tree5_1)
        camera.draw(tree1_2)
    if 250 < sprite.y <= 335:
        camera.draw(tree1_1)
        camera.draw(tree2_1)
        camera.draw(rock1)
        camera.draw(sprite)
        camera.draw(tree4_1)
        camera.draw(tree5_1)
        camera.draw(tree1_2)
    if 335 < sprite.y <= 360:
        camera.draw(tree1_1)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(rock1)
        camera.draw(sprite)
        camera.draw(tree5_1)
        camera.draw(tree1_2)
    if 360 < sprite.y <= 445:
        camera.draw(tree1_1)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(rock1)
        camera.draw(sprite)
        camera.draw(tree5_1)
        camera.draw(tree1_2)
    if 445 < sprite.y <= 450:
        camera.draw(tree1_1)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(rock1)
        camera.draw(tree5_1)
        camera.draw(sprite)
        camera.draw(tree1_2)
    if 450 < sprite.y <= 650:
        camera.draw(tree1_1)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(rock1)
        camera.draw(tree5_1)
        camera.draw(tree1_2)
        camera.draw(sprite)

def draw_tile_5():
    """
    This function is designed to draw Tile 5. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    tree1_1 = tree1.copy_at(150, 150)
    tree2_1 = tree2.copy_at(690, 300)
    tree1_2 = tree1.copy_at(275, 450)
    tree3_1 = tree3.copy_at(500, 100)
    if sprite.y <= 125:
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(tree3_1)
        camera.draw(tree2_1)
        camera.draw(tree1_2)
    if 125 < sprite.y <= 175:
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(tree2_1)
        camera.draw(tree1_2)
    if 175 < sprite.y <= 325:
        camera.draw(tree1_1)
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree2_1)
        camera.draw(tree1_2)
    if 325 < sprite.y <= 475:
        camera.draw(tree1_1)
        camera.draw(tree3_1)
        camera.draw(tree2_1)
        camera.draw(sprite)
        camera.draw(tree1_2)
    if 475 < sprite.y <= 650:
        camera.draw(tree1_1)
        camera.draw(tree3_1)
        camera.draw(tree2_1)
        camera.draw(tree1_2)
        camera.draw(sprite)

def draw_tile_6():
    """
    This function is designed to draw Tile 6. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    tree4_1 = tree4.copy_at(600, 125)
    tree1_1 = tree1.copy_at(200, 450)
    tree1_2 = tree1.copy_at(700, 350)
    rock1 = rock.copy_at(225, 245)
    if sprite.y <= 145:
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(rock1)
        camera.draw(tree4_1)
        camera.draw(tree1_2)
    if 145 < sprite.y <= 150:
        camera.draw(rock1)
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(tree4_1)
        camera.draw(tree1_2)
    if 150 < sprite.y <= 375:
        camera.draw(rock1)
        camera.draw(tree4_1)
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(tree1_2)
    if 375 < sprite.y <= 475:
        camera.draw(rock1)
        camera.draw(tree4_1)
        camera.draw(tree1_2)
        camera.draw(sprite)
        camera.draw(tree1_1)
    if 475 < sprite.y <= 650:
        camera.draw(tree1_1)
        camera.draw(rock1)
        camera.draw(tree4_1)
        camera.draw(tree1_2)
        camera.draw(sprite)

def draw_tile_8():
    """
    This function is designed to draw Tile 8. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    camera.draw(road)
    camera.draw(lines)
    camera.draw(roadspace1)
    camera.draw(roadspace2)
    camera.draw(roadspace3)
    camera.draw(roadspace4)
    camera.draw(roadspace5)
    tree3_1 = tree3.copy_at(100, 220)
    tree2_1 = tree2.copy_at(450, 125)
    tree2_2 = tree2.copy_at(730, 225)
    if sprite.y <= 150:
        camera.draw(sprite)
        camera.draw(tree3_1)
        camera.draw(tree2_2)
        camera.draw(tree2_1)
    if 150 < sprite.y <= 245:
        camera.draw(tree2_1)
        camera.draw(sprite)
        camera.draw(tree2_2)
        camera.draw(tree3_1)
    if 245 < sprite.y <= 250:
        camera.draw(tree2_1)
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree2_2)
    if 250 < sprite.y <= 650:
        camera.draw(tree2_1)
        camera.draw(tree2_2)
        camera.draw(tree3_1)
        camera.draw(sprite)

def draw_tile_10():
    """
    This function is designed to draw Tile 10. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    tree4_1 = tree4.copy_at(350, 100)
    tree2_1 = tree2.copy_at(700, 250)
    tree5_1 = tree5.copy_at(200, 350)
    rock1 = rock.copy_at(600, 475)
    note = uvage.from_color(270, 370, "white", 30, 40)
    if sprite.y <= 125:
        camera.draw(note)
        camera.draw(sprite)
        camera.draw(tree4_1)
        camera.draw(tree5_1)
        camera.draw(tree2_1)
        camera.draw(rock1)
    if 125 < sprite.y <= 275:
        camera.draw(note)
        camera.draw(tree4_1)
        camera.draw(sprite)
        camera.draw(tree5_1)
        camera.draw(tree2_1)
        camera.draw(rock1)
    if 275 < sprite.y <= 375:
        camera.draw(note)
        camera.draw(tree4_1)
        camera.draw(tree2_1)
        camera.draw(sprite)
        camera.draw(tree5_1)
        camera.draw(rock1)
    if 375 < sprite.y <= 390:
        camera.draw(note)
        camera.draw(rock1)
        camera.draw(tree4_1)
        camera.draw(tree2_1)
        camera.draw(sprite)
        camera.draw(tree5_1)
    if 390 < sprite.y <= 650:
        camera.draw(note)
        camera.draw(tree4_1)
        camera.draw(tree5_1)
        camera.draw(tree2_1)
        camera.draw(rock1)
        camera.draw(sprite)

def draw_tile_12():
    """
    This function is designed to draw Tile 12. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    tree2_1 = tree2.copy_at(275, 325)
    tree2_2 = tree2.copy_at(125, 140)
    tree2_3 = tree2.copy_at(730, 125)
    tree4_1 = tree4.copy_at(610, 205)
    tree3_1 = tree3.copy_at(570, 440)
    rock1 = rock.copy_at(275, 200)
    if sprite.y <= 100:
        camera.draw(sprite)
        camera.draw(tree2_1)
        camera.draw(tree2_2)
        camera.draw(tree2_3)
        camera.draw(tree4_1)
        camera.draw(tree3_1)
        camera.draw(rock1)
    if 100 < sprite.y <= 145:
        camera.draw(rock1)
        camera.draw(sprite)
        camera.draw(tree2_1)
        camera.draw(tree2_2)
        camera.draw(tree2_3)
        camera.draw(tree4_1)
        camera.draw(tree3_1)
    if 145 < sprite.y <= 165:
        camera.draw(rock1)
        camera.draw(tree2_3)
        camera.draw(sprite)
        camera.draw(tree2_1)
        camera.draw(tree2_2)
        camera.draw(tree4_1)
        camera.draw(tree3_1)
    if 165 < sprite.y <= 225:
        camera.draw(rock1)
        camera.draw(tree2_3)
        camera.draw(tree2_2)
        camera.draw(sprite)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(tree3_1)
    if 225 < sprite.y <= 345:
        camera.draw(rock1)
        camera.draw(tree2_3)
        camera.draw(tree2_2)
        camera.draw(tree4_1)
        camera.draw(sprite)
        camera.draw(tree2_1)
        camera.draw(tree3_1)
    if 345 < sprite.y <= 460:
        camera.draw(rock1)
        camera.draw(tree2_3)
        camera.draw(tree2_2)
        camera.draw(tree4_1)
        camera.draw(tree2_1)
        camera.draw(sprite)
        camera.draw(tree3_1)
    if 460 < sprite.y <= 650:
        camera.draw(rock1)
        camera.draw(tree2_3)
        camera.draw(tree2_2)
        camera.draw(tree4_1)
        camera.draw(tree2_1)
        camera.draw(tree3_1)
        camera.draw(sprite)

def draw_tile_13():
    """
    This function is designed to draw Tile 13. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    tree5_1 = tree5.copy_at(400, 250)
    tree3_1 = tree3.copy_at(690, 140)
    tree3_2 = tree3.copy_at(200, 110)
    tree1_1 = tree1.copy_at(600, 450)
    rock1 = rock.copy_at(200, 475)
    if sprite.y <= 135:
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(rock1)
        camera.draw(tree5_1)
        camera.draw(tree3_2)
        camera.draw(tree3_1)
    if 135 < sprite.y <= 165:
        camera.draw(tree3_2)
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(rock1)
        camera.draw(tree5_1)
        camera.draw(tree3_1)
    if 165 < sprite.y <= 280:
        camera.draw(tree3_2)
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(rock1)
        camera.draw(tree5_1)
    if 280 < sprite.y <= 375:
        camera.draw(tree5_1)
        camera.draw(tree3_2)
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(rock1)
    if 375 < sprite.y <= 475:
        camera.draw(rock1)
        camera.draw(tree3_2)
        camera.draw(tree3_1)
        camera.draw(tree5_1)
        camera.draw(sprite)
        camera.draw(tree1_1)
    if 475 < sprite.y <= 650:
        camera.draw(tree3_2)
        camera.draw(tree3_1)
        camera.draw(rock1)
        camera.draw(tree5_1)
        camera.draw(tree1_1)
        camera.draw(sprite)

def draw_tile_14():
    """
    This function is designed to draw Tile 14. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    tree2_1 = tree2.copy_at(675, 225)
    tree4_1 = tree4.copy_at(125, 425)
    tree3_1 = tree3.copy_at(200, 100)
    tree3_2 = tree3.copy_at(450, 340)
    if sprite.y <= 125:
        camera.draw(sprite)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(tree3_2)
        camera.draw(tree3_1)
    if 125 < sprite.y <= 250:
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(tree3_2)
    if 250 < sprite.y <= 365:
        camera.draw(tree2_1)
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree4_1)
        camera.draw(tree3_2)
    if 365 < sprite.y <= 450:
        camera.draw(tree3_2)
        camera.draw(tree3_1)
        camera.draw(tree2_1)
        camera.draw(sprite)
        camera.draw(tree4_1)
    if 450 < sprite.y <= 650:
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(tree3_2)
        camera.draw(tree3_1)
        camera.draw(sprite)

def draw_tile_15():
    """This function is designed to draw Tile 15. It allows for the illusion of 3D based on drawing order."""
    camera.clear("black")
    tree4_1 = tree4.copy_at(190, 190)
    tree4_3 = tree4.copy_at(500, 130)
    tree4_4 = tree4.copy_at(670, 195)
    tree4_6 = tree4.copy_at(530, 450)
    tree4_7 = tree4.copy_at(360, 420)
    tree5_1 = tree5.copy_at(100, 275)
    if sprite.y <= 155:
        camera.draw(sprite)
        camera.draw(tree4_1)
        camera.draw(tree4_3)
        camera.draw(tree4_4)
        camera.draw(tree4_6)
        camera.draw(tree4_7)
        camera.draw(tree5_1)
    if 155 < sprite.y <= 215:
        camera.draw(tree4_3)
        camera.draw(sprite)
        camera.draw(tree4_1)
        camera.draw(tree4_4)
        camera.draw(tree4_6)
        camera.draw(tree4_7)
        camera.draw(tree5_1)
    if 215 < sprite.y <= 220:
        camera.draw(tree4_1)
        camera.draw(tree4_3)
        camera.draw(sprite)
        camera.draw(tree4_4)
        camera.draw(tree4_6)
        camera.draw(tree4_7)
        camera.draw(tree5_1)
    if 220 < sprite.y <= 310:
        camera.draw(tree4_1)
        camera.draw(tree4_3)
        camera.draw(tree4_4)
        camera.draw(sprite)
        camera.draw(tree4_6)
        camera.draw(tree4_7)
        camera.draw(tree5_1)
    if 310 < sprite.y <= 445:
        camera.draw(tree4_1)
        camera.draw(tree4_3)
        camera.draw(tree4_4)
        camera.draw(tree5_1)
        camera.draw(sprite)
        camera.draw(tree4_6)
        camera.draw(tree4_7)
    if 425 < sprite.y <= 475:
        camera.draw(tree4_1)
        camera.draw(tree4_3)
        camera.draw(tree4_4)
        camera.draw(tree4_7)
        camera.draw(tree5_1)
        camera.draw(sprite)
        camera.draw(tree4_6)
    if 475 < sprite.y <= 650:
        camera.draw(tree4_1)
        camera.draw(tree4_3)
        camera.draw(tree4_4)
        camera.draw(tree4_6)
        camera.draw(tree4_7)
        camera.draw(tree5_1)
        camera.draw(sprite)

def draw_tile_17():
    """
    This function is designed to draw Tile 17. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    tree1_1 = tree1.copy_at(100, 150)
    tree1_2 = tree1.copy_at(200, 300)
    tree1_3 = tree1.copy_at(100, 450)
    tree1_4 = tree1.copy_at(725, 150)
    tree1_5 = tree1.copy_at(625, 300)
    tree1_6 = tree1.copy_at(725, 450)
    if 300 < sprite.x < 500 and sprite.y <= 180:
        sprite.y = 180
    if sprite.y <= 170:
        camera.draw(sprite)
        camera.draw(shed)
        camera.draw(tree1_1)
        camera.draw(tree1_2)
        camera.draw(tree1_3)
        camera.draw(tree1_4)
        camera.draw(tree1_5)
        camera.draw(tree1_6)
    if 170 < sprite.y <= 330:
        camera.draw(tree1_1)
        camera.draw(tree1_4)
        camera.draw(shed)
        camera.draw(sprite)
        camera.draw(tree1_3)
        camera.draw(tree1_2)
        camera.draw(tree1_5)
        camera.draw(tree1_6)
    if 330 < sprite.y <= 475:
        camera.draw(tree1_1)
        camera.draw(tree1_4)
        camera.draw(tree1_2)
        camera.draw(tree1_5)
        camera.draw(shed)
        camera.draw(sprite)
        camera.draw(tree1_3)
        camera.draw(tree1_6)
    if 475 < sprite.y <= 650:
        camera.draw(tree1_1)
        camera.draw(tree1_4)
        camera.draw(tree1_2)
        camera.draw(tree1_5)
        camera.draw(shed)
        camera.draw(tree1_3)
        camera.draw(tree1_6)
        camera.draw(sprite)

def draw_tile_18():
    """
    This function is designed to draw Tile 18. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    camera.draw(key)
    tree1_1 = tree1.copy_at(125, 400)
    tree2_1 = tree2.copy_at(300, 125)
    tree3_1 = tree3.copy_at(700, 100)
    tree4_1 = tree4.copy_at(550, 450)
    rock1 = rock.copy_at(145, 300)
    rock2 = rock.copy_at(390, 390)
    if sprite.y <= 125:
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(rock1)
        camera.draw(tree3_1)
        camera.draw(rock2)
    if 125 < sprite.y <= 150:
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(rock1)
        camera.draw(rock2)
        camera.draw(tree1_1)
    if 150 < sprite.y <= 200:
        camera.draw(tree3_1)
        camera.draw(tree2_1)
        camera.draw(sprite)
        camera.draw(tree4_1)
        camera.draw(rock1)
        camera.draw(rock2)
        camera.draw(tree1_1)
    if 200 < sprite.y <= 290:
        camera.draw(tree3_1)
        camera.draw(tree2_1)
        camera.draw(rock1)
        camera.draw(sprite)
        camera.draw(tree4_1)
        camera.draw(rock2)
        camera.draw(tree1_1)
    if 290 < sprite.y <= 425:
        camera.draw(tree3_1)
        camera.draw(tree2_1)
        camera.draw(rock2)
        camera.draw(rock1)
        camera.draw(sprite)
        camera.draw(tree4_1)
        camera.draw(tree1_1)
    if 425 < sprite.y <= 475:
        camera.draw(tree3_1)
        camera.draw(tree2_1)
        camera.draw(rock2)
        camera.draw(rock1)
        camera.draw(tree1_1)
        camera.draw(sprite)
        camera.draw(tree4_1)
    if 475 < sprite.y <= 650:
        camera.draw(tree1_1)
        camera.draw(tree2_1)
        camera.draw(tree4_1)
        camera.draw(rock1)
        camera.draw(tree3_1)
        camera.draw(rock2)
        camera.draw(sprite)

def draw_tile_19():
    """
    This function is designed to draw Tile 19. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    tree5_1 = tree5.copy_at(700, 150)
    tree1_1 = tree1.copy_at(125, 460)
    tree3_1 = tree3.copy_at(110, 200)
    tree1_2 = tree1.copy_at(415, 135)
    if  sprite.y <= 160:
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(tree1_2)
        camera.draw(tree5_1)
        camera.draw(tree3_1)
    if 160 < sprite.y <= 185:
        camera.draw(tree1_2)
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(tree5_1)
        camera.draw(tree3_1)
    if 185 < sprite.y <= 225:
        camera.draw(tree5_1)
        camera.draw(tree1_2)
        camera.draw(sprite)
        camera.draw(tree1_1)
        camera.draw(tree3_1)
    if 225 < sprite.y <= 485:
        camera.draw(tree5_1)
        camera.draw(tree1_2)
        camera.draw(tree3_1)
        camera.draw(sprite)
        camera.draw(tree1_1)
    if 485 < sprite.y <= 650:
        camera.draw(tree1_1)
        camera.draw(tree1_2)
        camera.draw(tree3_1)
        camera.draw(tree5_1)
        camera.draw(sprite)

def draw_tile_20():
    """
    This function is designed to draw Tile 20. It allows for the illusion of 3D based on drawing order.
    :return:
    """
    camera.clear("black")
    tree5_1 = tree5.copy_at(200, 150)
    tree5_2 = tree5.copy_at(600, 150)
    tree5_3 = tree5.copy_at(200, 450)
    tree5_4 = tree5.copy_at(600, 450)
    if 350 < sprite.x < 450 and 310 <= sprite.y <= 320:
        sprite.y = 320
    if 125 < sprite.y <= 185:
        camera.draw(sprite)
        camera.draw(tree5_1)
        camera.draw(tree5_2)
        camera.draw(stairs)
        camera.draw(tree5_3)
        camera.draw(tree5_4)
    if 185 < sprite.y <= 270:
        camera.draw(tree5_1)
        camera.draw(tree5_2)
        camera.draw(sprite)
        camera.draw(stairs)
        camera.draw(tree5_3)
        camera.draw(tree5_4)
    if 270 < sprite.y <= 485:
        camera.draw(tree5_1)
        camera.draw(tree5_2)
        camera.draw(stairs)
        camera.draw(sprite)
        camera.draw(tree5_3)
        camera.draw(tree5_4)
    if 485 < sprite.y <= 650:
        camera.draw(tree5_1)
        camera.draw(tree5_2)
        camera.draw(tree5_3)
        camera.draw(tree5_4)
        camera.draw(stairs)
        camera.draw(sprite)

# MOVEMENT FUNCTION
def move_sprite():
    """
    This function is designed to allow the user to use WASD to move. The player can also hold up a camera due to the
    context of the game.
    :return:
    """
    sprite_move = False
    global current_frame
    if uvage.is_pressing("s") and uvage.is_pressing("d"):
        sprite.x = sprite.x
        sprite.y = sprite.y
    elif uvage.is_pressing("s") and uvage.is_pressing("a"):
        sprite.x = sprite.x
        sprite.y = sprite.y
    elif uvage.is_pressing("w") and uvage.is_pressing("d"):
        sprite.x = sprite.x
        sprite.y = sprite.y
    elif uvage.is_pressing("w") and uvage.is_pressing("a"):
        sprite.x = sprite.x
        sprite.y = sprite.y
    elif uvage.is_pressing("space") and uvage.is_pressing("d"):
        sprite.x = sprite.x
        sprite.y = sprite.y
        sprite.image = sprite_images[20]
    elif uvage.is_pressing("space") and uvage.is_pressing("a"):
        sprite.x = sprite.x
        sprite.y = sprite.y
        sprite.image = sprite_images[21]
    elif uvage.is_pressing("space") and uvage.is_pressing("s"):
        sprite.x = sprite.x
        sprite.y = sprite.y
        sprite.image = sprite_images[22]
    elif uvage.is_pressing("space") and uvage.is_pressing("w"):
        sprite.x = sprite.x
        sprite.y = sprite.y
        sprite.image = sprite_images[23]
    elif uvage.is_pressing("space") and 0 <= current_frame <= 5:
        sprite.image = sprite_images[20]
    elif uvage.is_pressing("space") and 5 < current_frame <= 11:
        sprite.image = sprite_images[21]
    elif uvage.is_pressing("space") and 11 < current_frame <= 15:
        sprite.image = sprite_images[22]
    elif uvage.is_pressing("space") and 15 < current_frame <= 19:
        sprite.image = sprite_images[23]
    else:
        if uvage.is_pressing("s"):
            if current_frame < 12:
                current_frame = 13
            current_frame += 0.2
            if current_frame >= 15:
                current_frame = 12
            sprite.image = sprite_images[int(current_frame)]
            sprite.y +=10
            sprite_move = True
        if uvage.is_pressing("w"):
            if current_frame < 16:
                current_frame = 17
            current_frame += 0.2
            if current_frame >= 19:
                current_frame = 16
            sprite.image = sprite_images[int(current_frame)]
            sprite.y -=10
            sprite_move = True
        if uvage.is_pressing("a"):
            if current_frame < 6:
                current_frame = 7
            current_frame += 0.23
            if current_frame >= 12:
                current_frame = 6
            sprite.image = sprite_images[int(current_frame)]
            sprite.x -=10
            sprite_move = True
        if uvage.is_pressing("d"):
            current_frame += 0.23
            if current_frame >= 6:
                current_frame = 0
            sprite.image = sprite_images[int(current_frame)]
            sprite.x += 10
            sprite_move = True

stair_touch = False

def touching_stairs():
    """
    This function is designed to determine whether the user is in front of the stairs.
    :return:
    """
    global Tile20
    global stair_touch
    if Tile20:
        if 300 < sprite.x < 460 and 350 > sprite.y > 300:
            stair_touch = True
        else:
            stair_touch = False

def stair_text():
    """
    This function is designed to prompt the user to climb the stairs or leave when in front of the stairs.
    :return:
    """
    global stair_touch
    global Purgatory
    global ending_current
    if stair_touch and Purgatory == False:
        text_prompt_box = uvage.from_color(400, 300, "black", 700, 300)
        text_prompt_proceed = uvage.from_text(400, 275, "Press SPACE to climb the stairs", 30, "white", bold=True)
        camera.draw(text_prompt_box)
        camera.draw(text_prompt_proceed)
        if uvage.is_pressing("space"):
            Purgatory = True
            ending_current = True

def draw_note():
    """
    This fnction is designed to display a note that the reader can see from the ground in Tile 10.
    :return:
    """
    global Tile10
    if Tile10:
        if 260 < sprite.x < 290 and 290 < sprite.y < 370:
            camera.clear("black")
            warning = uvage.from_text(400, 200, "BEWARE THE STAIRS", 100, "red")
            msg = uvage.from_text(400, 300, "BEWARE HELL", 100, "red")
            camera.draw(warning)
            camera.draw(msg)

# BOOLEANS FOR TILES. THERE SHOULD BE 16
Tile1 = True
Tile2 = False
Tile3 = False
Tile4 = False
Tile5 = False
Tile6 = False
Tile7 = False
Tile8 = False
Tile9 = False
Tile10 = False
Tile11 = False
Tile12 = False
Tile13 = False
Tile14 = False
Tile15 = False
Tile16 = False
Tile17 = False
Tile18 = False
Tile19 = False
Tile20 = False

#ONE-TIME EVENTS
touched_key = False
touching_mothman = False
choice = False
mothman_copy = mothman.copy_at(255, 300)
#USED FOR AFTER GUN IS AQUIRED. MOTHMAN SPAWNS.
def mothman_final():
    """
    This function is designed to spawn mothman once the player has aquired the gun. It also prompts the function below
    once mothman and the player come into proximity.
    :return:
    """
    global already_opened
    global Tile15
    global touching_mothman
    global choice
    global mothman_copy
    if already_opened:
        if Tile15:
            camera.draw(mothman_copy)
            if sprite.touches(mothman, -300, 70):
                choice = True
shoot = False
pic = False
#USED TO MAKE A CHOICE AT END OF GAME
def ending_choices():
    """
    This function is designed to allow the player to make a choice that determines which ending they gt upon confronting mothman.
    They can either kill him or simply take a picture of him.
    :return:
    """
    global choice
    global shoot
    global pic
    global mothman_copy
    if choice:
        mothman_copy.x = 900
        camera.clear("black")
        option1 = uvage.from_text(400, 225, "Press K to shoot mothman", 50, "red")
        option2 = uvage.from_text(400, 300, "Press M to take picture and leave", 50, "white")
        camera.draw(option1)
        camera.draw(option2)
        if uvage.is_pressing("k"):
            shoot = True
        elif uvage.is_pressing("m"):
            pic = True

ending1_final = False
def bad_ending1():
    """
    This function is designed to show the title of ending 2.
    :return:
    """
    global ending1_final
    global shoot
    if shoot:
        camera.clear("black")
        ending_title = uvage.from_text(400, 250, "REVENGE", 100, "red")
        exit = uvage.from_text(400, 350, "Press SPACE to continue", 50, "white")
        camera.draw(ending_title)
        camera.draw(exit)
        if uvage.is_pressing("space"):
            ending1_final = True

def bad_ending2():
    """
    This function is designed to offer the description of ending 2.
    :return:
    """
    global ending1_final
    if ending1_final:
        camera.clear("black")
        msg = uvage.from_text(400, 200, "BREAKING: Journalist found dead in the woods.", 45, "white")
        msg2 = uvage.from_text(400, 250, "Police say it was an animal attack, though it is unclear which species.", 25, "white")
        ending = uvage.from_text(400, 300, "Ending 2/3", 45, "white")
        camera.draw(msg)
        camera.draw(msg2)
        camera.draw(ending)
ending2_final = False
def good_ending1():
    """
    This function is designed to show the title for ending 1.
    :return:
    """
    global pic
    global ending2_final
    if pic:
        camera.clear("black")
        success = uvage.from_text(400, 250, "Success!", 100, "white")
        camera.draw(success)
        exit = uvage.from_text(400, 350, "Press SPACE to continue", 50, "white")
        camera.draw(exit)
        if uvage.is_pressing("space"):
            ending2_final = True
def good_ending2():
    """
    This function is designed to offer the description for ending 1.
    :return:
    """
    global ending2_final
    if ending2_final:
        camera.clear("black")
        msg = uvage.from_text(400, 200, "BREAKING: New species discovered.", 50, "white")
        msg2 = uvage.from_text(400, 250, "Journalist publishes images of bipedal insect in West Virginia.", 25,"white")
        ending = uvage.from_text(400, 300, "Ending 1/3", 45, "white")
        camera.draw(msg)
        camera.draw(msg2)
        camera.draw(ending)

# FUNCTION FOR DRAWING TILES BASED ON MOVEMENT.
def draw_tiles():
    """
    This function is designed to lay out a grid-like system of "tiles" that are drawn depending on the character's location.
    THe edge tiles are designed such that if you run to the edge of one, you will be transported back to the start of it. This
    allows for continuous movement rather than getting jammed at the edge of a tile.
    :return:
    """
    global tut
    global game_on
    global stair_touch
    global already_entered_5
    global already_entered_2
    global touched_key
    global Tile1
    global Tile2
    global Tile3
    global Tile4
    global Tile5
    global Tile6
    global Tile8
    global Tile10
    global Tile12
    global Tile13
    global Tile14
    global Tile15
    global Tile15
    global Tile17
    global Tile18
    global Tile19
    global Tile20
    if Tile1:
        draw_tile_1()
        if sprite.x < 35:
            sprite.x = 845
            Tile2 = True
            Tile1 = False
        if sprite.x > 850:
            sprite.x = 40
            Tile3 = True
            Tile1 = False
        if sprite.y < 25:
            sprite.y = 600
            Tile1 = False
            Tile5 = True
        if sprite.y > 625:
            sprite.y = 25
    if Tile2:
        draw_tile_2()
        if sprite.x > 850:
            sprite.x = 40
            Tile2 = False
            Tile1 = True
        if sprite.y < 25:
            sprite.y = 600
            Tile2 = False
            Tile4 = True
        if sprite.x < 35:
            sprite.x = 845
        if sprite.y > 625:
            sprite.y = 25
    if Tile3:
        draw_tile_3()
        if sprite.x < 35:
            sprite.x = 845
            Tile3 = False
            Tile1 = True
        if sprite.y > 625:
            sprite.y = 35
        if sprite.x > 850:
            sprite.x = 40
            Tile3 = False
            Tile8 = True
        if sprite.y < 25:
            sprite.y = 600
            Tile3 = False
            Tile6 = True
    if Tile4:
        draw_tile_4()
        if sprite.x > 850:
            sprite.x = 40
            Tile4 = False
            Tile5 = True
        if sprite.y > 625:
            sprite.y = 35
            Tile4 = False
            Tile2 = True
        if sprite.x < 35:
            sprite.x = 845
        if sprite.y < 25:
            sprite.y = 600
            Tile4 = False
            Tile12 = True
    if Tile5:
        draw_tile_5()
        if sprite.x < 35:
            sprite.x = 845
            Tile5 = False
            Tile4 = True
        if sprite.y > 625:
            sprite.y = 35
            Tile5 = False
            Tile1 = True
        if sprite.x > 850:
            sprite.x = 40
            Tile5 = False
            Tile6 = True
        if sprite.y < 25:
            sprite.y = 600
            Tile5 = False
            Tile13 = True
    if Tile6:
        draw_tile_6()
        if sprite.x < 35:
            sprite.x = 845
            Tile6 = False
            Tile5 = True
        if sprite.y > 625:
            sprite.y = 35
            Tile6 = False
            Tile3 = True
        if sprite.y < 25:
            sprite.y = 600
            Tile6 = False
            Tile14 = True
        if sprite.x > 850:
            sprite.x = 40
            Tile6 = False
            Tile10 = True
    if Tile8:
        draw_tile_8()
        if sprite.y > 625:
            sprite.y = 35
        if sprite.x > 850:
            sprite.x = 40
        if sprite.x < 35:
            sprite.x = 845
            Tile8 = False
            Tile3 = True
        if sprite.y < 25:
            sprite.y = 600
            Tile8 = False
            Tile10 = True
    if Tile10:
        draw_tile_10()
        if sprite.y > 625:
            sprite.y = 35
            Tile10 = False
            Tile8 = True
        if sprite.x > 850:
            sprite.x = 40
        if sprite.x < 35:
            sprite.x = 845
            Tile10 = False
            Tile6 = True
        if sprite.y < 25:
            sprite.y = 600
            Tile10 = False
            Tile15 = True
    if Tile12:
        draw_tile_12()
        if sprite.x > 850:
            sprite.x = 40
            Tile12 = False
            Tile13 = True
        if sprite.y > 625:
            sprite.y = 35
            Tile12 = False
            Tile4 = True
        if sprite.x < 35:
            sprite.x = 845
        if sprite.y < 25:
            sprite.y = 600
            Tile12 = False
            Tile17 = True
    if Tile13:
        draw_tile_13()
        if sprite.x < 35:
            sprite.x = 845
            Tile13 = False
            Tile12 = True
        if sprite.y > 625:
            sprite.y = 35
            Tile13 = False
            Tile5 = True
        if sprite.x > 850:
            sprite.x = 40
            Tile13 = False
            Tile14 = True
        if sprite.y < 25:
            sprite.y = 600
            Tile13 = False
            Tile18 = True
    if Tile14:
        draw_tile_14()
        if sprite.x < 35:
            sprite.x = 845
            Tile14 = False
            Tile13 = True
        if sprite.y > 625:
            sprite.y = 35
            Tile14 = False
            Tile6 = True
        if sprite.y < 25:
            sprite.y = 600
            Tile14 = False
            Tile19 = True
        if sprite.x > 850:
            sprite.x = 40
            Tile14 = False
            Tile15 = True
    if Tile15:
        draw_tile_15()
        if sprite.y > 625:
            sprite.y = 35
            Tile15 = False
            Tile10 = True
        if sprite.x > 850:
            sprite.x = 40
        if sprite.x < 35:
            sprite.x = 845
            Tile15 = False
            Tile14 = True
        if sprite.y < 25:
            sprite.y = 600
            Tile15 = False
            Tile20 = True
    if Tile17:
        draw_tile_17()
        if sprite.x > 850:
            sprite.x = 40
            Tile17 = False
            Tile18 = True
        if sprite.y > 625:
            sprite.y = 35
            Tile17 = False
            Tile12 = True
        if sprite.x < 35:
            sprite.x = 845
        if sprite.y < 25:
            sprite.y = 600
    if Tile18:
        draw_tile_18()
        if sprite.bottom_touches(key, -40, 5):
            key.x = 900
        if sprite.x < 35:
            sprite.x = 845
            Tile18 = False
            Tile17 = True
        if sprite.y > 625:
            sprite.y = 35
            Tile18 = False
            Tile13 = True
        if sprite.x > 850:
            sprite.x = 40
            Tile18 = False
            Tile19 = True
        if sprite.y < 25:
            sprite.y = 600
        touched_key = True
    if Tile19:
        draw_tile_19()
        if sprite.x < 35:
            sprite.x = 845
            Tile19 = False
            Tile18 = True
        if sprite.y > 625:
            sprite.y = 35
            Tile19 = False
            Tile14 = True
        if sprite.x > 850:
            sprite.x = 40
            Tile19 = False
            Tile20 = True
        if sprite.y < 25:
            sprite.y = 600
    if Tile20:
        draw_tile_20()
        if sprite.y > 625:
            sprite.y = 35
            Tile20 = False
            Tile15 = True
        if sprite.x > 850:
            sprite.x = 40
        if sprite.x < 35:
            sprite.x = 845
            Tile20 = False
            Tile19 = True
        if sprite.y < 25:
            sprite.y = 600
game_on = False
ending_current = False
tut = False
def game_start():
    """
    This function is designed to allow the player to start the game.
    :return:
    """
    global game_on
    global tut
    global ending_current
    if not game_on and not ending_current:
        camera.clear("black")
        mothman = uvage.from_text(400, 150, "MOTHMAN", 150, "red", bold=True)
        start = uvage.from_text(400, 250, "Press SPACE to start", 50, "white", bold=True)
        camera.draw(mothman)
        camera.draw(start)
        if uvage.is_pressing("space"):
            tut = True

seconds1 = 0
bg = False
def tutorial():
    """
    This function is designed to provide necessary information about moving and losing before the player starts.
    :return:
    """
    global game_on
    global bg
    global tut
    if tut:
        camera.clear("black")
        mov = uvage.from_text(400, 200, "Press WASD to move", 100, "white")
        exit = uvage.from_text(400, 325, "Press E to exit tutorial", 50, "white")
        timer = uvage.from_text(400, 270, "Dawn breaks when the timer reaches 100", 40, "white")
        camera.draw(timer)
        camera.draw(mov)
        camera.draw(exit)
        if uvage.is_pressing("e"):
            tut = False
            bg = True
            #game_on = True
def background():
    """
    This function is designed to offer a little backstory to the player of their character before they begin playing.
    :return:
    """
    global game_on
    global bg
    if bg:
        camera.clear("black")
        identity = uvage.from_text(400, 150, "You are a journalist.", 50, "white")
        goal = uvage.from_text(400, 200, "You are about to be fired.", 30, "white")
        location = uvage.from_text(400, 225, "You have decided to explore the forests of West Virginia,", 30, "white")
        location2 = uvage.from_text(400, 250, "in the hopes of finding Mothman and keeping your job.", 30, "white")
        timer = uvage.from_text(440, 275, "You only have until dawn before you lose your job...", 30, "white")
        exit = uvage.from_text(400, 335, "Press SPACE to exit", 50, "white")
        camera.draw(identity)
        camera.draw(goal)
        camera.draw(timer)
        camera.draw(location)
        camera.draw(location2)
        camera.draw(exit)
        if uvage.is_pressing("space"):
            bg = False
            game_on = True
already_opened = False
#USED ONCE KEY IS AQUIRED OR BEFORE KEY IS AQUIRED
def shed1():
    """
    This function is dsigned to tell the player that the shed is locked if they have not yet aquired a key, and to
    allow the player to unlock the shed if they have aquired the key. They wil then get a gun. This also prompts
    mothman to spawn in Tile15, in which he previously cannot be found. this step is necessary for game progression
    for endings 1 and 2.
    :return:
    """
    global Tile17
    global touched_key
    global already_opened
    if Tile17:
        if 300 < sprite.x < 500 and 165 < sprite.y <= 180:
            if not already_opened and touched_key:
                camera.clear("black")
                action = uvage.from_text(400, 200, "KEY used to unlock SHED", 50, "white")
                gun = uvage.from_text(400, 300, "GUN with single bullet aquired", 50, "red")
                exit = uvage.from_text(400, 400, "Press E to Confirm", 50, "white")
                camera.draw(action)
                camera.draw(gun)
                camera.draw(exit)
                if uvage.is_pressing("e"):
                    already_opened = True
                    touched_key = False
            elif not already_opened and not touched_key:
                camera.clear("black")
                text = uvage.from_text(400, 250, "This door is locked.", 100, "white")
                camera.draw(text)
purg = False
def staircase():
    """
    This function is designed to allow the play to climb the stairs if they stand in front of the stairs.
    :return:
    """
    global Tile20
    global purg
    if Tile20:
        if 350 < sprite.x < 450 and 305 < sprite.y <= 320:
            camera.clear("black")
            climb = uvage.from_text(400, 150, "Press SPACE to climb stairs", 50, "white")
            leave = uvage.from_text(400, 250, "Move from stairs to exit", 50, "white")
            camera.draw(climb)
            camera.draw(leave)
            if uvage.is_pressing("space"):
                purg = True
seconds = 0
e1 = False
purg_description = False

def purg_e():
    """
    This function is designed to display the ending title for ending 3.
    :return:
    """
    global purg
    global purg_description
    if purg:
        camera.clear("black")
        text = uvage.from_text(400, 200, "PURGATORY", 100, "red", bold=True)
        exit = uvage.from_text(400, 350, "Press C to continue", 50, "white")
        camera.draw(text)
        camera.draw(exit)
        if uvage.is_pressing("c"):
            purg_description = True
            purg = False

def purg_text():
    """
    This function is designed to display the ending description for the third possible ending of the game.
    :return:
    """
    global purg_description
    global game_on
    global Tile20
    global Tile1
    if purg_description:
        camera.clear("black")
        msg = uvage.from_text(400, 200, "The search for the missing journalist continues.", 45, "white")
        msg2 = uvage.from_text(400, 250, "Police urge anyone with information to call their tip line.", 35, "white")
        ending = uvage.from_text(400, 300, "Ending 3/3", 45, "white")
        camera.draw(msg)
        camera.draw(msg2)
        camera.draw(ending)

seconds = 0
score = 0
lose_game = False
def time_counter():
    """
    This function is designed to keep track of the time. If the timer reaches 100, the player will lose.
    :return:
    """
    global seconds
    global score
    global game_on
    global lose_game
    if game_on:
        seconds += 1
        if seconds > 30:
            score += 1
            seconds = 0
        time_in_game = uvage.from_text(400, 50, str(score), 50, "yellow", bold=True)
        camera.draw(time_in_game)
        if score >= 100:
            lose_game = True

def lose():
    """
    This function is designed for f the timer reaches 100, in which you lose the game.
    :return:
    """
    if lose_game:
        camera.clear("black")
        game_over = uvage.from_text(400, 250, "GAME OVER", 100, "red", bold=True)
        camera.draw(game_over)

def tick():
    """
    This function is designed to imlement all other function to run the game.
    :return:
    """
    global game_on
    global tut
    global ending_current
    game_start()
    tutorial()
    background()
    if game_on:
        draw_tiles()
        move_sprite()
        shed1()
        draw_note()
        staircase()
        time_counter()
        purg_e()
        purg_text()
        stair_text()
        ending_choices()
        bad_ending1()
        bad_ending2()
        good_ending1()
        good_ending2()
        lose()
    mothman_final()
    camera.display()

uvage.timer_loop(30, tick)