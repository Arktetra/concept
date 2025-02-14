<script lang="ts">
    import type { PageData } from "./$types";

    let { data }: { data: PageData } = $props();
</script>

<article class="concept">
    <div class="title">
        <h1 class="internal">{data.title}</h1>
        <p class="internal">{data.abstract}</p>
    </div>
    <!-- <hr> -->
    <!-- <div class="body">{@html data.content}</div> -->
    <div class="metadata">
        <div class="internal">Author:</div>
        <div class="internal">Published Date: {data.created_at}</div>
        <div class="internal">Updated Date: {data.updated_at}</div>
    </div>
    <div class="body">
        <div class="internal">
            {data.content}
        </div>
    </div>
</article>

<style>
    /* hr {
        border: 1px solid black;
    } */

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

    .internal {
        width: 50%;
    }

    .title>h1 {
        margin-bottom: 0px;
        font-size: 48px;
    }

    .metadata {
        padding: 1rem 0 1.5rem 0;
        margin: 0 0 1.5rem 0;
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
    }

    @media only screen and (max-width: 768px) {
        /* :global(body) {
            background-color: lightblue;
        } */
        .internal {
            width: 95vw;
        }
    }
</style>