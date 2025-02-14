<script>
    let { children } = $props();
</script>

<div class="header">
    <div class="nav-bar">
        <a href="/concept">
            <h1>Concept</h1>
        </a>
        <nav class="nav-links">
            <a href="/about">About</a>
            <a href="/settings">Settings</a>
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
</style>