<p>Todo</p>
<a href="/home">Home</a>

<script>
    // Reactive variables for settings
    let theme = 'light'; // Default theme
    let notificationsEnabled = true; // Default notification preference
    let username = 'YourName'; // Default username
    let email = 'your_email@example.com'; // Default email

    // Function to save settings
    function saveSettings() {
        alert('Settings saved!');
        // Here, you can add logic to send the updated settings to your backend/database
    }
</script>

<style>
    /* General Styles */
    .settings-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        font-family: 'Arial', sans-serif;
    }

    h1 {
        font-size: 2.5rem;
        margin-bottom: 20px;
        color: #333;
        text-align: center;
    }

    .setting-card {
        background: #fff;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    .setting-card h2 {
        font-size: 1.5rem;
        margin-bottom: 15px;
        color: #444;
    }

    label {
        display: block;
        margin-bottom: 15px;
        font-size: 1rem;
        color: #666;
    }

    select, input[type="text"], input[type="email"] {
        width: 100%;
        padding: 10px;
        font-size: 1rem;
        border: 1px solid #ddd;
        border-radius: 5px;
        margin-top: 5px;
    }

    /* Toggle Switch */
    .toggle-switch {
        position: relative;
        display: inline-block;
        width: 50px;
        height: 25px;
    }

    .toggle-switch input {
        opacity: 0;
        width: 0;
        height: 0;
    }

    .slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: #ccc;
        border-radius: 25px;
        transition: 0.3s;
    }

    .slider:before {
        position: absolute;
        content: '';
        height: 21px;
        width: 21px;
        left: 2px;
        bottom: 2px;
        background: #fff;
        border-radius: 50%;
        transition: 0.3s;
    }

    input:checked + .slider {
        background: #7c3aed; /* Purple accent color */
    }

    input:checked + .slider:before {
        transform: translateX(25px);
    }

    /* Save Button */
    .save-button {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        padding: 12px 24px;
        background: #7c3aed; /* Purple accent color */
        color: #fff;
        border: none;
        border-radius: 5px;
        font-size: 1rem;
        cursor: pointer;
        transition: background 0.3s ease;
        margin-top: 20px;
    }

    .save-button:hover {
        background: #6d28d9; /* Darker purple on hover */
    }


</style>

<!-- Settings Section -->
<div class="settings-container">
    <h1>Settings</h1>

    <!-- Theme Selection Card -->
    <div class="setting-card">
        <h2>Theme</h2>
        <label>
            Select Theme:
            <select bind:value={theme}>
                <option value="light">Light</option>
                <option value="dark">Dark</option>
            </select>
        </label>
    </div>

    <!-- Notifications Card -->
    <div class="setting-card">
        <h2>Notifications</h2>
        <label>
            Enable Notifications:
            <div class="toggle-switch">
                <input type="checkbox" bind:checked={notificationsEnabled} />
                <span class="slider"></span>
            </div>
        </label>
    </div>

    <!-- Account Information Card -->
    <div class="setting-card">
        <h2>Account Information</h2>
        <label>
            Username:
            <input type="text" bind:value={username} />
        </label>
        <label>
            Email:
            <input type="email" bind:value={email} />
        </label>
    </div>

    <!-- Save Button -->
    <button class="save-button" on:click={saveSettings}>
        
        Save Changes
    </button>
</div>