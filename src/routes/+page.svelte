<script lang="ts">
  import CodeMirror, { Renderer } from "sveltemirror";

  import { markdown, markdownLanguage } from "@codemirror/lang-markdown";
  import { languages } from "@codemirror/language-data";
  import { dracula } from "thememirror";
  import { onMount } from "svelte";

  import { mode } from "./config";
  import { prerender, isLocalHost } from "./lib/utils.js";

  let //
    value = "",
    TA = "",
    isEditor = true,
    preprocess;

  onMount(async () => {
    const url = new URL(location.href);
    let mod = url.searchParams.get("mode");
    if (!mod) mod = "doc";

    mod = mode[mod];
    preprocess = (text) => {
      if (text?.length < 1) return;
      localStorage.setItem(mod.memory, text);

      return mod.render(text).html;
    };

    const isLS = isLocalHost();
    const file = new URL(location.href).searchParams.get("file");

    let code = !file ? localStorage.getItem(mod.memory) : "";
    if (code.length > 1) {
      value = code;
    } else {
      value = await mod.useLocal(isLS, file);
      isEditor = !isLS || !file;
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
<main class="f fw" class:edOnly={!isEditor}>
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
      styles={{
        "&": {
          fontSize: "18px",
          height: "100%",
          width: "100%",
        },
      }}
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

  .edOnly > .frame {
    width: 100%;
  }
  .edOnly > .editor {
    display: none;
  }

  .editor,
  .frame {
    height: 100%;
    background: #ccc;
    overflow-y: scroll;
  }
</style>
