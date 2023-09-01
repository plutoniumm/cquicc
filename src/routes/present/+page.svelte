<script lang="ts">
  import CodeMirror from "svelte-codemirror-editor";

  import { markdown, markdownLanguage } from "@codemirror/lang-markdown";
  import { languages } from "@codemirror/language-data";
  import { dracula } from "thememirror";
  import { onMount } from "svelte";

  import { defStyles } from "../utils";
  import { render } from "./utils";

  let value = "";
  let TA = "";
  let frame, old, doc;

  const write = (text, store = true) => {
    const { html } = render(text);

    if (store) localStorage.setItem("cquicc-present", text);

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

  onMount(async () => {
    if (!doc) doc = frame.contentWindow.document;

    const demo = new URLSearchParams(location.search).get("demo");
    const code = localStorage.getItem("cquicc-present");

    if (code && !demo) {
      write(code);
      value = code;
    } else {
      const Template = (await import("./basic.md?raw")).default;
      write(Template, false);
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
    if (/print-pdf/g.test(location.search)) {
      window.frames[0].print();
    }
  };

  const keyup = (e) => {
    if (e.key === "p" && e.ctrlKey) print();
  };
</script>

<svelte:window on:keyup={keyup} />

<div class="f j-ar p-fix w-50" id="funcs">
  <div class="rx10 ptr" on:click={print}>TogglePrint</div>
  <div class="rx10 ptr" on:click={triggerPrint}>Print</div>
  <div
    class="rx10 ptr"
    on:click={() => (TA = window.frames[0].document.body.innerHTML)}
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
