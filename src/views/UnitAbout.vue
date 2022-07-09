<template>
  <v-container fluid class="font-size-16 pa-0">
    <!-- <router-link
      :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no"
      class="links"
    >
      < Back to unit
    </router-link> -->
    <h1>About this unit</h1>
    <p>
      This is module {{$route.params.module_id}} and unit {{$route.params.unit_no}}
    </p>
  </v-container>
</template>

<script>
export default {
  name: "UnitAbout"
};
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
