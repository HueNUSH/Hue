<template>
  <v-container fluid class="pb-6 pt-16" style="padding-left: 80px; padding-right: 100px">
    <h1 v-if="isSignedIn">Welcome back, {{ user.username }}!</h1>
    <h1 v-else>Please Sign In</h1>

    <p class="text-dark-tertiary text-font-size-16">Academic Week</p>
    <div v-if="!isSignedIn" style="display: flex;" id="google-login-btn" v-google-identity-login-btn="{ clientId, locale: 'en' }">
    </div>
    <v-btn elevation="2" v-else @click="signOut"> Sign Out</v-btn>

    <h2 class="text-dark-primary text-display-semibold text-font-size-16 pb-3" style="margin-top: 75px;">
      My modules
    </h2>
    <div style="max-width: 80rem">
      <v-row>
        <v-col cols="12" lg="4" md="6" v-for="(module, index) in modules" :key="index">
          <router-link class="unit-card" :to="'/modules/' + module._id" :module="module">
            <v-card class="pa-4 fill-height d-flex flex-column" elevation="0">
              <v-row>
                <v-col cols="auto" class="d-flex flex-column">
                  <v-sheet class="rounded-circle d-flex align-center justify-center align-self-baseline" :color="
                    module.moduleIconBackgroundColor === 'orange'
                      ? '#FBDE94'
                      : module.moduleIconBackgroundColor === 'pink'
                        ? '#FFC8F9'
                        : module.moduleIconBackgroundColor === 'green'
                          ? '#C5F4B5'
                          : '#B6EDFE'
                  " :height="40" :width="40">
                    <v-icon>
                      {{ module.moduleIcon }}
                    </v-icon>
                  </v-sheet>


                  <h3 class="text-dark-primary text-display-semibold text-font-size-22">
                    {{ module.moduleName }}
                  </h3>
                  <p class="text-dark-tertiary text-font-size-14">
                    <b>{{ module.unitsCompleted }}/{{ module.units.length }}</b> sections completed
                  </p>
                </v-col>
              </v-row>

              <p class="learn-arrow text-semibold text-font-size-16">View units →</p>
            </v-card>
          </router-link>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { Modules } from "@/types/modules";
import { User } from "@/types/user";
// @ts-ignore
import GoogleSignInButton from "vue-google-identity-login-btn";


export default Vue.extend({
  name: "MyModules",
  directives: {
    GoogleSignInButton
  },
  data: () => ({
    isSignedIn: false,
    user: {} as User,
    modules: [] as Array<Modules>,
    clientId: "766984185858-k7ln7n0dnh3sc8go96nulegdumo4fteq.apps.googleusercontent.com"
  }),

  methods: {
    populateGeneralModules() {
      fetch("http://localhost:8000/chokola/modules/get_modules", {
        method: "GET",
        headers: {
          "accept": "application/json",
        }
      }).then(
        response => response.json().then(
          data => {
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
            for (const moduleKey in data.data) {
              const module: Modules = JSON.parse(JSON.stringify(data.data[parseInt(moduleKey)]));
              this.modules.push(module);
            }
          }
        )
      );
    },
    populateUserModules(userId: string) {
      fetch("http://localhost:8000/chokola/users/get_user?" + new URLSearchParams({
        "userId": userId,
      }), {
          headers: {
            "accept": "application/json",
          }
        }
      ).then(
        response => response.json().then(
          data => {
            this.modules = [] as Array<Modules>;
            console.log(data);
            for (const moduleId in data.data.userModules) {
              const module: Modules = JSON.parse(JSON.stringify(data.data.userModules[moduleId]));
              this.modules.push(module);
            }
          }
        )
      );
    },
    onGoogleAuthSuccess(jwtCredentials: any) {
      console.log(jwtCredentials);
      const profileData = JSON.parse(atob(jwtCredentials.split(".")[1]));
      this.isSignedIn = true;

      this.user = new User();
      this.user.userId = profileData.sub;
      this.user.username = profileData.name;
      this.user.email = profileData.email;
      this.user.createdAt = Date.now();
      this.user.userModules = [];

      fetch("http://localhost:8000/chokola/users/user_exists?" + new URLSearchParams({
        "userId": this.user.userId,
      }), {
          headers: {
            "accept": "application/json",
          }
        }
      ).then(
        response => response.json().then(
          data => {
            if (!data.data.exists) {
              for (const moduleKey in this.modules) {
                this.user.userModules.push(this.modules[parseInt(moduleKey)]._id);
              }
              this.createNewUser();
            }
            else this.populateUserModules(this.user.userId);
          }
        )
      );
    },
    createNewUser() {
      fetch("http://localhost:8000/chokola/users/create_user", {
        method: "POST",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.user),
      }).then(
        response => {
          if (response.status === 200) this.populateUserModules(this.user.userId);
          else console.log("Couldn't create user"); //TODO: Error Handling
        }
      );
    },
    signOut() {
      google.accounts.id.disableAutoSelect();
      this.user = {} as User;
      this.isSignedIn = false;
      this.populateGeneralModules();
    }
  },
  created() {
    this.populateGeneralModules();
  }
});
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";
@import "../styles/global.scss";
</style>
