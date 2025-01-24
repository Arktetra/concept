<!-- login page -->

<script lang="ts">
  import { login } from "$lib/api/auth";
  import { writable } from "svelte/store";

  let email = "john.doe@example.com";
  let password = "securepassword";
  let error = writable("");

  async function handleLogin() {
    try {
      const response = await login(email, password);
      console.log("login successfull: ", response);
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

<form on:submit|preventDefault={handleLogin}>
  <input type="email" bind:value={email} placeholder="Email" required />
  <input
    type="password"
    bind:value={password}
    placeholder="password"
    required
  />
  <button type="submit">Login</button>
</form>

{#if $error}
  <p style="color: red;">{$error}</p>
{/if}
