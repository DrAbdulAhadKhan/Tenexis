import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    port: 3000,
    host: '0.0.0.0',
    allowedHosts: true,
  },
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        products: resolve(__dirname, 'products.html'),
        osteotomy: resolve(__dirname, 'osteotomy.html'),
        osteotomy2: resolve(__dirname, 'osteotomy-2.html'),
        osteotomy3: resolve(__dirname, 'osteotomy-3.html'),
        osteotomy4: resolve(__dirname, 'osteotomy-4.html'),
        osteotomy5: resolve(__dirname, 'osteotomy-5.html'),
        kneePositioner: resolve(__dirname, 'knee-positioner.html'),
        booking: resolve(__dirname, 'booking.html'),
      },
    },
  },
})
