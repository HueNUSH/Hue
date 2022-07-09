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
      This is module {{$route.params.module_id}} and unit {{$route.params.unit_no}}, section {{$route.params.section}}
    </p>

    <div v-if="$route.params.section == 'pdf'">
        <!-- <vue-pdf-app style="height:100vh;width: 128vh;" :pdf="pdfLink"></vue-pdf-app> -->
        <embed :src="pdfLink" style="width:100%;height: 100vh;">
    </div>

    
    <div v-else-if="$route.params.section == 'pptx'">
        <iframe :src="pptxLink" frameborder="0" width="960" 
        height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    </div>

    
    <div v-else-if="$route.params.section == 'mp4'">
        <p>We'll be hosting lecture recordings as unlisted YouTube videos for now</p>
        <iframe width="960" height="569" :src="mp4Link" title="Video Content" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

  </v-container>
</template>

<script>
export default {
  name: "UnitAbout",
  
  computed: {
    pdfLink(){
        return 'https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/pdfreference1.0.pdf';
    },
    pptxLink(){
      return "https://docs.google.com/presentation/d/e/2PACX-1vR6NICC42Gg7ZZiDnXS0x8DiFC68OKX5Priuh4QjiqYfXSdaiI1tlhLAK3_IMZsF_00eCrcQXC1KUeQ/embed?start=false&loop=false&delayms=3000";
    },
    mp4Link(){
      return "https://www.youtube.com/embed/Eh2CvFvRcPE"
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>