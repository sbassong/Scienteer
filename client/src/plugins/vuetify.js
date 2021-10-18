import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: colors.blue.darken1, // #E53935
        secondary: colors.purple.lighten3, // #FFCDD2
        accent: colors.purple.darken1, // #3F51B5
      },
    },
  },
});
