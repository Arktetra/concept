<script lang="ts">
    import { text } from "@sveltejs/kit";
    import Comment from "./Comment.svelte";
    import { onMount } from "svelte";
    import { post, user } from "../../../state.svelte";
    import { goto } from "$app/navigation";
    import { addComment } from "../../../callbacks.svelte";

    let { comments, className } : {
        comments: {
            user_name : string,
            comment_text : string,
            created_at : string,
        }[],
        className: string
    } = $props();

    let commentArea;
    let textareaSelected = $state(false);
    let comment = $state("");

    async function commentCallback() {
        if (user.email === "") {
            goto("/concept/register");
        }

        await addComment(comment);

        textareaSelected = false;
        comment = "";
    }
</script>

<div class="comments-section">
    <h2 class={className}>Comments</h2>
    <textarea
        class={className}
        placeholder="Add a comment..."
        onfocus={() => {textareaSelected = true}}
        bind:value={comment}
        bind:this={commentArea}
    ></textarea>
    {#if textareaSelected}
        <div class="form-buttons {className}">
            <button
                id="cancel"
                onclick={() => {
                    comment = "";
                    textareaSelected = false;
                }}
            >
                Cancel
            </button>
            <button
                id="comment"
                class={comment === "" ? "inactive" : "active"}
                onclick={commentCallback}
            >
                Comment
            </button>
        </div>
    {/if}
    <div class="comments-container {className}">
        {#each comments as comment}
            <Comment comment={comment} />
        {/each}
    </div>
</div>

<style>
    button {
        border: none;
    }

    textarea {
        margin: 0rem 0px 1.5rem 0rem;
        padding: 5px;
        text-decoration: none;
        resize: none;
        overflow: hidden;
        field-sizing: content;
        border: none;
        border-bottom: 1px solid rgb(0, 0, 0, 0.2);
        font-family: 'Times New Roman', Times, serif;
        font-size: 16px;
    }

    textarea:focus {
        outline: none;
    }

    .comments-section {
        border-top: 1px solid rgb(0, 0, 0, 0.2);
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .form-buttons {
        display: flex;
        justify-content: end;
        gap: 1rem;
    }

    .form-buttons button {
        padding: 2px 10px;
        border-radius: 10px;
    }

    #comment {
        padding: 2px 10px;
        border-radius: 10px;
    }

    .inactive {
        background-color: #d3d3d3;
        color: rgb(255, 255, 255, 0.9);
    }

    .active:hover, #cancel:hover {
        cursor: pointer;
        opacity: 1.0;
        background-color: #000000dd;
        color: #ffffff;
    }
</style>