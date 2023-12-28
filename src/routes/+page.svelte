<script>
  import list from "./imgur.txt?raw";
  let //
    search,
    value = "";

  const images = list
    .split("\n")
    .filter(Boolean)
    .map((e) => {
      let [link, name] = e.split("::");
      if (!link.includes("i.imgur")) {
        link = `https://i.imgur.com/${link}.png`;
      }
      return [name || link, link];
    });

  function copyLink({ target: t }) {
    if (t.tagName === "IMG") {
      navigator.clipboard.writeText(t.src);
    }
  }

  function l(s) {
    return s.toLowerCase();
  }

  function activateSearch({ key }) {
    if (document.activeElement.tagName === "INPUT") return;
    if (key === "/") {
      search.focus();
    }
    return true;
  }

  $: s = (value, key) => {
    if (value.length < 2) return true;
    key = l(key);
    value = l(value).replaceAll(" ", ",").split(",");

    for (let i = 0; i < value.length; i++) {
      // if list is long we may need to use Fuse.js
      // very liberal search, ANY matches allowed
      if (key.includes(value[i])) return true;
    }
    return false;
  };
</script>

<svelte:window on:keyup={activateSearch} />

<div
  id="search"
  class="p5 m5 p-fix"
  style="background: #fff;top:-5px;z-index:1;"
>
  <input
    type="text"
    placeholder="Search"
    bind:value
    bind:this={search}
    class="rx5 p10 d-b mx-a w-50"
  />
</div>

<div
  class="f j-ar fw"
  on:click={copyLink}
  style="z-index: 0;padding-top:100px;"
>
  {#each images as image}
    {#if s(value, image[0])}
      <div class="p5">
        <img class="rx5 ptr" src={image[1]} alt={image[0]} />
        <div class="p5 tc link">{image[0]}</div>
      </div>
    {/if}
  {/each}
</div>

<style lang="scss">
  img {
    max-width: 300px;
    max-height: 400px;
    transform: scale(1);
    transition: transform 0.1s ease-in-out;
    z-index: 0;
    &:hover {
      z-index: 3;
      transform: scale(1.5);
    }
  }
  #search {
    width: calc(100% - 10px);
  }
  input {
    background: #eee;
  }

  .link {
    color: #888;
    opacity: 0.8;
    font-size: 0.8em;
  }
</style>
