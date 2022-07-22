<template>
  <v-container fluid class="font-size-16 pa-0">
    <!-- <router-link
      :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no"
      class="links"
    >
      &lt; Back to unit
    </router-link> -->
    <h1>This section tests {{$route.params.section}} rendering</h1>
    <p>
      This is module {{$route.params.module_id}} and unit {{$route.params.unit_no}}, section {{this.$props.sectionDesc}}
    </p>

    <div v-if="this.$props.mediaType === 'pdf'">
        <embed :src="this.$props.sectionMedia" style="width:100%;height: 100vh;">
    </div>

    <div v-else-if="this.$props.mediaType === 'embed'">
        <iframe :src="this.$props.sectionMedia" frameborder="0" width="960"
        height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    </div>

    <div v-else-if="this.$props.mediaType === 'slides'">
        <iframe src="this.$props.sectionMedia" width="476px" height="288px" frameborder="0">This is an embedded <a target="_blank" href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps">Office</a>.</iframe>
    </div>


  </v-container>
</template>

<script>
export default {
  name: "UnitAbout",
  props: ["sectionDesc", "mediaType", "sectionMedia"]
};
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";

</style>
