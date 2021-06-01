"""
This program generates the Warhol effect based on the original image.
"""
import random
from simpleimage import SimpleImage

N_ROWS = 3
N_COLS = 2
BORDER_SIZE = 10
PATCH_NAME = 'face2.jpeg'
PATCH_SIZE = 570 + BORDER_SIZE * 2
WIDTH = ((N_COLS * PATCH_SIZE) - (BORDER_SIZE * (N_COLS - 1)))
HEIGHT = (N_ROWS * PATCH_SIZE) - (BORDER_SIZE * (N_ROWS - 1))
# images/simba-sq.jpg


def main():
    # This makes a blank image with set height and width
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    # This nested loop works each individual row and col applying the code inside it to each patch
    for row in range(N_ROWS):
        for col in range(N_COLS):
            # This gives me a random color back to apply to each patch
            patch = add_border(make_recolored_patch(random.uniform(0, 2), random.uniform(0, 2), random.uniform(0, 2)), BORDER_SIZE)
            # This function gets 4 parameters passed into the code:
            # 1. image I want to apply the code to, 2. the position of the row, 3. the position of the col
            # 4. the filter applied to each patch
            add_patch(final_image, row, col, patch)
    print("yay")
    final_image.show()


def add_border(image, border_sz):
    new_width = image.width + border_sz * 2
    new_height = image.height + border_sz * 2
    border_image = SimpleImage.blank(new_width, new_height)
    for x in range(border_image.width):
        for y in range(border_image.height):
            if border_pixel(x, y, border_sz, border_image):
                pixel = border_image.get_pixel(x, y)
                pixel.red = 255
                pixel.green = 255
                pixel.blue = 255
            else:
                original_pixel = image.get_pixel(x - border_sz, y - border_sz)
                border_image.set_pixel(x, y, original_pixel)
    return border_image


def border_pixel(x, y, border_sz, border_image):
    if y < border_sz:
        return True
    if y >= border_image.height - border_sz:
        return True
    if x < border_sz:
        return True
    if x >= border_image.height - border_sz:
        return True
    return False

def add_patch(image, row, col, patch):
    # This nested loop, loops through each individual y and x value applying the code inside it
    for y in range(PATCH_SIZE):
        for x in range(PATCH_SIZE):
            # get pixel gives the current location of the start of the patch
            pixel = patch.get_pixel(x, y)
            # This code adds each patch to the next location, starting with (0, 0) and applying to every row & col
            image.set_pixel(x + (col * (PATCH_SIZE - BORDER_SIZE)), y + (row * (PATCH_SIZE - BORDER_SIZE)), pixel)


def make_recolored_patch(red_scale, green_scale, blue_scale):
    # This takes the patch and applies the random filter to every pixel in the patch
    patch = SimpleImage(input("Enter Image File here(or press enter for the default image): "))
    # if patch == '':
        # patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red = red_scale * pixel.red
        pixel.green = green_scale * pixel.green
        pixel.blue = blue_scale * pixel.blue
    # returns a new patch with a random filter
    return patch


if __name__ == '__main__':
    main()