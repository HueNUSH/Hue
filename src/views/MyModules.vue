<template>
  <v-container fluid class="pb-6 pt-16" style="padding-left: 80px; padding-right: 100px">
    

    <h1 v-if="msUser">Welcome back, {{ msUser.name }}!</h1>
    <h1 v-else>Please Sign In</h1>

    <p class="text-dark-tertiary text-font-size-16">Academic Week</p>
    
    <v-btn elevation="2" @click="$msal.signOut()" v-if="msUser" > Sign Out</v-btn>
    <v-btn @click="$msal.signIn()" v-else > Sign In Using Microsoft <v-icon right>mdi-microsoft</v-icon></v-btn>

    


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
                    <b>{{ module.unitsCompleted }}/{{ module.units.length }}</b> units completed
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
// @ts-ignore
import { msalMixin } from 'vue-msal'; 
// @ts-ignore
import msal from 'vue-msal'

Vue.use(msal, {
    auth: {
      clientId: 'a3f9eae8-f870-4197-bf20-3c759610892e',
      postLogoutRedirectUri: 'http://huelearning.space/modules',
      
    }
});

// @ts-ignore
import VueCookies from "vue-cookies"
import { Modules } from "@/types/modules";
import { User } from "@/types/user";
// @ts-ignore
import GoogleSignInButton from "vue-google-identity-login-btn";

Vue.use(VueCookies, { expire: "1m", path: "/"});

export default Vue.extend({
  name: "MyModules",
  mixins: [msalMixin],
  directives: {
    GoogleSignInButton
  },
  
  data: () => ({
    isSignedIn: false,
    user: {} as User,
    modules: [] as Array<Modules>
  }),
  methods: {
    getGeneralModules(): Promise<Array<Modules>>{
      return new Promise<Array<Modules>>(resolve => {
        fetch(Vue.prototype.$backendLink + "/chokola/modules/get_modules", {
          method: "GET",
          headers: {
            "accept": "application/json",
          }
        }).then(
          response => response.json().then(
            data => {
              resolve(data.data);
            }
          )
        );
      });
    },
    getModule(moduleId : string, userId : string): Promise<Modules>{
      
        return new Promise<Modules>(resolve => {
        fetch(Vue.prototype.$backendLink + "/chokola/users/get_user_module?" + new URLSearchParams({
          "userId" : userId,
          "moduleId" : moduleId
          
        }), {
          method: "GET",
          headers: {
            "accept": "application/json",
          }
        }).then(
          response => response.json().then(
            data => {
              resolve(data.data);
            }
          )
        );
      });
    } ,
    populateGeneralModules() {
      this.getGeneralModules().then(data => {
          for (const moduleKey in data) {
            const module: Modules = JSON.parse(JSON.stringify(data[parseInt(moduleKey)]));
            this.modules.push(module);
          }
        }
      );
    },
    populateUserModules(userId: string) {
      fetch(Vue.prototype.$backendLink + "/chokola/users/get_user?" + new URLSearchParams({
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
            for (const moduleId in data.data.userModules) {

              this.getModule(moduleId, userId).then(
                data => {
                  const module: Modules = JSON.parse(JSON.stringify(data));
            this.modules.push(module);
                }
              );

            }
          }
        )
      );
    },


    onMSALAuthSuccess(msalAuth : any){
      if(this.$cookies.get("userId")){
        console.log("Already Signed In!");
      } else {
        this.isSignedIn = true;
        console.log("Signed in account!")

        this.user = new User();
        this.user.userId = msalAuth.accountIdentifier;
        this.user.username = msalAuth.name;
        this.user.email = msalAuth.userName;
        this.user.createdAt = Date.now();
        this.user.userModules = [];
        fetch(Vue.prototype.$backendLink + "/chokola/users/user_exists?" + new URLSearchParams({
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
              else {
                this.populateUserModules(this.user.userId);
                this.$cookies.set("userId", this.user.userId);
              }
            }
          ))
        
      }
    },

    createNewUser() {
      fetch(Vue.prototype.$backendLink + "/chokola/users/create_user", {
        method: "POST",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.user),
      }).then(
        response => {
          if (response.status === 200) {
            this.populateUserModules(this.user.userId);
            this.$cookies.set("userId", this.user.userId);
          }
          else console.log("Couldn't create user"); //TODO: Error Handling
        }
      );
    },
    signOut() {
      //@ts-ignore
      // google.accounts.id.disableAutoSelect();
      console.log("Signed Out!")
      this.user = {} as User;
      this.isSignedIn = false;
      this.populateGeneralModules();
      this.$cookies.set("userId", "");
    }
  },  
  computed:{
    msUser(){
      let msUser = null;
      if(this.msal.isAuthenticated){
        msUser = {
          ...this.msal.user,
          profile: {}
        }
        if (this.msal.graph && this.msal.graph.profile){
          msUser.profile = this.msal.graph.profile;
        }
        console.log(msUser);
        this.onMSALAuthSuccess(msUser);
      } else {
        this.signOut();
      }
      return msUser;
    }
  },
  created() {
    const userId = this.$cookies.get("userId");
    if (userId === null) {
      this.populateGeneralModules();
    }
    else {
      fetch(Vue.prototype.$backendLink + "/chokola/users/user_exists?" + new URLSearchParams({
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
              this.user.userId = userId;
              this.user.username = data.data.username;
              this.populateUserModules(this.user.userId);
              this.isSignedIn = true;
            }
            else {
              this.populateGeneralModules();
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
</style>
