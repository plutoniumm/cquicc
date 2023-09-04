<script lang="ts">
  import CodeMirror, { Renderer } from "sveltemirror";

  import { markdown, markdownLanguage } from "@codemirror/lang-markdown";
  import { languages } from "@codemirror/language-data";
  import { dracula } from "thememirror";
  import { onMount } from "svelte";

  import { defStyles } from "../utils";
  import { render as rander, prerender } from "./utils";

  let value = "";
  let TA = "";

  const preprocess = (text) => {
    const { html } = rander(text || "");
    localStorage.setItem("cquicc-present", text);

    return html;
  };

  onMount(async () => {
    const code = localStorage.getItem("cquicc-present");

    if (code.length > 1) {
      value = code;
    } else {
      const Template = (await import("./basic.md?raw")).default;
      value = Template;
    }
    document.title += (-new Date()).toString(36);
  });

  const print = () => {
    // toggle ?print-pdf
    const url = /print-pdf/g.test(location.search)
      ? location.href.replace(/\?print-pdf/g, "")
      : location.href + "?print-pdf";

    // reload with new url
    window.location.href = url;
  };
  const triggerPrint = () => {
    if (/print-pdf/g.test(location.search)) window.frames[0].print();
  };

  const keyup = (e) => {
    if (e.key === "p" && e.ctrlKey) print();
  };
</script>

<svelte:window on:keyup={keyup} />

<div class="f j-ar p-fix w-50" id="funcs">
  <div class="rx10 p10 ptr" on:click={print}>TogglePrint</div>
  <div class="rx10 p10 ptr" on:click={triggerPrint}>Print</div>
  <div
    class="rx10 p10 ptr"
    on:click={() => (TA = prerender(window.frames[0].document.body))}
  >
    GetCode
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
      extensions={[dracula]}
      basic={true}
      styles={defStyles}
      lineWrapping={true}
      placeholder="Type some markdown here..."
    />
  </div>
  <div class="frame">
    <Renderer bind:value {preprocess} />
  </div>
</main>
{#if TA.length}
  <div class="p-fix blur tc" id="popup">
    <textarea name="code" bind:value={TA} class="rpm-10 flow-y-s" />
    <button
      class="d-b rx20 mx-a ptr"
      on:click={() => (TA = "")}
      style="color:#fff;background:#f00;width:50px;">X</button
    >
  </div>
{/if}

<style lang="scss">
  #popup {
    z-index: 100000;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    --bg: #2222;
    --sz: 16px;
    textarea {
      width: 80%;
      height: 80%;
      background: #222;
      color: #fff;
    }
  }
  #funcs {
    color: #fff;
    bottom: 20px;
    right: 20px;
    z-index: 10000;
    .rx10 {
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
