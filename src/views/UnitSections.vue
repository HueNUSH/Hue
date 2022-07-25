<template>
  <v-app>
    <v-container fluid class="px-12 py-6 text-font-size-16 fill-height">
      <v-row class="d-flex align-start fill-height">
        <v-col cols="3" class="pa-14">
          <v-card elevation="12" class="d-inline-flex">
            <v-navigation-drawer floating permanent>

              <v-list dense rounded class="py-6">

                <v-list-item :key="'About'"
                             :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no + '/about'"
                             @click="sectionIndex = -1"
                >
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
                               :to="'/modules/' + $route.params.module_id + '/' + $route.params.unit_no + '/' + index"
                               @click="carrySectionData(section.sectionDesc, section.mediaType, section.sectionMedia, index);"
                               
                               
                  >
                  <!-- highlighted v-list-item--active v-list-item v-list-item--link theme--light highlighted -->
                  <!-- v-list-item v-list-item--link theme--light highlighted -->
                    <v-list-item-icon>
                      <v-icon>{{ section.sectionIcon }}</v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                      <v-list-item-title>{{ sectionProgress[index] === 1 ? section.sectionName + ' ✓': section.sectionName   }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
              </v-list>
            </v-navigation-drawer>
          </v-card>
        </v-col>


        <v-col cols="8" class="pa-14 ">
          <router-link :to="'/modules/' + $route.params.module_id" class="links">
            &lt; Back to Module
          </router-link>

          <v-main class="py-6" fluid full-width>
            <router-view :sectionDesc="sectionDesc" :sectionMedia="sectionMedia" :mediaType="mediaType" :unitAbout="unitAbout"/>
          </v-main>
        </v-col>
        <v-col>
          <v-btn icon @click="completeSection">
            <v-icon size="50px">
              mdi-arrow-right-bold-circle-outline
            </v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script lang="ts">
import { Units } from "@/types/units";
import Vue from "vue";
import router from "@/plugins/router";
export default Vue.extend({
  name: "UnitSections",
  data: () => ({
    unit: {} as Units,
    sectionDesc: "",
    mediaType: "",
    sectionMedia: "",
    unitAbout: "",
    sectionIndex: -1,
    userId: "",
    sectionProgress : [] as Array<number>
  }),
  methods: {
    carrySectionData(sectionDesc:string, mediaType:string, sectionMedia:string, sectionIndex: number){
      this.sectionDesc = sectionDesc;
      this.sectionMedia = sectionMedia;
      this.mediaType = mediaType;
      this.sectionIndex = sectionIndex;
    },
    async completeSection(){
      console.log(this.sectionIndex)
      console.log(this.userId)
      if (this.sectionIndex >= 0 && this.userId !== "") {
        await fetch(Vue.prototype.$backendLink + "/chokola/users/complete_section?" + new URLSearchParams({
          "userId": this.userId,
          "moduleId": this.$route.params.module_id,
          "unit_index": this.$route.params.unit_no,
          "section_index": String(this.sectionIndex)
        }), {
          method: "PUT",
          headers: {
            "Accept": "application/json",
          },
        }).then(
          response => response.json().then(
            data => {
              console.log(data);
            }
          )
        );
      }
      if (this.sectionIndex !== this.unit.sections.length-1) {
        await router.push({name: "unitContent", params: {
            module_id: this.$route.params.module_id,
            unit_no: this.$route.params.unit_no,
            section: String(this.sectionIndex + 1)
          }}
        );
        const section = this.unit.sections[this.sectionIndex+1];
        this.carrySectionData(section.sectionDesc, section.mediaType, section.sectionMedia, this.sectionIndex+1);
      }
      else {
        await router.push({name: "moduleUnits", params:{module_id: this.$route.params.module_id}});
      }
    },

    async populateGeneralSections(moduleId: string, unitIndex: string) {
      await fetch(Vue.prototype.$backendLink + "/chokola/modules/get_unit/?" + new URLSearchParams({
        "module_id": moduleId,
        "unit_index": unitIndex
      }), {
        method: "GET",
      }).then(
        response => response.json().then(
          data => {
            this.unit = JSON.parse(JSON.stringify(data.data));
            this.unitAbout = this.unit.unitAbout;
          }
        )
      );
    },
    async populateUserSections(userId: string, moduleId: string, unitIndex: string) {
      fetch(Vue.prototype.$backendLink + "/chokola/users/get_user_unit?" + new URLSearchParams({
        "userId": userId,
        "moduleId": moduleId,
        "unitIndex": unitIndex
      }), {
        method: "GET",
      }).then(
        response => response.json().then(
          data => {
            console.log("here")
            this.unit = JSON.parse(JSON.stringify(data.data));
            this.sectionProgress = this.unit.sectionProgress
            
            console.log(+this.sectionProgress[0])
          }
        )
      );
    }
  },
  async created() {
    Vue.prototype.$moduleExists(this.$route.params.module_id).then(async (exists: boolean) => {
      if (!exists) {
        this.$emit("not-found", true);
      } else {
        const userId = this.$cookies.get("userId");

        if (userId === null) {
          await this.populateGeneralSections(this.$route.params.module_id, this.$route.params.unit_no);
        } else {
          await fetch(Vue.prototype.$backendLink + "/chokola/users/user_exists?" + new URLSearchParams({
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

                } else {
                  this.populateGeneralSections(this.$route.params.module_id, this.$route.params.unit_no);
      
                }
                if(this.$route.params.section != undefined) {
                  console.log(this.$route.params.section)
                  this.sectionIndex = +(this.$route.params.section)}
              } 
            )
          );
        }
      }
    });
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

::v-deep .v-btn__content {
  color: $c-text-dark-tertiary;
}

.v-btn {
  position: fixed;
  right: 5%;
  bottom: 50%;
  transform: translate(-50%, -50%);
  margin: 0 auto;  // Without this the box extends the width of the page
}
</style>
