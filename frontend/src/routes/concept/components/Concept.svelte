<script lang="ts">
    import { onMount } from "svelte";
    import ConceptPreview from "./ConceptPreview.svelte";
    import { getConcepts } from "../../../callbacks.svelte";

    let concepts: {
        id: number,
        title: string,
        abstract: string,
        created_at: string,
        updated_at: string,
        authors: string[],
        type: string
    }[];

    onMount(async () => {
        concepts = await getConcepts();
        console.log(concepts);
    })
</script>

{#each concepts as concept}
    <ConceptPreview concept={concept}/>
{/each}