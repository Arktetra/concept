<script lang="ts">
    import { onMount } from "svelte";
    import { mdToHtml } from "../../../../converter";
    import { concept, create } from "../../../../state.svelte";

    onMount(() => {
        create.clicked = true;
        create.type = "post";

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
            <div class="tags internal">
                <label for="tags">tags:</label>
                <textarea
                    id="#tags"
                    class="tags internal"
                    bind:value={concept.tags}
                >
                </textarea>
            </div>
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
            <div class="tags internal">
                {#each new Set(concept.tags.trim().split(" ")) as tag}
                <div class="tag">
                    {tag}
                </div>
                {/each}
            </div>
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

    .tag {
        background-color: #d3d3d3;
        border-radius: 10px;
        padding: 0px 10px;
        color: #333333;
    }

    .tags {
        display: flex;
        font-size: 18px;
        gap: 5px;
    }

    .title {
        padding: 1rem 0rem 1rem 0;
        font-size: 48px;
        margin-bottom: 0px;
        font-weight: bold;
    }

    .abstract {
        font-size: 18px;
        padding-top: 10px;
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
        max-height: 87vh;
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
</style>