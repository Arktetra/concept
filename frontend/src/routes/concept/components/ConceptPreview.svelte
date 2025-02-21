<script lang="ts">
    import { goto } from "$app/navigation";
    import { deletePost } from "../../../callbacks.svelte";

    let { concept } : {
        concept: {
            id: number,
            title: string,
            abstract: string,
            created_at: string,
            updated_at: string,
            authors: string[],
            tags: string[],
            type: string
        }
    } = $props();

    let conceptHovered = $state(false);

    $effect(() => {
        console.log(concept);
    })
</script>

<div
    tabindex="0"
    role="button"
    aria-pressed="false"
    class="concept-container"
    onmouseenter={() => {conceptHovered = true;}}
    onmouseleave={() => {conceptHovered = false;}}
>
    <a
        href="/concept/{concept.type}/{concept.id}"
        class="category-preview"
    >
        <h2 class="title">{concept.title}</h2>
        <div class="authors">{concept.authors.join(", ")}</div>
        <div class="tags">
            {#each concept.tags as tag}
                <div class="tag">
                    {tag}
                </div>
            {/each}
        </div>
        <div class="abstract">{concept.abstract}</div>
    </a>
    {#if conceptHovered}
        <div class="options">
            <button id="edit" class="option">Edit</button>
            <button id="categorize" class="option">Categorize</button>
            <button
                id="delete"
                class="option"
                onclick={async () => {
                    if (concept.type === "posts") {
                        await deletePost(concept.id);
                        window.location.reload();
                    }
                }}
            >Delete</button>
        </div>
    {/if}
</div>

<style>
    .category-preview {
        border-bottom: 1px solid rgba(0, 0, 0, 0.2);
        display: block;
        padding: 24px 0px;
        margin: 0px;
        flex-grow: 3;
        /* width: 80%; */
        /* margin-left: auto; */
    }

    .concept-container {
        border-bottom: 1px solid rgba(0, 0, 0, 0.2);
        display: flex;
        margin-left: auto;
        margin-right: auto;
        width: 80%;
        justify-content: space-between;
        align-items: center;
    }

    .option {
        width: 100%;
        padding: 0px 10px;
        border-radius: 10px;
        border: none;
    }

    .option:hover {
        background-color: #000000dd;
        color: #ffffff;
        cursor: pointer;
    }

    .options {
        margin-right: auto;
        display: flex;
        flex-direction: column;
        gap: 1rem;
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
        margin: 10px 0px;
    }

    .title {
        margin: 0px;
    }

    .authors {
        margin: 5px 0px;
        color: rgb(0, 0, 0, 0.6);
    }

    .abstract {
        margin: 10px 0px;
        color: rgb(0, 0, 0, 0.8);
    }

    a {
        color: black;
        text-decoration: none;
    }
</style>