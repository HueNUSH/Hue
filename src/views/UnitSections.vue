<template>
  <v-app>
    <v-container fluid class="px-12 py-6 text-font-size-16">
      <div d-flex>
        <div class="pa-14" style="display:inline-block;vertical-align: top;">
          <v-card elevation="12" width="256">
            <v-navigation-drawer floating permanent>

              <v-list dense rounded class="py-6">

                <v-list-item :key="'About'"
                  :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no + '/about'">
                  <v-list-item-icon>
                    <v-icon>mdi-information</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>About</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>


                <v-list-item>
                  <v-divider></v-divider>
                </v-list-item>

                <v-list-item v-for="(section, index) in unit.sections"
                  :key="section.sectionName"
                  :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no + '/' + section.sectionName"
                  @click="carrySectionData(section.sectionDesc, section.mediaType, section.sectionMedia)"
                  >
                  <v-list-item-icon>
                    <v-icon>{{ section.sectionIcon }}</v-icon>
                  </v-list-item-icon>

                  <v-list-item-content>
                    <v-list-item-title>{{ section.sectionName }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-navigation-drawer>
          </v-card>
        </div>

        <div class="pa-14" style="display:inline-block;vertical-align: top;width:70%">
          <router-link :to="'/modules/' + $route.params.module_id" class="links">
            &lt; Back to Module
          </router-link>

          <v-main class="py-6" fluid full-width>
            <router-view :sectionDesc="sectionDesc" :sectionMedia="sectionMedia" :mediaType="mediaType"/>
          </v-main>

        </div>

      </div>
    </v-container>
  </v-app>
</template>

<script lang="ts">
import { Units } from "@/types/units";
import Vue from "vue"
export default Vue.extend({
  name: "UnitSections",
  data: () => ({
    unit: Units,
    sectionDesc: "",
    mediaType: "",
    sectionMedia: "",
    userId: "",
  }),
  methods: {
    carrySectionData(sectionDesc:string, mediaType:string, sectionMedia:string){
      this.sectionDesc = sectionDesc;
      this.sectionMedia = sectionMedia;
      this.mediaType = mediaType;
    },

    async populateGeneralSections(moduleId: string, unitIndex: string) {
      await fetch("http://localhost:8000/chokola/modules/get_unit/?" + new URLSearchParams({
        "module_id": moduleId,
        "unit_index": unitIndex
      }), {
        method: "GET",
      }).then(
        response => response.json().then(
          data => {
            this.unit = JSON.parse(JSON.stringify(data.data));
          }
        )
      );
    },
    async populateUserSections(userId: string, moduleId: string, unitIndex: string) {
      fetch("http://localhost:8000/chokola/users/get_user_unit?" + new URLSearchParams({
        "userId": userId,
        "moduleId": moduleId,
        "unitIndex": unitIndex
      }), {
        method: "GET",
      }).then(
        response => response.json().then(
          data => {
            this.unit = JSON.parse(JSON.stringify(data.data));
          }
        )
      );
    }
  },
  async created() {
    const userId = this.$cookies.get("userId");
    if (userId === null) {
      await this.populateGeneralSections(this.$route.params.module_id, this.$route.params.unit_no);
    }
    else {
      await fetch("http://localhost:8000/chokola/users/user_exists?" + new URLSearchParams({
        "userId": userId,
      }), {
          headers: {
            "accept": "application/json",
          }
        }
      ).then(
        response => response.json().then(
          data => {
            if (data.data.exists) {
              this.userId = userId;
              this.populateUserSections(userId, this.$route.params.module_id, this.$route.params.unit_no);
            }
            else {
              this.populateGeneralSections(this.$route.params.module_id, this.$route.params.unit_no);
            }
          }
        )
      );
    }
  }
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";

::v-deep .v-list-item {
  color: $c-primary-accent  !important;
  opacity: 1 !important;
}

::v-deep .v-list-item--active:before,
.v-list-item--active:hover:before,
.v-list-item:focus:before {
  opacity: 0.2 !important;
}
</style>
