<script lang="ts">
  import CodeMirror, { Renderer } from "sveltemirror";

  import { markdown, markdownLanguage } from "@codemirror/lang-markdown";
  import { languages } from "@codemirror/language-data";
  import { dracula } from "thememirror";
  import { onMount } from "svelte";

  import { defStyles, render } from "./utils";

  let value = "";
  const preprocess = (text) => {
    const { html } = render(text || "");
    localStorage.setItem("cquicc-code", text);
    return html;
  };

  onMount(async () => {
    const code = localStorage.getItem("cquicc-code");

    if (code.length > 1) {
      value = code;
    } else {
      const Template = (await import("./basic.md?raw")).default;
      value = Template;
    }

    document.title += (-new Date()).toString(36);
  });

  const print = () => window.frames[0].print();
  const keyup = (e) => {
    if (e.key === "p" && e.ctrlKey) print();
  };
</script>

<svelte:window on:keyup={keyup} />

<div class="f j-ar p-fix" id="funcs">
  <div class="rx10 ptr" on:click={print}>PDF</div>
</div>
<main class="f fw">
  <div class="editor">
    <CodeMirror
      bind:value
      extensions={[
        markdown({
          base: markdownLanguage,
          codeLanguages: languages,
          completeHTMLTags: true,
        }),
        dracula,
      ]}
      styles={defStyles}
      lineWrapping={true}
      placeholder="Type some markdown here..."
    />
  </div>
  <div class="frame">
    <Renderer bind:value {preprocess} />
  </div>
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
  .frame {
    width: calc(100% - var(--split));
  }

  .editor,
  .frame {
    height: 100%;
    background: #ccc;
    overflow-y: scroll;
  }
</style>
