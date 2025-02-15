<script lang="ts">
    let { concept } : {
        concept: {
            id: number,
            title: string,
            abstract: string,
            created_at: string,
            updated_at: string,
            type: string
        }
    } = $props();

    $effect(() => {
        console.log(concept);
    })
</script>

<a href="/concept/{concept.type}/{concept.id}" class="category-preview">
    <h2 class="title">{concept.title}</h2>
    <div class="authors">Author 1, Author 2, Author 3</div>
    <div class="abstract">{concept.abstract}</div>
    <div class="content">Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim eum facilis aspernatur perferendis? Architecto aut esse repellat exercitationem. Quod laborum minus porro accusantium earum, ipsam omnis atque. Placeat, autem reprehenderit!</div>
</a>

<style>
    .category-preview {
        border-bottom: 1px solid rgba(0, 0, 0, 0.2);
        display: block;
        padding: 24px 0;
        width: 80%;
        margin-left: auto;
        margin-right: auto;
    }

    a {
        color: black;
        text-decoration: none;
    }
</style>