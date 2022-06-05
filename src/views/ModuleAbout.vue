<template>
  <v-container fluid class="px-12 py-6">
    <router-link :to="'/modules/' + $route.params.module_id">
      < Back to module
    </router-link>
    <h1>About this module</h1>
  </v-container>
</template>

<script>
export default {
  name: "ModuleAbout"
}
</script>

<style scoped>

</style>
