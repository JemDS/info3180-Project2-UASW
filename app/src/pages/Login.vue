<template>
  <q-page class="flex flex-center">
    <div style="width:25%">
      <b-card title="Login to your account">

        <b-form>
          <b-form-group
            id="input-group-1"
            label="Username:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="form.username"
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
              v-model="form.password"
              type="password"
              placeholder="Password"
              required
            ></b-form-input>
          </b-form-group>

          <b-button block type="submit" variant="success">Login</b-button>
        </b-form>
      </b-card>
    </div>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "",
        password: ""
      }
    };
  }
};
</script>

<style></style>
