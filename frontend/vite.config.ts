import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		proxy: {
			'/auth/login': 'http://127.0.0.1:5000',
			'/auth/register': 'http://127.0.0.1:5000',
			'/blog/posts/get': 'http://127.0.0.1:5000'
		}
	}
});
