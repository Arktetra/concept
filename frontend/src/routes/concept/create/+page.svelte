<script lang="ts">
</script>

<div class="popup-overlay" id="popupOverlay">
    <div class="popup" id="popup">
        <span class="close" id="closePopup">&times;</span>
        <div class="popup-content">
            <p>Select one of the following options:</p>
            <a id="createPost" href="/concept/create/post">Create Post</a>
            <a id="createCategory" href="/concept/create/category">Create Category</a>
        </div>
    </div>
</div>

<style>
    .popup-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
    }

    .popup {
        font-family: Arial, Helvetica, sans-serif;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }

    .popup-content {
        text-align: center;
    }

    .popup .close {
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 20px;
        cursor: pointer;
        color: #333;
    }

    .popup a {
        background-color: rgb(38, 84, 184);
        color: #fff;
        padding: 10px 0px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
        display: flex;
        flex-direction: column;
        text-decoration: none;
        width: 100%;
    }

    .popup a:hover {
        opacity: 0.9;
    }

    #createCategory {
        margin-top: 10px;
    }
</style>