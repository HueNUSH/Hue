<template>
  <v-container fluid class="font-size-16 pa-0">
    <!-- <router-link
      :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no"
      class="links"
    >
      &lt; Back to unit
    </router-link> -->
    <h1>{{sectionNameVal}}</h1>
    <p>
      {{ sectionDescVal }}
    </p>

    <div v-if="mediaTypeVal === 'pdf'">
      <embed src="https://files.catbox.moe/fvjz8b.pdf" style="width:100%;height: 100vh;">
    </div>

    <div v-else-if="mediaTypeVal === 'embed'">
      <iframe :src="sectionMediaVal" frameborder="0" width="960" height="569" allowfullscreen="true"
        mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    </div>

    <div v-else-if="mediaTypeVal === 'slides'">
      <!-- <iframe :src="sectionMediaVal" width="476px" height="288px" frameborder="0">This is an embedded <a target="_blank" href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps">Office</a>.</iframe> -->
      <iframe
        
        :src="sectionMediaVal"
        width="960px" height="569px" frameborder="0">This is an embedded <a target="_blank"
          href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank"
          href="https://office.com/webapps">Office</a>.</iframe>
    </div>


  </v-container>
</template>

<script lang="ts">
import { Sections } from "@/types/sections";
import Vue from "vue";
export default Vue.extend({
  name: "UnitAbout",
  props: ["sectionName","sectionDesc", "mediaType", "sectionMedia"],
  data: () => ({
    sectionDescVal: "",
    mediaTypeVal: "",
    sectionMediaVal: "",
    sectionNameVal:"",
    section: {} as Sections
  }),
  watch: {
    $props: {
      handler() {
        this.sectionDescVal = this.$props.sectionDesc;
        this.mediaTypeVal = this.$props.mediaType;
        this.sectionMediaVal = this.$props.sectionMedia;
        this.sectionNameVal = this.$props.sectionName;
      },
      deep: true,
      immediate: true
    }
  },
  methods: {
    async getSectionData(moduleId: string, unitIndex: string, sectionIndex: string) {
      await fetch(Vue.prototype.$backendLink + "/chokola/modules/get_section/?" + new URLSearchParams({
        "module_id": moduleId,
        "unit_index": unitIndex,
        "section_index": sectionIndex
      }), {
        method: "GET",
      }).then(
        response => response.json().then(
          data => {
            this.section = JSON.parse(JSON.stringify(data.data));
            this.sectionDescVal = this.section.sectionDesc;
            this.mediaTypeVal = this.section.mediaType;
            this.sectionMediaVal = this.section.sectionMedia;
            this.sectionNameVal = this.section.sectionName;
            console.log(this.section.sectionMedia)
          }
        )
      );
    }
  },
  async created() {
    this.getSectionData(this.$route.params.module_id, this.$route.params.unit_no, this.$route.params.section)
  }

});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
