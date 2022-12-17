from PIL import Image, ImageDraw
im  =  Image.new ( "RGB", (1000, 500), "#7b68ee" )
draw = ImageDraw.Draw(im)
draw.rectangle((-500, 500, 1000, 200), fill='#7a29a3', outline=(0, 0, 0))
draw.rectangle((-500, 500, 1000, 200), fill='#7a69a3', outline=(0, 0, 0))
im.save("new.png", "PNG")
draw.text((150,150),'Hello World',fill=('#d0b2d6'))
im.save("text.png")


