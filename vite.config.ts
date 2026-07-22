import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { execSync } from 'child_process';

let commitHash = 'DEV';
try {
  commitHash = execSync('git rev-parse --short HEAD').toString().trim();
} catch (e) {
  // fallback
}

export default defineConfig({
  plugins: [react()],
  define: {
    __BUILD_COMMIT_HASH__: JSON.stringify(commitHash),
  },
});
