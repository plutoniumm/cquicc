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
</script>

<div class="p5 f j-ar" id="functions">
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div class="p10 rx5" on:click={() => window.frames[0].print()}>print</div>
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
    <!-- theme={dracula} -->
  </div>
  <iframe id="mfWHAT" bind:this={frame} frameborder="0" title="Editor Output" />
</main>

<style lang="scss">
  #functions {
    background: #222;
    color: #fff;
    div {
      background: #000;
      transition: background 0.2s ease-in-out;
      &:hover {
        background: #8888;
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
