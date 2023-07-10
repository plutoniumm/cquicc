<script lang="ts">
  import CodeMirror from "svelte-codemirror-editor";
  import { html } from "@codemirror/lang-html";
  import Template from "./basic.html?raw";
  import { dracula } from "thememirror";
  import { onMount } from "svelte";
  import { marked } from "marked";

  let //
    frame,
    value = Template,
    old,
    doc;

  const write = (text) => {
    doc.open();
    doc.write(text);
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

  // is iframe
  const isTop = () => {
    try {
      return window.top === window.self;
    } catch (e) {
      return false;
    }
  };

  const handleMessage = ({ data }) => {
    if (isTop()) return 0; // ignore if !embeded
    if (data.type !== "code") return 0; // ignore if not code

    const { code } = data;
    value = code;
    write(code);
  };
</script>

<svelte:window on:message={handleMessage} />

<main class="f fw">
  <div class="editor">
    <CodeMirror
      bind:value
      lang={html()}
      theme={dracula}
      styles={{
        "&": {
          fontSize: "18px",
          height: "100%",
          width: "100%",
        },
      }}
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
