<template>
  <q-page class="flex flex-center home-page">
    <div style="width:100%">
      <b-row>
        <b-col
          cols="6"
          align-v="center"
          class="p-6 flex flex-center"
          align-self="center"
        >
          <div style="width:50%">
            <b-row><h1><strong>Buy and Sell Cars Online</strong></h1></b-row>
            <b-row
              ><p>
                United Auto Sales provides the fastest, easiest and most user
                friendly way to buy or sell cars online. Find a Great Price on
                the Vehicle You Want
              </p></b-row
            >
            <b-row
              ><b-button variant="primary mr-2">Register</b-button
              ><b-button to="/login" variant="success">Login</b-button></b-row
            >
          </div>
        </b-col>

        <b-col cols="6">
          <b-img
            class="hero-img"
            src="https://images.unsplash.com/photo-1586798563075-5ca1b37d2f92?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDd8fHJlZCUyMGNhcnxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60"
            fluid-grow
          />
        </b-col>
      </b-row>
    </div>
  </q-page>
</template>

<script>
export default {};
</script>

<style scoped></style>
