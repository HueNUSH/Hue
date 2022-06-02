<template>
  <v-container fluid class="px-12 py-6">
    <a id="back-link" :href="'/#/modules/' + $route.params.module_id">
      < Back to Module
    </a>

    <p> Modules page </p>
    <p> Module id: {{ $route.params.module_id }}</p>
    <p> Unit no: {{ $route.params.unit_no}} </p>
    <v-btn to="/modules/1/1/1">
      Click me to go to Subchapter 1
    </v-btn>
  </v-container>
</template>

<script>
export default {
  name: "Unit"
}
</script>

<style>
#back-link {
  color: #55342A;
  font-size: larger;
}
</style>
