<template>
  <v-container fluid class="px-12 py-6">
    <router-link :to="'/modules/' + $route.params.module_id">
      < Back to module
    </router-link>
    <p>About this module</p>
  </v-container>
</template>

<script>
export default {
  name: "ModuleAbout"
}
</script>

<style scoped>

</style>
