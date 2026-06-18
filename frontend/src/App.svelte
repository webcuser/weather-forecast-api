<script>
import { onMount } from 'svelte';

let city = 'London';
let weather = {};

const fetchWeather = async () => {
    const res = await fetch(`http://localhost:8000/weather/${city}`);
    weather = await res.json();
};

onMount(() => {
    fetchWeather();
});
</script>

<main>
    <h1>Weather Forecast</h1>
    <input bind:value={city} placeholder="Enter city" />
    <button on:click={fetchWeather}>Get Weather</button>
    <pre>{JSON.stringify(weather, null, 2)}</pre>
</main>
