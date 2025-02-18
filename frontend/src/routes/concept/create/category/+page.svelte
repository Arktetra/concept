<script lang="ts">
    import { onMount } from "svelte";
    import { concept, create } from "../../../../state.svelte";


    onMount(() => {
        create.clicked = true;
        create.type = "category";

        return () => create.clicked = false;
    })
</script>

<article class="category">
    <div class="title-block">
        <textarea
            class="title internal"
            placeholder="Title"
            bind:value={concept.title}
        ></textarea>
        <textarea
            class="abstract internal"
            placeholder="Abstract"
            bind:value={concept.abstract}
        ></textarea>
    </div>
</article>

<style>
    textarea {
        margin: 0;
        padding: 0;
        resize: none;
        overflow: hidden;
        field-sizing: content;
        border: none;
    }

    textarea:focus {
        outline: none;
    }

    .abstract {
        font-size: 18px;
    }

    .category {
        display: flex;
        justify-content: center;
    }

    .internal {
        width: 50vw;
        font-family: 'Times New Roman', Times, serif;
    }

    .title-block {
        display: flex;
        flex-direction: column;
    }

    .title {
        padding: 1rem 0rem 1rem 0;
        font-size: 48px;
        margin-bottom: 0px;
        font-weight: bold;
        overflow-wrap: break-word;
    }

    @media only screen and (max-width: 786px) {
        .internal {
            width: 90vw;
        }
    }
</style>