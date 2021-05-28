from PIL.Image import Image
from simpleimage import SimpleImage

INTENSITY_THRESHOLD=1.6  # A CONSTANT

# ---------------------APPLIES THE THE RED FILTER ON IMAGE------------------------
def red_filter(image):
    for pixels in image:
        pixels.blue = 0
        pixels.green = 0
    return image

# ---------------------APPLIES THE THE GREEN FILTER ON IMAGE------------------------
def green_filter(image):
    for pixels in image:
        pixels.blue = 0
        pixels.red = 0
    return image

# ---------------------APPLIES THE THE BLUE FILTER ON IMAGE------------------------
def blue_filter(image):
    for pixels in image:
        pixels.red = 0
        pixels.green = 0
    return image

# ---------------------APPLIES THE THE DARK FILTER ON IMAGE------------------------
def dark_filter(image):
    for pixels in image:
        pixels.red=pixels.red//2
        pixels.green=pixels.green//2
        pixels.blue=pixels.blue//2
    return image

# ---------------------APPLIES THE THE GREY FILTER ON IMAGE------------------------
def calc_brightness(red,green,blue):
    return (red*0.299) + (0.587*green) + (blue*0.114)

def grey_filter(image):
    for pixels in image:
        brightness=calc_brightness(pixels.red, pixels.green, pixels.blue)
        pixels.red=brightness
        pixels.green=brightness
        pixels.blue=brightness
    return image

# -----------------CHANGES THE BACKGROUND OF AN IMAGE WITH OTHER------------------------
def change_background(main_img,background_img):
# use the Constant Intensity Threshold vlaue as 1.6
    m_image=SimpleImage(main_img)
    b_image=SimpleImage(background_img)
    for pixels in m_image:
        avg= (pixels.red + pixels.green + pixels.blue)//3
        # check if the pixel is suffienciently green if yes then replace the pixels
        if pixels.blue >= avg * INTENSITY_THRESHOLD:
            x=pixels.x
            y=pixels.y
            m_image.set_pixel(x,y,b_image.get_pixel(x,y))
    return m_image

# ------------------------FINDS THE FLAMES OF FOREST-----------------------------
def find_flames(filename):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(filename)
    for pixels in image:
        avg= (pixels.red + pixels.green + pixels.blue)//3
        if pixels.red >= avg * INTENSITY_THRESHOLD:
            # INTENSITY_THRESHOLD must be used as 1.0
            pixels.red=255
            pixels.green=0
            pixels.blue=0
        else:
            pixels.red=avg
            pixels.green=avg
            pixels.blue=avg
    return image

# ---------------Flipping Effect on the Images--------------
def flip(image):
    width=image.width
    height=image.height
    mirror=SimpleImage.blank(width,height)
    for y in range(height):
        for x in range(width):
            pixel=image.get_pixel(x,y)
            mirror.set_pixel((width)-(x+1),y,pixel)
    return mirror

# ------------Filter of Indian Flag----------------
def Indra(image):
    width=image.width
    height=image.height
    
    for i in range(height//3):
        for j in range(width):
            pixel=image.get_pixel(j,i)
            pixel.blue=70
            pixel.green=150
            image.set_pixel(j,i,pixel)

    for i in range((height//2)+(height//3)//2,height):
        for j in range(width):
            pixel=image.get_pixel(j,i)
            pixel.red=0
            pixel.blue=0
            image.set_pixel(j,i,pixel)

    return image

# ---------------Diagonal Quote Filter for Square Images-------------
def QuoteMaker_1(image):
    width=image.width
    height=image.height

    for i in range(width):
        for j in range(height):
            if (i+j) >= (width-1):
                pixel=image.get_pixel(j,i)
                pixel.red=0
                pixel.green=0
                image.set_pixel(j,i,pixel)
    
    for pixels in image:
        pixels.red=pixels.red//2.5
        pixels.green=pixels.green//2.5
        pixels.blue=pixels.blue//2.5

    return image

# --------------Center Focused Quote Filter of any Size Images-------------
def QuoteMaker_2(image):
    width=image.width
    height=image.height

    for i in range(height//4,((height//2)+height)//2):
        for j in range(width):
                pixel=image.get_pixel(j,i)
                pixel.red=40
                pixel.green=50
                pixel.blue=80
                image.set_pixel(j,i,pixel)

    for pixels in image:
        pixels.red=pixels.red//1.75
        pixels.green=pixels.green//1.75
        pixels.blue=pixels.blue//1.75

    return image

def main():
    print("I thank Code In Place for helping me learn Python.\nRegards : Ritesh Gupta.")    
    while True:
        filename=get_file()
        image=SimpleImage(filename)
        print('''
        1) Indra Effect
        2) Red Filter
        3) Blue Filter
        4) Green Filter
        5) Dark Filter
        6) Grey Scale
        7) Forest Fire Detector
        8) Flip Effect
        9) Quote Effect 1 for Square Images
        10) Quote Effect 2\n''')
        inp=int(input("Input any Option to Apply Filter or\nPress Ctrl + C to exit : "))

# use of dictionary as an switch conditions
        switcher = {
            1:Indra,
            2:red_filter,
            3:green_filter,
            4:blue_filter,
            5:dark_filter,
            6:grey_filter,
            7:find_flames,
            8:flip,
            9:QuoteMaker_1,
            10:QuoteMaker_2
            }
        r=switcher.get(inp,"Invalid Input")(image)
        r.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter name of image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

if __name__ == '__main__':
    main()