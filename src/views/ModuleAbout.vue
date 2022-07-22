<template>
  <v-container fluid class="pb-6 pt-16" style="padding-left: 80px; padding-right: 100px">
    <router-link
      :to="'/modules/' + $route.params.module_id"
      class="links"
    >
      &lt; Back to module
    </router-link>
    <p></p>
    <h1>About this module</h1>
    
  </v-container>
</template>

<script>
export default {
  name: "ModuleAbout"
};
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
