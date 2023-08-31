import { vitePreprocess } from '@sveltejs/kit/vite';
import adapter from '@sveltejs/adapter-static';

const excludes = [
  "a11y-no-static-element-interactions",
  "a11y-click-events-have-key-events"
];

/** @type {import('@sveltejs/kit').Config} */
export default {
  preprocess: vitePreprocess(),
  kit: {
    adapter: adapter()
  },
  onwarn: ( warning, handler ) => {
    if ( excludes.includes( warning.code ) ) return;
    handler( warning );
  }
};