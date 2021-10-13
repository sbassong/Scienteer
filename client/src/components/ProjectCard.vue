<template>
  <div class="card project-card" >
    <div class="image-cont">
      <!-- <img :src='' alt=""> -->
    </div>
    <div class="info-cont flex-col">
      <h3>{{}}</h3>
      <h3>{{}}</h3>
    </div>
    
    <!-- <div class="info-cont flex-col">
      <p>{{}}</p>
      <p>{{}}</p>
    </div> -->

  </div>
</template>

<script>
export default {
  name: 'ArtistCard',
  props: {

  }
}
</script>

<style scoped>
  .card {
  max-width: 300px;
  max-height: 380px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
  margin: 0.5em
}

.card:hover {
  opacity: 0.8;
}

.card .image-cont {
  width: auto;
}

.card img {
  width: 100%;
  height: 200px;
}

.card .info-cont {
  padding: 1em;
}
</style>