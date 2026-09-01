import asyncio
import os
from playwright.async_api import async_playwright

async def run_render():
    html_path = os.path.abspath(r'C:\Users\faizy\Desktop\Anatomy fixed Casette new.html')
    file_url = f'file:///{html_path.replace("\\", "/")}'
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='msedge', headless=True)
        page = await browser.new_page(viewport={'width': 800, 'height': 800})
        
        await page.goto(file_url, wait_until='networkidle')
        await asyncio.sleep(2)
        
        js_code = """
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
            
            // Set clear color to transparent
            stage._renderer.setClearColor(0x000000, 0);
            
            // Fit camera to cassette
            const b = new THREE.Box3().setFromObject(cassette);
            const ctr = b.getCenter(new THREE.Vector3());
            stage._controls.target.copy(ctr);
            
            // Center the camera and focus on cassette alone
            stage._camera.position.set(0, 0.05, 0.18);
            stage._controls.target.set(0, 0, 0);
            stage._controls.update();
            
            stage._renderer.render(stage._scene, stage._camera);
            return { hasCassette: !!cassette, hasCaseG: !!caseG };
        }
        """
        res = await page.evaluate(js_code)
        print("JS Eval result:", res)
        await asyncio.sleep(0.5)
        
        out_png = os.path.abspath(r'scratch\test_cassette_no_cover.png')
        await page.screenshot(path=out_png, omit_background=True)
        print(f"Saved {out_png}")
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(run_render())
