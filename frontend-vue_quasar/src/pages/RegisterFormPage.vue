<template>
  <RegisterForm />
</template>

<script>
import { defineComponent } from 'vue';
import RegisterForm from '../components/RegisterForm.vue';
// import {validationMixin} from 'vuelidate'
// import {required, maxLength, email} from 'vuelidate/lib/validators'

export default defineComponent({
  name: 'RegisterFormPage',
  components: {
    RegisterForm,
  },

  data: () => ({
  }),
});
</script>
