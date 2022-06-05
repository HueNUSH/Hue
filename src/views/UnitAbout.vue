<template>
  <v-container fluid class="px-12 py-6">
    <router-link :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no">
      < Back to unit
    </router-link>
    <p>About this unit</p>
  </v-container>
</template>

<script>
export default {
  name: "UnitAbout"
}
</script>

<style scoped>

</style>
