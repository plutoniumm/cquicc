<script>
  import A from "itarr";
  import list from "./imgur.txt?raw";
  let value = "";

  const images = new A(list.split("\n"))
    .filter(Boolean)
    .map((e) => {
      let [link, name] = e.split("::");
      if (!link.includes("i.imgur")) {
        link = `https://i.imgur.com/${link}.png`;
      }
      return [name || link, link];
    })
    .collect();

  function copyLink({ target: t }) {
    if (t.tagName === "IMG") {
      navigator.clipboard.writeText(t.src);
    }
  }

  function l(s) {
    return s.toLowerCase();
  }
</script>

<div
  id="search"
  class="p5 m5 p-fix"
  style="background: #fff;top:-5px;z-index:1;"
>
  <input
    type="text"
    placeholder="Search"
    bind:value
    class="rx5 p10 d-b mx-a w-50"
  />
</div>

<div
  class="f j-ar fw"
  on:click={copyLink}
  style="z-index: 0;padding-top:100px;"
>
  {#each images as image}
    {#if value.length > 1 ? l(image[0]).includes(l(value)) : true}
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
    &:hover {
      transform: scale(1.05);
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
