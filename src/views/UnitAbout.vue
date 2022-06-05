<template>
  <v-container fluid class="px-12 py-6">
    <router-link :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no">
      < Back to unit
    </router-link>
    <h1>About this unit</h1>
  </v-container>
</template>

<script>
export default {
  name: "UnitAbout"
};
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
</style>
