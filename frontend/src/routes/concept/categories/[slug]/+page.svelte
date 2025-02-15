<script lang="ts">
    import type { PageData } from "./$types";
    import ConceptPreview from "../../components/ConceptPreview.svelte";

    let { data }: { data: PageData } = $props();
    console.log(data);
</script>

{#each data["posts"]! as post}
    <ConceptPreview concept={post}/>
{/each}