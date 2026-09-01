import os
from PIL import Image

def optimize_gif(input_path, output_path):
    print("Optimizing GIF...")
    im = Image.open(input_path)
    frames = []
    try:
        while True:
            frames.append(im.copy())
            im.seek(len(frames))
    except EOFError:
        pass
    
    # Save optimized version with palette optimization
    first_frame = frames[0]
    first_frame.save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=17,
        loop=0,
        optimize=True,
        disposal=2
    )
    print(f"Compressed GIF size: {os.path.getsize(output_path)} bytes")

optimize_gif(r'C:\Users\faizy\Desktop\cd_jewel_case_spinning.gif', r'C:\Users\faizy\Desktop\cd_jewel_case_spinning_compressed.gif')
