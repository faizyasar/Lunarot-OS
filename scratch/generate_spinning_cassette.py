import asyncio
import os
import io
import sys
from PIL import Image
from playwright.async_api import async_playwright

async def generate_gif_and_webp():
    html_path = os.path.abspath(r'C:\Users\faizy\Desktop\Anatomy fixed Casette new.html')
    file_url = f'file:///{html_path.replace("\\", "/")}'
    
    num_frames = 60
    fps = 25
    frame_duration_ms = int(1000 / fps) # 40ms per frame
    
    frames = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='msedge', headless=True)
        page = await browser.new_page(viewport={'width': 600, 'height': 600})
        
        await page.goto(file_url, wait_until='networkidle')
        await asyncio.sleep(1.5)
        
        init_js = """
        () => {
            const stage = document.querySelector('three-d-stage');
            const THREE = stage._THREE;
            
            stage.style.background = 'transparent';
            document.body.style.background = 'transparent';
            document.documentElement.style.background = 'transparent';
            
            const sc = stage._scene;
            const root = sc.getObjectByName('compact_cassette_assembly');
            const caseG = sc.getObjectByName('storage_case');
            const cassette = sc.getObjectByName('cassette');
            
            if (caseG) caseG.visible = false;
            
            stage._renderer.setClearColor(0x000000, 0);
            
            stage._camera.position.set(0, 0.11, 0.15);
            stage._controls.target.set(0, 0, 0);
            stage._controls.update();
            
            stage._renderer.setAnimationLoop(null);
            
            window.__cassette_root = root;
            window.__cassette = cassette;
            window.__stage = stage;
            window.__THREE = THREE;
            return true;
        }
        """
        await page.evaluate(init_js)
        await asyncio.sleep(0.5)
        
        print(f"Capturing {num_frames} frames of 360-degree rotation...", flush=True)
        for i in range(num_frames):
            angle_rad = (2 * 3.141592653589793 * i) / num_frames
            reel_angle = (2 * 3.141592653589793 * i * 3) / num_frames
            
            render_frame_js = f"""
            () => {{
                const root = window.__cassette_root;
                const cassette = window.__cassette;
                const stage = window.__stage;
                
                root.rotation.y = {angle_rad};
                
                const rSupply = cassette.getObjectByName('reel_supply');
                const rTakeup = cassette.getObjectByName('reel_takeup');
                if (rSupply) rSupply.rotation.z = {reel_angle};
                if (rTakeup) rTakeup.rotation.z = {reel_angle};
                
                stage._renderer.render(stage._scene, stage._camera);
            }}
            """
            await page.evaluate(render_frame_js)
            png_bytes = await page.screenshot(omit_background=True, type='png')
            img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
            frames.append(img)
            
            if (i + 1) % 15 == 0:
                print(f"Captured frame {i+1}/{num_frames}", flush=True)
                
        await browser.close()
        
    print("Processing images into transparent WebP and GIF...", flush=True)
    
    desktop_webp = r"C:\Users\faizy\Desktop\cassette_spinning.webp"
    desktop_gif = r"C:\Users\faizy\Desktop\cassette_spinning.gif"
    
    # 1. Animated WebP (fast encoding, default method)
    print("Saving WebP...", flush=True)
    frames[0].save(
        desktop_webp,
        save_all=True,
        append_images=frames[1:],
        duration=frame_duration_ms,
        loop=0,
        quality=90,
        format="WEBP"
    )
    print(f"Saved WebP ({os.path.getsize(desktop_webp)} bytes)", flush=True)
    
    # 2. Animated GIF with alpha thresholding
    print("Saving GIF...", flush=True)
    gif_frames = []
    for f in frames:
        alpha = f.split()[3]
        p_frame = f.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
        mask = Image.eval(alpha, lambda a: 255 if a < 64 else 0)
        p_frame.paste(255, mask)
        p_frame.info['transparency'] = 255
        gif_frames.append(p_frame)
        
    gif_frames[0].save(
        desktop_gif,
        save_all=True,
        append_images=gif_frames[1:],
        duration=frame_duration_ms,
        loop=0,
        disposal=2,
        format="GIF"
    )
    print(f"Saved GIF ({os.path.getsize(desktop_gif)} bytes)", flush=True)
    
    print("ALL DONE SUCCESSFULLY!", flush=True)

if __name__ == '__main__':
    asyncio.run(generate_gif_and_webp())
