<template>
  <q-page class="flex flex-center">
    <div style="width:25%">
      <b-card title="Login to your account">
        <b-form validated @submit.prevent="handleLogin">
          <b-form-group
            id="input-group-1"
            label="Username:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="user.username"
              type="text"
              placeholder="Username"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id="input-group-1"
            label="Password:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="user.password"
              type="password"
              placeholder="Password"
              required
            ></b-form-input>
          </b-form-group>

          <b-button block type="submit" variant="success">
            <span
              v-show="loading"
              class="spinner-border spinner-border-sm"
            ></span>
            <span>Login</span></b-button
          >
          <div v-if="message" class="alert alert-danger" role="alert">
            {{ message }}
          </div>
        </b-form>
      </b-card>
    </div>
  </q-page>
</template>

<script>
import User from "../models/user";
export default {
  data() {
    return {
      user: new User("", ""),
      loading: false,
      message: ""
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  created() {
    if (this.loggedIn) {
      this.$router.push("/login");
    }
  },
  methods: {
    handleLogin() {
      this.loading = true;

      if (this.user.username && this.user.password) {
        this.$store.dispatch("auth/login", this.user).then(
          () => {
            this.$router.push("/");
          },
          error => {
            this.loading = false;
            this.message =
              (error.response && error.response.data) ||
              error.message || "Internal Server Error"

          }
        );
      }
    }
  }
};
</script>

<style></style>
