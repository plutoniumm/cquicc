<script lang="ts">
  import CodeMirror from "svelte-codemirror-editor";
  import { markdown } from "@codemirror/lang-markdown";
  import Template from "./basic.md?raw";
  import { dracula } from "thememirror";
  import { onMount } from "svelte";

  import { defStyles, render } from "./utils";

  let //
    frame,
    value = Template,
    old,
    doc;

  const write = (text) => {
    const { meta, html } = render(text);

    console.log(meta);

    doc.open();
    doc.write(html);
    doc.close();
  };

  const handleChange = () => {
    const current = value;
    if (old === current) return 0;

    old = current;
    write(current);
  };

  onMount(() => {
    if (!doc) doc = frame.contentWindow.document;
    write(Template);
  });
</script>

<main class="f fw">
  <div class="editor">
    <CodeMirror
      bind:value
      lang={markdown()}
      theme={dracula}
      styles={defStyles}
      lineWrapping={true}
      on:change={handleChange}
    />
  </div>
  <iframe id="mfWHAT" bind:this={frame} frameborder="0" title="Editor Output" />
</main>

<style>
  main {
    width: 100vw;
    height: 100vh;
    background: #888;
  }

  .editor,
  iframe {
    width: 50%;
    height: 100%;
    background: #ccc;
    overflow-y: scroll;
  }

  @media (max-width: 768px) {
    .editor,
    iframe {
      width: 100%;
      height: 50%;
    }
  }

  iframe {
    background: #eee;
  }
</style>
