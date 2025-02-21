<script lang="ts">
    let { comment } : {
        comment: {
            user_name: string,
            comment_text: string,
            created_at: string
        }
    } = $props()
</script>

<div class="comment-container">
    <div class="metadata">
        <h3 class="user-name">{comment.user_name}</h3>
        <p class="date">{comment.created_at}</p>
    </div>
    <p>{comment.comment_text}</p>
</div>

<style>
    h3, p {
        margin: 0px;
        padding: 0px;
    }

    .comment-container {
        border-left: 1px solid rgb(0, 0, 0, 0.2);
        padding-left: 1em;
        margin-bottom: 1em;
    }

    .comment-container h3 {
        display: block;
    }

    .metadata {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 1em;
    }

    .date {
        color: rgb(0, 0, 0, 0.7);
    }
</style>