<template>
  <v-container fluid class="px-12 py-6">
    <a id="back-link" :href="'/#/modules/' + $route.params.module_id + '/' + $route.params.unit_no">
      < Back to Unit
    </a>

    <p>Subchapter page</p>
  </v-container>
</template>

<script>
export default {
  name: "Subchapter"
}
</script>

<style>
#back-link {
  color: #55342A;
  font-size: larger;
}
</style>
