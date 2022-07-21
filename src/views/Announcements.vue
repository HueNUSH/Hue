<template>
  <v-container fluid class="pb-6 pt-16" style="padding-left: 80px; padding-right: 100px">
    <h1 class="mb-5">Announcements</h1>
    <v-row>
      <v-col cols="12" style="max-width:75%" v-for="(announcement, index) in announcements" :key="index">
      <v-card class="mx-auto">
        <v-card-text class="pb-2 mt-2">
          <p class="text-dark-primary text-display-semibold text-font-size-22">
            {{announcement.title}}
          </p>
          <p class="text-dark-tertiary text-font-size-14">Announcement posted on {{announcement.timestamp}}</p>
          <p v-if="announcement.editedTimestamp != ''" class="text-dark-tertiary text-font-size-14">Edited on {{announcement.editedTimestamp}}</p>
          <p class="text-dark-tertiary text-font-size-16">{{announcement.body}}</p>
          <v-spacer></v-spacer>
        </v-card-text>
      </v-card>

      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { Announcement } from "@/types/announcement";

export default Vue.extend({
  name: "Announcements",
  data: () => ({
    announcements: [] as Array<Announcement>
  }),

  methods: {
    populateAnnouncements() {
      fetch("https://nushigh.school/chokola/announcements/get_announcements", {
        method: "GET",
        headers: {
          "accept": "application/json",
        }
      }).then(
        response => response.json().then(
          data => {
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
            for (const annKey in data.data[0]) {
              const announcement: Announcement = JSON.parse(JSON.stringify(data.data[0][parseInt(annKey)]));
              this.announcements.push(announcement);
            }
          }
        )
      );
    },
  },
  created() {
    this.populateAnnouncements();
  }
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
