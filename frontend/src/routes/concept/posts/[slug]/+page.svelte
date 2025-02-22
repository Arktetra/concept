<script lang="ts">
    import { mdToHtml } from "../../../../converter";
import Comments from "../../components/Comments.svelte";
    import type { PageData } from "./$types";

    let { data }: { data: PageData } = $props();
</script>

<article class="concept">
    <div class="title">
        <h1 class="internal">{data.title}</h1>
        <p class="internal">{data.abstract}</p>
        <div class="tags internal">
            {#each data.tags as tag}
                <div class="tag">
                    {tag}
                </div>
            {/each}
        </div>
    </div>
    <!-- <hr> -->
    <!-- <div class="body">{@html data.content}</div> -->
    <div class="metadata">
        <div class="internal">Author: {data.authors.join(", ")}</div>
        <div class="internal">Published Date: {data.created_at}</div>
        <div class="internal">Updated Date: {data.updated_at}</div>
    </div>
    <div class="body">
        <div class="internal">
            {@html mdToHtml(data.content)}
        </div>
    </div>
    <Comments comments={data.comments} className="internal"/>
</article>

<style>
    :global(.internal) {
        width: 50%;
    }

    .tags {
        display: flex;
        gap: 5px;
    }

    .tag {
        background-color: #d3d3d3;
        border-radius: 10px;
        padding: 0px 10px;
        color: #333333;
    }

    .concept {
        display: flex;
        flex-direction: column;
        width: 100%;
        align-items: center;
    }

    .title {
        padding: 1rem 0rem 1rem 0rem;
        width: 100%;
        border-bottom: 1px solid rgba(0, 0, 0, 0.2);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .title>p {
        color: rgba(0, 0, 0, 0.8);
        font-size: 18px;
    }

    .title>h1 {
        margin-bottom: 0px;
        font-size: 48px;
    }

    .metadata {
        padding: 1rem 0 1rem 0;
        border-bottom: 1px solid rgb(0, 0, 0, 0.2);
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        color: rgba(0, 0, 0, 0.7);
        gap: 4px;
        font-size: 14px;
    }

    .body {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 1rem 0 1rem 0;
    }

    @media only screen and (max-width: 768px) {
        :global(.internal) {
            width: 95vw;
        }
    }
</style>