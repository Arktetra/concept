<script>
    import { discardCallback, publishCallback } from '../../callbacks.svelte';
    import { create, user } from '../../state.svelte';

    let { children } = $props();

</script>

<div class="header">
    <div class="nav-bar">
        <a href="/concept">
            <h1>Concept</h1>
        </a>
        <nav class="nav-links">
            {#if create.clicked}
                <!-- <a href="/concept"> -->
                    <button
                        id="publish"
                        class="post-related-button"
                        onclick={publishCallback}
                    >
                    Publish
                    </button>
                <!-- </a> -->
                <button
                    id="discard"
                    class="post-related-button"
                    onclick={discardCallback}
                >
                Discard
                </button>
            {:else}
                {#if user.email === ""}
                    <a href="/concept/register">Create</a>
                {:else}
                    <a href="/concept/create">Create</a>
                {/if}
            {/if}
            <a href="/concept/about">About</a>
            <a href="/concept/settings">Settings</a>
        </nav>
    </div>
    <hr>
</div>

{@render children()}

<style>
    :global(body) {
        margin: 0;  /* for removing space on left and right of hr */
    }

    .nav-bar {
        display: flex;
        justify-content: space-around;
        align-items: center;
    }

    .nav-links {
        display: flex;
        gap: 20px;
    }

    .nav-links > a {
        color: black;
    }

    .nav-links > a:link, a:visited {
        text-decoration: none;
    }

    .nav-links > a:active {
        text-decoration: underline;
    }

    .nav-links > a:hover {
        text-decoration: underline;
    }

    a {
        color: black;
        text-decoration: none;
    }

    .post-related-button {
        padding: 2px 10px 2px 10px;
        border-radius: 10px;
        border: 1px solid rgb(0, 0, 0, 0.2);
        color: white;
        cursor: pointer;
    }

    #publish {
        background-color: #1f951f;
    }

    #discard {
        background-color: #e82727;
    }

    #publish:hover {
        opacity: 0.9;
    }

    #discard:hover {
        opacity: 0.85;
    }

</style>