<!-- login page -->

<script lang="ts">
  import { writable } from "svelte/store";
  import { loginCallback } from "../../../callbacks.svelte";

  let email = "";
  let password = "";
  let error = writable("");
</script>

<div class="wrapper">
  <form on:submit|preventDefault={() => loginCallback(email, password)}>
    <h2>Login</h2>
    <p>Create a <a href="/concept/register">new account</a>.</p>
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
