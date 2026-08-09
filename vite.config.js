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
        products2: resolve(__dirname, 'products-2.html'),
        products3: resolve(__dirname, 'products-3.html'),
        products4: resolve(__dirname, 'products-4.html'),
        products5: resolve(__dirname, 'products-5.html'),
        kneePositioner: resolve(__dirname, 'knee-positioner.html'),
        booking: resolve(__dirname, 'booking.html'),
      },
    },
  },
})
