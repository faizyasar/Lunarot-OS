import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import {defineConfig} from 'vite';
import {viteSingleFile} from 'vite-plugin-singlefile';
import {execSync} from 'child_process';

let commitHash = 'DEV';
try {
  commitHash = execSync('git rev-parse --short HEAD').toString().trim();
} catch (e) {}

export default defineConfig(() => {
  return {
    plugins: [react(), tailwindcss(), viteSingleFile()],
    define: {
      __BUILD_COMMIT_HASH__: JSON.stringify(commitHash),
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    server: {
      hmr: process.env.DISABLE_HMR !== 'true',
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
  };
});
