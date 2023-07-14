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

  const print = () => window.frames[0].print();

  const keyup = (e) => {
    if (e.key === "p" && e.ctrlKey) print();
  };
</script>

<svelte:window on:keyup={keyup} />

<div class="f j-ar p-fix" id="funcs">
  <div class="rx10 ptr" on:click={print}>print</div>
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
    style="background:#888;"
  />
</main>

<style lang="scss">
  #funcs {
    color: #fff;
    bottom: 20px;
    right: 20px;
    z-index: 10000;
    .rx10 {
      padding: 10px;
      background: #2af;
      transition: opacity 0.2s ease-in-out;
      &:hover {
        opacity: 0.8;
      }
    }
  }
  main {
    width: 100vw;
    height: 100vh;
    background: #888;
    --split: 42%;
  }

  .editor {
    width: var(--split);
  }
  iframe {
    width: calc(100% - var(--split));
  }

  .editor,
  iframe {
    height: 100%;
    background: #ccc;
    overflow-y: scroll;
  }
</style>
