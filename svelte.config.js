import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const excludes = [
  "a11y-no-static-element-interactions",
  "a11y-click-events-have-key-events"
];

export default {
  preprocess: vitePreprocess(),
  onwarn: ( warning, handler ) => {
    if ( excludes.includes( warning.code ) ) return;
    handler( warning );
  }
};