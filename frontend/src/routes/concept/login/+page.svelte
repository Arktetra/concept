<!-- login page -->

<script lang="ts">
  import { writable } from "svelte/store";
  import { user } from "../../../state.svelte";

  let email = "john.doe@example.com";
  let password = "securepassword";
  let error = writable("");

  async function handleLogin() {
    try{
      const response = await fetch("auth/login", {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
          body: JSON.stringify({email, password}),
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error)
      }

      window.location.href = response.url;

      user.session = true;
    } catch (err) {
      if (err instanceof Error) {
        error.set(err.message);
      } else {
        error.set("An error occurred.");
      }
    }
  }
</script>

<div class="wrapper">
  <form on:submit|preventDefault={handleLogin}>
    <h2>Login</h2>
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
    {#if $error}
      <p class="error">{$error}</p>
    {/if}
    <button type="submit">Login</button>
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
  input {
    width: 100%;
    padding: 10px;
    margin-bottom: 1rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
    color: #333;
  }
  input:focus {
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
</style>
