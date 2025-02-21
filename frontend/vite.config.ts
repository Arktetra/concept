import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		proxy: {
			'/accounts/login': 'http://127.0.0.1:5000',
			'/accounts/logout': 'http://127.0.0.1:5000',
			'/accounts/register': 'http://127.0.0.1:5000',
			'/categories/get': 'http://127.0.0.1:5000',
			'/comments/add': 'http://127.0.0.1:5000',
			'/concepts/get': 'http://127.0.0.1:5000',
			'/concepts/add': 'http://127.0.0.1:5000',
			'/posts/comments': 'http://127.0.0.1:5000',
			'/posts/delete': 'http://127.0.0.1:5000',
			'/posts/get': 'http://127.0.0.1:5000',
		}
	}
});
