<template>
  <v-container fluid class="px-12 py-6">
    <router-link to="/modules">
      < My modules
    </router-link>
    <h1>Units of a module</h1>
    <p>Module id: {{ $route.params.module_id }}</p>
    <p>This page will display all units</p>
    <v-btn to="/modules/1/1">
      Click me to go to unit 1
    </v-btn>
    <v-btn :to="'/modules/' + $route.params.module_id + '/about'">
      About this module
    </v-btn>
  </v-container>
</template>

<script>
export default {
  name: "ModuleUnits"
};
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
</style>
