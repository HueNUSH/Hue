<template>
  <v-container fluid class="px-12 py-6">
    <p> Modules page </p>
    <p> Module id: {{ $route.params.module_id }}</p>
    <p>This page will display all units</p>
    <v-btn to="/modules/1/1">
      Click me to go to unit 1
    </v-btn>
  </v-container>
</template>

<script>
export default {
  name: "modules"
}
</script>

<style scoped>

</style>
