<template>
  <v-container fluid class="px-12 py-6">
    Home Page

    <br/>

    <v-btn to="/modules/1">
      This button brings you to a module
      <!--  For now this is hardcoded, when mongo db is set up, it should contain module name and id  -->
    </v-btn>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "Main",
  data: function () {
    return {
      name: "",
      mainOut: ""
    };
  },
});
</script>
