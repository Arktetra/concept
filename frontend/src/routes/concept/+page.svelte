<script lang="ts">
    import Concept from "./components/Concept.svelte";
</script>

<Concept />

<style>
    :global(html) {
        overflow-x: hidden;
    }

    :global(::-webkit-scrollbar) {
        width: 5px;
    }

    :global(::-webkit-scrollbar-track) {
        background: #f1f1f1;
    }

    :global(::-webkit-scrollbar-thumb) {
        background: #888;
        border-radius: 5px;
    }
</style>