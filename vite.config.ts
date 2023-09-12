import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

function docsHMR () {
  return {
    name: 'custom-hmr',
    enforce: 'post',
    handleHotUpdate ({ file, server }) {
      if (file.endsWith('.md')) {
        server.ws.send({
          type: 'full-reload',
          path: '*'
        });
      }
    },
  }
}

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    sveltekit(), docsHMR()
  ],
  server: {
    port: 3000,
  }
})
