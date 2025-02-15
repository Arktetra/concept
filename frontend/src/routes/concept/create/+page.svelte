<script lang="ts">
    import { onMount } from "svelte";
    import { mdToHtml } from "../../../converter";
    import { concept, create } from "../../../state.svelte";

    onMount(() => {
        create.clicked = true;

        return () => create.clicked = false;
    });
</script>

<article class="concept">
    <div class="source">
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
        <div class="body">
            <textarea class="content internal"
                placeholder="Your concept..."
                bind:value={concept.content}
            ></textarea>
        </div>
    </div>
    <div class="render">
        <div class="title-block">
            <h1 class="title internal">{concept.title}</h1>
            <p class="abstract internal">{concept.abstract}</p>
        </div>
        <div
            class="body internal"
            style="
                display: flex;
                flex-direction: column;
                width: 100%;
                padding-bottom: 250px;">
            {@html mdToHtml(concept.content)}
        </div>
    </div>

</article>

<style>
    .concept {
        display: flex;
    }

    p, h1, textarea {
        margin: 0;
        padding: 0;
    }

    .source {
        display: flex;
        flex-direction: column;
        border-right: 1px solid rgb(0, 0, 0, 0.2);
    }

    .render {
        border-left: 1px solid rgb(0, 0, 0, 0.2);
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .render .body {
        width: 100%;
    }

    .render .body :global {
        * {
            width: 40vw;
        }
    }

    .title-block {
        padding: 1rem 0rem 1rem 0rem;
        display: flex;
        width: 100%;
        flex-direction: column;
        align-items: center;
        border-bottom: 1px solid rgb(0, 0, 0, 0.2);
    }

    textarea {
        resize: none;
        overflow: hidden;
        field-sizing: content;
        border: none;
    }

    textarea:focus {
        outline: none;
    }

    .title {
        padding: 1rem 0rem 1rem 0;
        font-size: 48px;
        margin-bottom: 0px;
        font-weight: bold;
    }

    .abstract {
        font-size: 18px;
    }

    .body {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-bottom: 250px;
    }

    .content, .render>.body {
        padding: 1rem 0rem 1rem 0;
        font-size: 18px;
    }

    .source, .render {
        width: 50vw;
    }

    .source, .render {
        height: 90vh;
        max-height: 90vh;
        overflow-y: scroll;
    }

    .internal {
        width: 40vw;
        font-family: 'Times New Roman', Times, serif;
    }

    .render .title {
        overflow-wrap: break-word;
    }

    @media only screen and (max-width: 768px) {
        .internal {
            width: 40vw;
        }


    }

    :global(html) {
        overflow-x: hidden;
        overflow-y: hidden;
    }

    ::-webkit-scrollbar {
        width: 5px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }

    ::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 5px;
    }
</style>