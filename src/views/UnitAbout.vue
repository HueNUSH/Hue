<template>
  <v-container fluid class="font-size-16 pa-0">
    <!-- <router-link
      :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no"
      class="links"
    >
      < Back to unit
    </router-link> -->
    <h1>About this unit</h1>
    <p></p>
    <!-- <p>
      This is a demo unit and each section of it will test a different form of multimedia. 
      
    </p>
    <p>Please make sure that everything works fine on your end!</p> -->
    <p style="width:40%">{{this.$props.unitAbout}}</p>
  </v-container>
</template>

<script>
export default {
  name: "UnitAbout",
  props: ["unitAbout"]
};

</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
