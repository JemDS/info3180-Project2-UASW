<template>
  <q-page class="flex flex-center">
    <b-card title="Register New User">
      <b-form @submit.prevent="handleRegister">
        <b-form-row>
          <b-form-group
            id="input-group-username"
            label="Username:"
            label-for="input-username"
          >
            <b-form-input
              id="input-username"
              v-model="user.username"
              placeholder="Username"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group
            class="ml-4"
            id="input-group-password"
            label="Password:"
            label-for="input-password"
          >
            <b-form-input
              id="input-password"
              v-model="user.password"
              type="password"
              placeholder="Password"
              required
            ></b-form-input>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group
            class="ml-3"
            id="input-group-fname"
            label="First Name:"
            label-for="input-fname"
          >
            <b-form-input
              id="input-fname"
              v-model="user.fName"
              placeholder="Jane"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group
            class="ml-3"
            id="input-group-lname"
            label="Last Name:"
            label-for="input-lname"
          >
            <b-form-input
              id="input-lname"
              v-model="user.lName"
              placeholder="Doe"
              required
            ></b-form-input>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group
            class="ml-3"
            id="input-group-email"
            label="Email:"
            label-for="input-email"
          >
            <b-form-input
              id="input-email"
              v-model="user.email"
              type="email"
              placeholder="Example@example.com"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id="input-group-location"
            label="Location:"
             class="ml-3"
            label-for="location"
          >
            <b-form-input
              id="location"
              v-model="user.location"
              placeholder="Kingston, Jamaica"
              required
            ></b-form-input>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group
            id="input-group-biography"
            label="Biography:"
            label-for="input-biography"
          >
            <b-form-textarea
              id="input-biography"
              v-model="user.biography"
              placeholder="Start writing your bio..."
              cols="48"
              rows="2"
              max-rows="6"
            ></b-form-textarea>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group
            id="input-group-photo"
            label="Photo:"
            label-for="input-photo"
          >
            <b-form-file
              id="input-photo"
              v-model="photo"
              :state="Boolean(user.photo)"
              placeholder="Choose a file or drop it here..."
              drop-placeholder="Drop file here..."
            ></b-form-file>
          </b-form-group>
        </b-form-row>
        <div
          v-if="message"
          class="alert"
          :class="successful ? 'alert-success' : 'alert-danger'"
        >
          {{ message }}
        </div>
        <b-button type="submit" variant="success">Register</b-button>

      </b-form>
    </b-card>
  </q-page>
</template>

<script>
import User from "../models/user";
import axios from "axios";
export default {
  data() {
    return {
      user: new User("", "", ""),
      submitted: false,
      successful: false,
      message: "",
      photo: []
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  mounted() {
    if (this.loggedIn) {
      this.$router.push("/register");
    }
  },
  methods: {
    handleRegister() {
      this.message = "";

      const upload_url =
        " https://api.cloudinary.com/v1_1/djhycr4me/image/upload";
      const fd = new FormData();

      fd.append("file", this.photo);
      fd.append("upload_preset", "webdev2");

      axios.post(upload_url, fd).then(res => {
        this.user.photo = res.data.url;
        this.$store.dispatch("auth/register", this.user).then(
          data => {
            this.message = "User added Successfully";
            this.successful = true;
          },
          error => {
            this.message =
              (error.response && error.response.data) ||
              error.message ||
              error.toString();
            this.successful = false;
          }
        );
      });
    }
  }
};
</script>

<style scoped></style>
