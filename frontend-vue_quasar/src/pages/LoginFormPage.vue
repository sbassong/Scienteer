<template>
  <div>
    <LoginForm />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import LoginForm from '../components/LoginForm.vue';

export default defineComponent({
  name: 'LoginFormPage',
  components: { LoginForm },

  data: () => ({
  }),

  methods: {
  },
});
</script>
