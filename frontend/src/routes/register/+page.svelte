<script lang="ts">
  import { register } from "$lib/api/registration";
  import { writable } from "svelte/store";
  // Writable stores to hold form input values
  let userName = "";
  let email = "";
  let password = "";
  let mobile = "";
  let role = "";

  let error = writable("");
  let success = writable("");

  async function handleRegister() {
    try {
      const userData = {
        user_name: userName,
        email,
        password,
        mobile: mobile || undefined,
        role: role || undefined,
      };

      const response = await register(userData);
      console.log("Registration successful:", response);
      success.set("Registration successful!");
      error.set("");
    } catch (err) {
      if (err instanceof Error) {
        error.set(err.message);
      } else {
        error.set("An unknown error occurred.");
      }
    }
  }
</script>

<div class="wrapper">
  <form on:submit|preventDefault={handleRegister}>
    <h2>Register</h2>

    <label for="userName">Full Name</label>
    <input
      id="userName"
      type="text"
      bind:value={userName}
      placeholder="Enter your full name"
      required
    />

    <label for="email">Email</label>
    <input
      id="email"
      type="email"
      bind:value={email}
      placeholder="Enter your email"
      required
    />

    <label for="password">Password</label>
    <input
      id="password"
      type="password"
      bind:value={password}
      placeholder="Enter your password"
      required
    />

    <label for="mobile">Mobile (Optional)</label>
    <input
      id="mobile"
      type="tel"
      bind:value={mobile}
      placeholder="Enter your mobile number"
    />

    <label for="role">Role (Optional)</label>
    <select id="role" bind:value={role}>
      <option value="" disabled selected>Select a role</option>
      <option value="user">User</option>
      <option value="admin">Admin</option>
    </select>

    {#if $error}
      <p class="error">{$error}</p>
    {/if}
    {#if $success}
      <p class="success">{$success}</p>
    {/if}

    <button type="submit">Register</button>
  </form>
</div>

<style>
  .wrapper {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    margin: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  form {
    background: #ffffff;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 400px;
  }

  h2 {
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 1.5rem;
    color: #333;
  }

  label {
    display: block;
    margin-bottom: 0.5rem;
    font-size: 14px;
    color: #555;
  }

  input,
  select {
    width: 100%;
    padding: 10px;
    margin-bottom: 1rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
    color: #333;
  }

  input:focus,
  select:focus {
    border-color: #007bff;
    outline: none;
    box-shadow: 0 0 4px rgba(0, 123, 255, 0.25);
  }

  button {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    font-size: 16px;
    font-weight: bold;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  button:hover {
    background-color: #0056b3;
  }

  .error {
    color: red;
    font-size: 14px;
    margin-bottom: 1rem;
    text-align: center;
  }

  .success {
    color: green;
    font-size: 14px;
    margin-bottom: 1rem;
    text-align: center;
  }
</style>
