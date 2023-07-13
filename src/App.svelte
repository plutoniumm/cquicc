<script lang="ts">
  import CodeMirror from "svelte-codemirror-editor";

  import { markdown, markdownLanguage } from "@codemirror/lang-markdown";
  import { languages } from "@codemirror/language-data";
  import Template from "./basic.md?raw";
  import { dracula } from "thememirror";
  import { onMount } from "svelte";

  import { defStyles, render } from "./utils";

  let value = Template;
  let frame, old, doc;

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

  $: zoom = 1;
  $: zoomStyle = [
    [`zoom:`, zoom],
    [`-webkit-transform`, `scale(${zoom})`],
    [`-moz-transform`, `scale(${zoom})`],
  ]
    .map((x) => x.join(":"))
    .join(";");

  const print = () => window.frames[0].print();
</script>

<div class="p5 f j-ar" id="functions">
  <div class="p10 rx5" on:click={print}>print</div>
  <div class="f">
    <div class="p10 rx5" on:click={() => (zoom += 0.1)}>+</div>
    <div class="p10 rx5" on:click={() => (zoom -= 0.1)}>-</div>
  </div>
</div>
<main class="f fw">
  <div class="editor">
    <CodeMirror
      bind:value
      lang={markdown({
        base: markdownLanguage,
        codeLanguages: languages,
        completeHTMLTags: true,
      })}
      theme={dracula}
      basic={true}
      styles={defStyles}
      lineWrapping={true}
      placeholder="Type some markdown here..."
      on:change={handleChange}
    />
  </div>
  <iframe
    id="mfWHAT"
    bind:this={frame}
    frameborder="0"
    title="Editor Output"
    style={zoomStyle}
  />
</main>

<style lang="scss">
  iframe {
    transform-origin: 0 0;
    -webkit-transform-origin: 0 0;
    -moz-transform-origin: 0 0;
  }
  #functions {
    background: #222;
    color: #fff;
    .rx5 {
      background: #000;
      transition: background 0.2s ease-in-out;
      &:hover {
        background: #6664;
      }
    }
  }
  main {
    width: 100vw;
    height: calc(100vh - 2em - 16px);
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
