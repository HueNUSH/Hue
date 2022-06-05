<template>
  <v-container fluid class="px-12 py-6">
    <router-link :to="'/modules/' + $route.params.module_id">
      < Back to Module
    </router-link>
    <h1>Sections of a unit</h1>
    <p>Module id: {{ $route.params.module_id }}</p>
    <p>Unit no: {{ $route.params.unit_no }}</p>
    <v-btn :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no + '/about'">
      About this unit
    </v-btn>
  </v-container>
</template>

<script>
export default {
  name: "UnitSections"
};
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
</style>
