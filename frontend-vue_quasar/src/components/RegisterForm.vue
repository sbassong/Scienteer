<!-- eslint-disable no-alert -->
<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <q-page class="flex flex-center bg-grey-2">
        <PreviousButton backLink="/" />
        <q-card class="q-pa-md shadow-2 my_card" bordered>
          <q-card-section class="text-center">
            <div class="text-grey-9 text-h5 text-weight-bold">Sign up</div>
            <div class="text-grey-8">Create your account</div>
          </q-card-section>

          <q-card-section>
            <q-input dense outlined v-model="name" label="Full Name"></q-input>
            <q-input dense outlined class="q-mt-md" v-model="email" label="Email Address"></q-input>
            <q-input dense outlined class="q-mt-md" v-model="password"
              type="password" label="Password"></q-input>
            <q-input dense outlined class="q-mt-md" v-model="c_password"
              type="password" label="Confirm Password"></q-input>
          </q-card-section>

          <q-card-section>
            <q-btn style="border-radius: 8px;" color="dark" rounded size="md" @click="handleSubmit"
              label="Sign up" no-caps class="full-width"></q-btn>
          </q-card-section>
          <q-card-section class="text-center q-pt-none">
            <div class="text-grey-8">Already have an account?
              <a href="/login" class="text-dark text-weight-bold" style="text-decoration: none">
                Signin.
              </a>
            </div>
          </q-card-section>
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue';
import PreviousButton from './PreviousButton.vue';
import { RegisterUser } from '../services/auth';
// import {validationMixin} from 'vuelidate'
// import {required, maxLength, email} from 'vuelidate/lib/validators'

export default defineComponent({
  name: 'RegisterForm',
  components: {
    PreviousButton,
  },
  // mixins: [validationMixin],

  // validations: {
  //   name: { required, maxLength: maxLength(30) },
  //   email: { required, email },
  //   password: { required },
  //   select: { required },
  // },

  data: () => ({
    name: '',
    email: '',
    password: '',
    c_password: '',
    select: null,
    researcher: null,
    roles: ['Scienteer', 'Researcher'],
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault();
      if (this.password !== this.c_password) {
        alert('Passwords do not match');
        return;
      }
      console.log('I passed the check');
      const userBody = {
        name: this.name,
        email: this.email,
        password: this.password,
        researcher: this.scienteerOrNo(),
      };
      await RegisterUser(userBody);
      this.name = '';
      this.email = '';
      this.password = '';
      this.researcher = null;
      this.$router.push('/login');
    },
    scienteerOrNo() {
      if (this.select === 'Scienteer') return false;
      return true;
    },
  },
});
</script>

<style scoped>
  .my_card {
    width: 25rem;
    border-radius: 8px;
    box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
  }
</style>
