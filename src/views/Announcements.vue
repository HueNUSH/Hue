<template>
  <v-container fluid class="pb-6 pt-16" style="padding-left: 80px; padding-right: 100px">
    <h1>Announcements</h1>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { Announcement } from "@/types/announcement";

export default Vue.extend({
  name: "Announcements",
  data: () => ({
    announcements: [] as Array<Announcement>
  })
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
