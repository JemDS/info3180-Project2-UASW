<template>
  <q-page class="flex flex-center">
    <b-card title="Register New User">
      <b-form>
        <b-form-row>
          <b-form-group
            id="input-group-username"
            label="Username:"
            label-for="input-username"
          >
            <b-form-input
              id="input-username"
              v-model="form.username"
              type="text"
              placeholder="Username"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group
            class="ml-3"
            id="input-group-password"
            label="Password:"
            label-for="input-password"
          >
            <b-form-input
              id="input-password"
              v-model="form.password"
              type="password"
              placeholder="Password"
              required
            ></b-form-input>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group
            id="input-group-name"
            label="Fullname:"
            label-for="input-name"
          >
            <b-form-input
              id="input-name"
              v-model="form.name"
              type="text"
              placeholder="Jane Doe"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group
            class="ml-3"
            id="input-group-email"
            label="Email:"
            label-for="input-email"
          >
            <b-form-input
              id="input-email"
              v-model="form.email"
              type="email"
              placeholder="Example@example.com"
              required
            ></b-form-input>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group
            id="input-group-location"
            label="Location:"
            label-for="location"
          >
            <b-form-input
              id="location"
              v-model="form.location"
              type="text"
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
              v-model="text"
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
              v-model="form.photo"
              :state="Boolean(form.photo)"
              placeholder="Choose a file or drop it here..."
              drop-placeholder="Drop file here..."
            ></b-form-file>
          </b-form-group>
        </b-form-row>
        <b-button type="submit" variant="success">Register</b-button>
      </b-form>
    </b-card>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "",
        password: "",
        name: "",
        email: "",
        location: "",
        biography: "",
        photo: ""
      }
    };
  }
};
</script>

<style scoped></style>
