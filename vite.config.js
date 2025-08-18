import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    host: '0.0.0.0',  // Listen on all network interfaces
    port: 5173,       // Default Vite port
    strictPort: false, // Try another port if 5173 is in use
    open: false,      // Don't open browser automatically
  },
});
