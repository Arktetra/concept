<script lang="ts">
    import PostPreview from "./PostPreview.svelte";

    let n_posts = 5;
</script>

{#each {length: n_posts} as _, i}
    <PostPreview />
{/each}