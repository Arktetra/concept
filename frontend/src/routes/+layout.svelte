<script>
    let { children } = $props();
</script>

<div class="header">
    <div class="nav-bar">
        <h1>Concept</h1>
        <nav class="nav-links">
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/settings">Settings</a>
        </nav>
    </div>
    <hr>
</div>

{@render children()}

<style>
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
</style>