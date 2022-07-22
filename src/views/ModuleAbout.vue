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
    <p></p>
    <p style="width:40%">{{aboutText}}</p>
    
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "ModuleAbout",
  data: () => ({
    aboutText : "testest"
  }),
  methods: {
     async getModuleAbout(moduleId: string) {
     await fetch("https://nushigh.school/chokola/modules/get_module?" + new URLSearchParams({
        "module_id": moduleId
      }), {
        method: "GET",
      }).then(
        response => response.json().then(
          data => {
            this.aboutText = JSON.parse(JSON.stringify(data.data)).moduleAbout;
          }
        )
      );
    },
  },
  created() {
    console.log(this.aboutText);
    this.getModuleAbout(this.$route.params.module_id);
  }
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
