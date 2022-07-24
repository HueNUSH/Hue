<template>
  <v-container fluid class="px-12 py-6">
    <router-link to="/modules">
      < My modules
    </router-link>
    <h1>404 Not found, double check the link you went to</h1>
  </v-container>
</template>

<script>
import Vue from "vue";

export default Vue.extend({
  name: "NotFound",
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
