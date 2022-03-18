<template>
  <n-card size="medium" :style="cardStyle" content-style="padding: 0">
    <n-skeleton v-if="!anime" class="image" />
    <img v-else :src="anime?.image" class="image" />
    <n-space vertical justify="end" class="card-footer" :size="[0, 0]">
      <div v-if="anime">
        <div class="gradient" style="height: 40px" />
        <n-space vertical :size="[0, 0]" class="card-data">
          <n-text style="margin-bottom: 0; font-size: 18px; color: white">{{
            year
          }}</n-text>
          <n-text style="font-size: 18px; color: #63e2b7">{{ name }}</n-text>
          <n-text style="color: white">{{ getGenres(anime.genres) }}</n-text>
        </n-space>
      </div>
    </n-space>
  </n-card>
</template>

<script>
import useBreakpoints from "vue-next-breakpoints";

export default {
  name: "AnimeListCard",
  props: {
    anime: { type: Object, default: undefined },
  },
  setup() {
    const bp = useBreakpoints({
      xs: 550,
      sm: 1000,
      md: 1500,
      lg: [1501],
    });
    return { bp };
  },
  computed: {
    name() {
      return this.anime.name || this.anime.original_name;
    },
    year() {
      return this.anime.premiere_date.split("-")[0];
    },
    cardStyle() {
      const style = { width: "17vw" };
      if (this.bp.md.matches) {
        style.width = "20vw";
      }
      if (this.bp.sm.matches) {
        style.width = "35vw";
      }
      if (this.bp.xs.matches) {
        style.width = "90vw";
      }
      style.height = `${parseInt(style.width) * 1.5}vw`;
      style.marginBottom = "8px";
      style.height = "60vh";
      return style;
    },
  },
  methods: {
    getGenres(ids) {
      const genres = [];
      for (const id of ids) {
        const name = this.$store.state.cache.genres[id];
        if (!name) continue;
        genres.push(name);
      }
      return genres.join(", ");
    },
  },
};
</script>

<style scoped>
.gradient {
  margin-bottom: 0;
  background: linear-gradient(
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0) 17%,
    rgba(0, 0, 0, 0.7) 77%,
    rgba(0, 0, 0, 0.8) 100%
  );
}
.image {
  object-fit: cover;
  width: 100%;
  height: 100%;
  position: absolute;
}
.card-footer {
  bottom: 0;
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: 2;
}
.card-data {
  background-color: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(2px);
  font-weight: bold;
  padding: 8px;
}
</style>
