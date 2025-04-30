import cairo

# Create a 200x100 image surface
with cairo.ImageSurface(cairo.FORMAT_ARGB32, 200, 100) as surface:
    ctx = cairo.Context(surface)
    
    # Set background to white
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    # Draw a red rectangle
    ctx.set_source_rgb(1, 0, 0)
    ctx.rectangle(10, 10, 180, 80)
    ctx.fill()

    # Save the image
    surface.write_to_png("example.png")

print("Image 'example.png' created.")
