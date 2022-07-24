<template>
  <v-container fluid class="px-12 py-6">
    <router-link to="/modules">
      < My modules
    </router-link>
    <h1>500 Internal Server Error, we made an oopsie, please report this error to us</h1>
  </v-container>
</template>

<script>
export default {
  name: "ServerError"
};
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
