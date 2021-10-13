<template>
  <div class="artist-content">
    <ArtistBio :name='artistDetails.name' :picture='artistDetails.picture' :bio='artistDetails.bio'/>
    <Forum :posts='artistDetails.posts' :artist_id='artistDetails.id'/>
  </div>
</template>

<script>

export default {
  name: 'ResearcherDetails',
  data: () => ({

  }),
  components: {

  },
  mounted() {

  },
  methods: {

  }
}
</script>

<style scoped>

</style>